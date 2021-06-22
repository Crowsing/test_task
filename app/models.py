from datetime import datetime

from app import db


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.NUMERIC)
    currency = db.Column(db.String(3))
    description = db.Column(db.TEXT)
    sending_time = db.Column(db.DATETIME, default=datetime.now)

    def __repr__(self):
        return '<User {}>'.format(self.id)
