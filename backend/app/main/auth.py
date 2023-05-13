import functools
import os

from flask import session, redirect, url_for, g, request

from app import db
from app.main import bp


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.student is None:
            return redirect(url_for("main.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    student_id = session.get("student_id")

    if student_id is None and os.getenv("FLASK_DISABLE_AUTH"):
        student_id = "1"

    if student_id is None:
        g.student = None
    else:
        g.student = db.get_student_by_id(student_id)


@bp.post("/login")
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    student = db.get_student_by_username(username)
    if student is None:
        return "User not found", 404
    if not student.password == password:
        return "Invalid password", 401

    session["student_id"] = student.student_id

    return redirect(url_for("admin.tasks"))
