import pytest

from app import create_app
from app.extensions import db

@pytest.fixture
def client():
    config = {
        'TESTING': True, 
        'SQLALCHEMY_DATABASE_URI': 'sqlite://'
    }
    app = create_app(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        db.init_app(app)

        with app.app_context():
            db.create_all()
            db.session.commit()

        yield client

        db.session.remove()
        db.drop_all()
