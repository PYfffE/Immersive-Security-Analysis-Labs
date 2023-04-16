from flask import Flask
from flask_bootstrap import Bootstrap5
from backend.app.admin import bp as admin_bp
from backend.app.main import bp as main_bp
import random

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    app.secret_key = random.randbytes(256)
    return app