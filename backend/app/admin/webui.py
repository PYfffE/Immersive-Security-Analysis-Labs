from flask import (
    render_template, request, redirect, url_for
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from .. import db
from . import bp
from .auth import login_required


LIST_LIMIT=10
class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(1, 20)], render_kw={'placeholder': 'Логин'})
    password = PasswordField('Пароль', validators=[DataRequired(), Length(8, 150)], render_kw={'placeholder': 'Пароль'})
    submit = SubmitField(label='Войти')

class AddStudentForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(1, 20)], render_kw={'placeholder': 'Логин студента'})
    password = PasswordField('Пароль', validators=[DataRequired(), Length(8, 150)], render_kw={'placeholder': 'Пароль студента'})
    submit = SubmitField(label='Добавить студента')

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('admin/login.html', form=form)
@bp.route('/')
@bp.route('/index')
@bp.route('/tasks')
@login_required
def tasks():
    page: int = int(request.args["page"]) if "page" in request.args else 1
    tasks_list, pagination = db.get_tasks_list((page - 1) * LIST_LIMIT, LIST_LIMIT)
    return render_template('admin/tasks.html', list=tasks_list, pagination=pagination)

@bp.route('/students')
@login_required
def students():
    return render_template('admin/students.html', list=db.get_students_list())

@bp.route('/top')
@login_required
def top():
    return

@bp.route('/task/<int:id>')
@bp.route('/task/<int:id>/details')
@login_required
def task_by_id(id: int):
    task = db.get_task(id)
    return render_template('admin/task_details.html', task=task)

@bp.route('/task/<int:id>/control')
@login_required
def task_control(id: int):
    task = db.get_task(id)
    return render_template('admin/task_control.html', task=task)

@bp.route('/task/<int:id>/students')
@login_required
def task_students(id: int):
    task = db.get_task(id)
    return render_template('admin/task_students.html', task=task)

@bp.route('/student/add')
@login_required
def add_student():
    return render_template('admin/add_student.html', form=AddStudentForm())
@bp.route('/student/<int:id>/edit')
@login_required
def edit_student(id):
    return render_template('admin/edit_student.html')