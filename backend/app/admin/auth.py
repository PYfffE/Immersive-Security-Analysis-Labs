import functools

from flask import session, redirect, url_for, g, request

from app import db
from app.admin import bp


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("admin.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = db.get_user_by_id(user_id)


@bp.post("/login")
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    user = db.get_user_by_username(username)
    if user is None:
        return "User not found", 404
    if not user.check_password(password):
        return "Invalid password", 401

    session["user_id"] = user.user_id

    return redirect(url_for("admin.tasks"))
