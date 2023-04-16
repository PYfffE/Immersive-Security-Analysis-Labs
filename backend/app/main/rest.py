import os

import paramiko
from flask import request

from backend.app.main import bp

host = os.getenv("SSH_HOST")
user = os.getenv("SSH_USER")
secret = os.getenv("SSH_PASSWORD")
port = os.getenv("SSH_PORT")


@bp.get("/deploy/{vuln_name}")
async def root(vuln_name: str):
    rs = run_docker_compose(vuln_name)
    return {
        "message": "Deployed!",
        "remote_message": rs,
        "ip": request.host
    }



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