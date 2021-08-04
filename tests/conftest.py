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
        # 'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.commit()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def mock_url():
    return URL(original='original', counter=1)

# @pytest.fixture
# def mock_get_sqlalchemy(mocker):
#     mock = mocker.patch('flask_sqlalchemy._QueryProperty.__get__').return_value = mocker.Mock()
#     return mock

# @pytest.fixture
# def mock_encoder(mocker):
#     return mocker.patch("app.utils.base62_encoder")
