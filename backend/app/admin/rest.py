import docker
import docker.errors
from flask import request, redirect, url_for, g

from app import db
from app.admin import bp
from app.admin.auth import login_required
from app.docker.api import (
    get_docker_container_for_name,
    run_docker_image,
    stop_docker_container,
)
from app.models.task_container import TaskContainer


@bp.post("/tasks/list")
@login_required
def tasks_list():
    return db.get_tasks_list()


@bp.post("/task/<task_id>/deploy")
@login_required
def deploy(task_id: str):
    container_config = db.get_container_config(task_id)
    force_deploy = bool(request.args.get("forceDeploy"))
    running_container_id = None
    container = get_docker_container_for_name(container_config.container_name)
    if not force_deploy and container is not None and container.status == "running":
        return {"error": "Container already running"}, 400
    if container is not None:
        running_container_id = container.id

    try:
        container = run_docker_image(
            container_config, force_deploy, running_container_id
        )
        container_ip = container.attrs["NetworkSettings"]["IPAddress"]
    except docker.errors.ImageNotFound:
        return {"error": f"Image '{container_config.image_name}' not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500

    db.save_task_container(
        TaskContainer(task_id, container.id, container_ip, container_config.image_name)
    )
    return {
        "status": container.status,
        "ip": container_ip,
        "container_ports": container.ports,
    }


@bp.post("/task/<task_id>/stop")
@login_required
def stop(task_id: str):
    task_container = db.get_task_container(task_id, g.student.student_id)
    try:
        stop_docker_container(task_container.container_id)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"status": "Stopped"}


@bp.delete("/task/<task_id>/<container_id>")
@login_required
def delete_container(task_id: str, container_id: str):
    try:
        stop_docker_container(container_id, delete_container=True)
    except Exception as e:
        return {"error": str(e)}, 500
    db.delete_task_container(task_id, container_id)
    return {"status": "Deleted"}


@bp.post("/student/add")
@login_required
def add_student_account():
    username = request.form.get("username")
    password = request.form.get("password")
    db.add_student(username, password)
    return redirect(url_for("admin.students"))
