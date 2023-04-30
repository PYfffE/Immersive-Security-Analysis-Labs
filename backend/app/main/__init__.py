from flask import Blueprint


bp = Blueprint("main", __name__, url_prefix="/")

from app.main import rest, webui  # noqa: E402
