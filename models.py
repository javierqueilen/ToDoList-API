from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask import json

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    tasks = db.Column(db.String(1000), nullable=False)
    #email = db.Column(db.String(100), nullable=False, unique=True)

    def serialize(self):
        return json.loads(self.tasks)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()