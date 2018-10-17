from flask import Flask
from flask import Blueprint
from flask_restful import Api
from flask_script import Manager


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    blueprint = Blueprint('api', __name__)
    api = Api(blueprint)
    app.register_blueprint(blueprint, url_prefix='/api')


if __name__ == "__main__":
    app = create_app()
    manager = Manager(app)
    manager.run()
    app.run()
