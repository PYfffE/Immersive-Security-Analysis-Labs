import uuid

from app.models.container_config import ContainerConfig
from app.models.pagination import Pagination
from app.models.student import Student
from app.models.task import Task
from app.models.task_container import TaskContainer
from app.models.user import User


def get_user_by_username(username: str) -> User:
    return User(str(uuid.uuid4()), username, "password", True)


def get_user_by_id(user_id: str) -> User:
    return User(user_id, "username", "password", True)


def get_tasks_list(
    offset: int = 0, limit: int = 10, task_ids: list = None
) -> (list[Task], Pagination):
    return [
        Task(1, "title1", "description1", "status1", "group1", "student1"),
        Task(2, "title2", "description2", "status2", "group2", "student2"),
        Task(3, "title3", "description3", "status3", "group3", "student3"),
    ], Pagination(int(offset / limit) + 1, limit, 100, 3)


def get_task(task_id: int) -> dict:
    return {
        "task_id": task_id,
        "title": "title",
        "description": "description",
        "status": "status",
        "group": "group",
        "student": "student",
    }


def get_students_list():
    return [
        {
            "student_id": 1,
            "name": "name1",
            "group": "group1",
            "email": "email1",
        },
        {
            "student_id": 2,
            "name": "name2",
            "group": "group2",
            "email": "email2",
        },
        {
            "student_id": 3,
            "name": "name3",
            "group": "group3",
            "email": "email3",
        },
    ]


def get_student_by_id(student_id: str) -> Student:
    return Student(
        student_id,
        "username1",
        "password1",
        "name1",
        "group1",
        "email1",
        [1, 2, 3, 4, 5],
    )


def get_student_by_username(username: str) -> Student:
    return Student(
        "1", username, "password1", "name1", "group1", "email1", [1, 2, 3, 4, 5]
    )


def add_student(username, password):
    return None


def get_container_config(task_id) -> ContainerConfig:
    return ContainerConfig(
        task_id,
        "briceburg/ping-pong",
        container_name="ping-pong-task_id",
        ports={"80/tcp": None},
    )


global container_id
global container_name
container_id = None
container_name = None


def save_task_container(param: TaskContainer):
    global container_id
    global container_name
    container_id = param.container_id
    container_name = param.container_name
    return None


def get_task_container(task_id, student_id) -> TaskContainer:
    if container_id is None:
        return None
    return TaskContainer(task_id, student_id, container_id, "container_ip", container_name=container_name,
                         image_name="image_name", container_ssh_password="", flag="flag")
