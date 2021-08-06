from app import create_app
import os

def test_config():
  config_name = os.getenv('FLASK_CONFIG')
  assert not create_app(config_name).testing
  assert create_app({
    "TESTING": True, 
    'SQLALCHEMY_DATABASE_URI': 'sqlite://'
  }).testing
