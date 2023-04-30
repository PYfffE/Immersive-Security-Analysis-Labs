import uuid

from .models.pagination import Pagination
from .models.user import User


def get_user_by_username(username: str) -> User:
    return User(str(uuid.uuid4()), username, 'password')


def get_user_by_id(user_id: str) -> User:
    return User(user_id, "username", 'password')

def get_tasks_list(offset: int=0, limit: int=10) -> (list, Pagination):
    return [
        {
            'task_id': 1,
            'title': 'title1',
            'description': 'description1',
            'status': 'status1',
            'group': 'group1',
            'student': 'student1',
        },
        {
            'task_id': 2,
            'title': 'title2',
            'description': 'description2',
            'status': 'status2',
            'group': 'group2',
            'student': 'student2',
        },
        {
            'task_id': 3,
            'title': 'title3',
            'description': 'description3',
            'status': 'status3',
            'group': 'group3',
            'student': 'student3',
        },
    ], Pagination(int(offset / limit) + 1, limit, 100, 3)

def get_task(task_id: int) -> dict:
    return {
        'task_id': task_id,
        'title': 'title',
        'description': 'description',
        'status': 'status',
        'group': 'group',
        'student': 'student',
    }


def get_students_list():
    return [
        {
            'student_id': 1,
            'name': 'name1',
            'group': 'group1',
            'email': 'email1',
        },
        {
            'student_id': 2,
            'name': 'name2',
            'group': 'group2',
            'email': 'email2',
        },
        {
            'student_id': 3,
            'name': 'name3',
            'group': 'group3',
            'email': 'email3',
        }
    ]


def add_student(username, password):
    return None