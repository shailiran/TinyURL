import pytest
import os
import tempfile
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.extensions import db
from app.models import URL

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': db_path
    })
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.commit()
        yield client
        db.session.remove()
        db.drop_all()
            
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def mock_url_1():
    return URL(original='original_1', counter=1)

@pytest.fixture
def mock_url_2():
    return URL(original='original_2', counter=2)
 
# @pytest.fixture
# def mock_get_sqlalchemy(mocker):
#     mock = mocker.patch('flask_sqlalchemy._QueryProperty.__get__').return_value = mocker.Mock()
#     return mock

# @pytest.fixture
# def mock_encoder(mocker):
#     return mocker.patch("app.utils.base62_encoder")
