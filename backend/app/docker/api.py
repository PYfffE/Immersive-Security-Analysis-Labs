import os
import time

import docker
import docker.errors
import docker.transport
from docker.models.containers import Container

from app.models.container_config import ContainerConfig

docker_remote_host = os.getenv("DOCKER_REMOTE_HOST")
user = os.getenv("SSH_USER")
port = os.getenv("SSH_PORT")


def init_docker_connection():
    return docker.DockerClient(base_url=f"ssh://{user}@{docker_remote_host}:{port}")


def run_docker_image(
    container_config: ContainerConfig,
    force_deploy: bool = False,
    running_container_id: str = None,
) -> Container:
    client = init_docker_connection()
    container = None
    if running_container_id is not None:
        try:
            container = client.containers.get(running_container_id)
            if force_deploy is True:
                container.stop()
                container.remove()
            else:
                container.start()
        except docker.errors.NotFound:
            pass
    if container is None or force_deploy is True:
        container: Container = client.containers.run(
            container_config.image_name,
            detach=True,
            name=container_config.container_name,
            command=container_config.command,
            environment=container_config.environment,
            ports=container_config.ports,
        )

    container.reload()
    timeout = 120
    stop_time = 0.5
    t_start = time.monotonic()
    while (
        container.status != "running" or not is_ports_assigned(container)
    ) and time.monotonic() - t_start < timeout:
        time.sleep(stop_time)
        continue
    client.close()
    return container


def get_docker_container_for_name(container_name: str):
    if container_name is None:
        return None
    client = init_docker_connection()
    try:
        container = client.containers.get(container_name)
    except docker.errors.NotFound:
        return None
    client.close()

    return container


def stop_docker_container(container_id: str):
    client = init_docker_connection()
    container = client.containers.get(container_id)
    container.stop()
    client.close()


def is_ports_assigned(container: Container):
    container.reload()
    # check that each port has external port assigned

    return (
        container.ports is not None
        and len(container.ports) > 0
        and all(
            len(container.ports[assigned_port]) > 0 for assigned_port in container.ports
        )
    )
