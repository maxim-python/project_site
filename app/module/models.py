#from flask_sqlalchemy import SQLAlchemy

from app import db

#db = SQLAlchemy()

class Metal_schingle(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), index=True, nullable=True)
        size_metal = db.Column(db.String, nullable=True)
        price = db.Column(db.Integer, nullable=True)
        description = db.Column(db.Text, nullable=True)
        unique_number = db.Column(db.Integer, nullable=True)

        def __repr__(self):
            return '<Metal_schingle {}>'.format(self.name) 