from flask import (
    render_template
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from backend.app.admin import bp
from backend.app.admin.auth import login_required


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(1, 20)], render_kw={'placeholder': 'Логин'})
    password = PasswordField('Пароль', validators=[DataRequired(), Length(8, 150)], render_kw={'placeholder': 'Пароль'})
    submit = SubmitField(label='Войти')

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('admin/index.html')

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('admin/login.html', form=form)

@bp.route('/tasks')
@login_required
def tasks():
    return

@bp.route('/students')
@login_required
def students():
    return

@bp.route('/top')
@login_required
def top():
    return