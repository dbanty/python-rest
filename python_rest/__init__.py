from flask import Flask


def create_app() -> Flask:
    """
    Creates an application instance to run
    :return: A Flask object
    """
    app = Flask(__name__)

    from . import blueprints

    blueprints.init_app(app)

    return app
