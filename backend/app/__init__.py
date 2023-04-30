import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from .admin import bp as admin_bp
from .main import bp as main_bp
from werkzeug.middleware.proxy_fix import ProxyFix
import random

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    app.secret_key = random.randbytes(256)
    if os.getenv('APP_ENV') == 'prod':
        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1, x_port=1
        )
    return app