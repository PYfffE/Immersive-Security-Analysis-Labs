class ContainerConfig:
    def __init__(
        self,
        task_id: str,
        image_name: str,
        container_name: str = None,
        command: str = None,
        environment: dict = {},
        network_config=None,
        ports: dict = {},
    ):
        self.ports = ports
        self.task_id = task_id
        self.image_name = image_name
        self.container_name = container_name
        self.command = command
        self.environment = environment
        self.network_config = network_config
