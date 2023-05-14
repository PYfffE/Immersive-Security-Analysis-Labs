class Student:
    def __init__(
        self,
        student_id: str,
        username,
        password,
        name,
        group,
        email,
        available_tasks: list,
    ):
        self.student_id = student_id
        self.username = username
        self.password = password
        self.name = name
        self.group = group
        self.email = email
        self.available_tasks = available_tasks
