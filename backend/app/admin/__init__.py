"""
Admin UI/REST API
"""
from flask import Blueprint

bp = Blueprint("admin", __name__, url_prefix="/admin/")

from app.admin import rest, webui  # noqa: E402
