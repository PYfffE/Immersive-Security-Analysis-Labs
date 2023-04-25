import os

import paramiko
from flask import request, session, redirect, url_for

from backend.app import db
from backend.app.admin import bp
from backend.app.admin.auth import login_required


@bp.post('/tasks/list')
@login_required
def tasks_list():
    return db.get_tasks_list()

host = os.getenv("SSH_HOST")
user = os.getenv("SSH_USER")
secret = os.getenv("SSH_PASSWORD")
port = os.getenv("SSH_PORT")


@bp.post("/deploy/<task_id>")
@login_required
def deploy(task_id: str):
    rs = run_docker_compose(task_id)
    return {
        "message": "Deployed!",
        "remote_message": "rs",
        "ip": request.host
    }

@bp.post('/student/add')
@login_required
def add_student_account():
    username = request.form.get('username')
    password = request.form.get('password')
    db.add_student(username, password)
    return redirect(url_for('admin.students'))


def run_docker_compose(name: str) -> str:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    # stdin, stdout, stderr = client.exec_command(f'[ -d "{name}" ] && echo "Yes"')
    stdin, stdout, stderr = client.exec_command(f'ls')
    data: str = str(stdout.read())
    print(data)
    if name in data:
        stdin, stdout, stderr = client.exec_command(f'cd {name} && '
                                                    f'sudo /usr/bin/docker-compose up --force-recreate -d --build')
        data = str(stdout.read() + stderr.read())
        print(data)
    client.close()
    return data