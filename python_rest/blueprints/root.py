from flask import Blueprint

root_blueprint = Blueprint("root", __name__)


@root_blueprint.route("/health/")
def health():
    """ A simple check to see if the application is running """
    return {"message": "Healthy"}
