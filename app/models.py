from .extensions import db
from .utils import base62_encoder

class URL(db.Model):
    """
    Create URL table
    """

    ___tablename___ = 'urls'

    id = db.Column('id_', db.Integer, primary_key=True)
    original_url = db.Column('original_url', db.String(512))
    short_url = db.Column('short_url', db.String(8), unique=True)

    def __init__(self, original):
        self.original_url = original
        self.short_url = base62_encoder()

    def incrementor():
        info = {"count": 0}
        def number():
            info["count"] += 1
            return info["count"]
        return number
