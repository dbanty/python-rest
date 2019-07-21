from flask import Flask


def init_app(app: Flask):
    """ Register all blueprints to the app """
    from .root import root_blueprint

    app.register_blueprint(root_blueprint)
