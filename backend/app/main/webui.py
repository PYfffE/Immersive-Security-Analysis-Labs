from flask import render_template, request, g
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from app import db
from app.docker.api import get_docker_container_for_name, docker_remote_host
from app.main import bp
from app.main.auth import login_required

LIST_LIMIT = 10


class LoginForm(FlaskForm):
    username = StringField(
        "Логин",
        validators=[DataRequired(), Length(1, 20)],
        render_kw={"placeholder": "Логин"},
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(), Length(8, 150)],
        render_kw={"placeholder": "Пароль"},
    )
    submit = SubmitField(label="Войти")


@bp.route("/login")
def login():
    form = LoginForm()
    return render_template("main/login.html", form=form)


@bp.route("/")
@bp.route("/index")
@bp.route("/tasks")
@login_required
def tasks():
    page: int = int(request.args["page"]) if "page" in request.args else 1
    l, p = db.get_tasks_list(
        (page - 1) * LIST_LIMIT, LIST_LIMIT, task_ids=g.student.available_tasks
    )
    return render_template("main/tasks.html", list=l, pagination=p)


@bp.route("/task/<int:task_id>")
@bp.route("/task/<int:task_id>/details")
@login_required
def task_by_id(task_id: int):
    if task_id not in g.student.available_tasks:
        return "Task not available", 403
    task = db.get_task(task_id)
    return render_template("main/task_details.html", task=task)


@bp.route("/task/<int:task_id>/practice")
@login_required
def task_practice(task_id: int):
    if task_id not in g.student.available_tasks:
        return "Task not available", 403
    task = db.get_task(task_id)
    container_status = None
    container_ip = None
    container_ports = None
    task_container = db.get_task_container(task_id, g.student.student_id)
    if task_container is not None:
        container = get_docker_container_for_name(task_container.container_name)
        if container is not None:
            container_status = container.status
            container_ip = docker_remote_host
            container_ports = [
                docker_port_info[0]["HostPort"]
                for (docker_port, docker_port_info) in container.ports.items()
            ]

    return render_template(
        "main/task_practice.html",
        task=task,
        container_status=container_status,
        container_ip=container_ip,
        container_ports=container_ports,
        task_container_info=task_container,
    )
