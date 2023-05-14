class TaskContainer:
    def __init__(
        self,
        task_id: str,
        student_id,
        container_id: str,
        container_ip: str,
        container_name: str = None,
        image_name: str = None,
        container_ssh_password: str = None,
        flag=None,
        container_ssh_username=None,
    ):
        self.task_id = task_id
        self.student_id = student_id
        self.container_id = container_id
        self.container_ip = container_ip
        self.container_name = container_name
        self.image_name = image_name
        self.container_ssh_password = container_ssh_password
        self.flag = flag
        self.container_ssh_username = container_ssh_username
