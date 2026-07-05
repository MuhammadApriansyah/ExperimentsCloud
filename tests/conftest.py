import pytest

from app import create_app
from app.extensions import db


@pytest.fixture(scope="session")
def app():

    app = create_app()
    app.config.from_object("app.config.testing.TestingConfig")

    yield app


@pytest.fixture(autouse=True)
def database(app):

    print("\nDatabase URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    with app.app_context():

        db.drop_all()
        db.create_all()

        yield

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
