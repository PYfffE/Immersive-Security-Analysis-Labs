import random
import string

import docker
import docker.errors
from flask import request, g

from app import db
from app.docker.api import (
    get_docker_container_for_name,
    run_docker_image,
    stop_docker_container,
    docker_remote_host,
)
from app.main import bp
from app.main.auth import login_required
from app.models.task_container import TaskContainer


def get_docker_container_unique_name(container_name, student_id, task_id) -> str:
    return f"{container_name}-{student_id}-{task_id}"


def generate_random_string(length=10):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


@bp.post("/task/<task_id>/run_container")
@login_required
def run_container(task_id: str):
    force_deploy = bool(request.args.get("forceDeploy"))

    container_config = db.get_container_config(task_id)

    running_container_id = None
    task_container = db.get_task_container(task_id, g.student.student_id)

    if task_container is not None:
        running_container_id = task_container.container_id

    container_config.container_name = get_docker_container_unique_name(
        container_config.container_name, g.student.student_id, task_id
    )

    if running_container_id is None:
        container = get_docker_container_for_name(container_config.container_name)
    else:
        container = get_docker_container_for_name(running_container_id)

    if not force_deploy and container is not None and container.status == "running":
        return {"error": "Container already running", "code": "ALREADY_RUNNING"}, 400

    if container is not None:
        running_container_id = container.id

    ssh_password = generate_random_string(12)
    ssh_username = g.student.username
    flag = generate_random_string(20)

    container_config.environment["SSH_PASSWORD"] = ssh_password
    container_config.environment["SSH_USERNAME"] = ssh_username
    container_config.environment["FLAG"] = flag
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
        TaskContainer(
            task_id,
            g.student.student_id,
            container.id,
            container_ip,
            container_name=container_config.container_name,
            image_name=container_config.image_name,
            container_ssh_password=ssh_password,
            container_ssh_username=ssh_username,
            flag=flag,
        )
    )
    external_ports = [
        docker_port_info[0]["HostPort"]
        for (docker_port, docker_port_info) in container.ports.items()
    ]
    return {
        "status": container.status,
        "ip": docker_remote_host,
        "container_ports": external_ports,
        "ssh_password": container_config.environment["SSH_PASSWORD"],
        "ssh_username": container_config.environment["SSH_USERNAME"],
    }


@bp.post("/task/<task_id>/stop_container")
@login_required
def stop_container(task_id: str):
    task_container = db.get_task_container(task_id, g.student.student_id)
    try:
        stop_docker_container(task_container.container_id)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"status": "Stopped"}


@bp.get("/task/<task_id>/state")
@login_required
def get_container_state(task_id):
    task_container = db.get_task_container(task_id, g.student.student_id)
    if task_container is None:
        return {"status": "not running"}, 404
    container = get_docker_container_for_name(task_container.container_name)
    if container is None:
        return {"status": "not running"}, 404
    external_ports = [
        docker_port_info[0]["HostPort"]
        for (docker_port, docker_port_info) in container.ports.items()
    ]
    return {
        "status": container.status,
        "ip": docker_remote_host,
        "container_ports": external_ports,
    }
