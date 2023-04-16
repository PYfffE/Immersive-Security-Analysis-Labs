from flask import request, session, redirect, url_for

from backend.app import db
from backend.app.admin import bp


# @bp.post('/login')
# def login_post():
#     username = request.form.get('username')
#     password = request.form.get('password')
#
#     user = db.get_user_by_username(username)
#     if user is None:
#         return 'User not found', 404
#     if not user.check_password(password):
#         return 'Invalid password', 401
#
#     session['user_id'] = user.user_id
#
#     return redirect(url_for('admin.index'))

