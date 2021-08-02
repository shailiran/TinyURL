import logging
import pytest
from flask import template_rendered
from app import create_app, db
from app.models import URL


@pytest.fixture
def app():
    """Create application for the tests"""
    _app = create_app()
    _app.logger.setLevel(logging.CRITICAL) #TODO - check
    ctx = _app.test_request_context()
    ctx.push()

    _app.config["TESTING"] = True
    _app.testing = True

    _app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://insta_admin:insta2018@54.75.34.129:3306/test' #TODO - chenge server: 54.75.34.129:8000

    with _app.app_context():
        db.create_all()
        url1 = URL(id=1, original_url='https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/', counter=1)
        db.session.add(url1)
        db.session.commit()

    yield _app
    ctx.pop()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)