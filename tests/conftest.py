import pytest
import os
import tempfile

from app import create_app
from app.extensions import db

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
