from datetime import datetime
from project import db
from typing import List


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def get_all(cls) -> List["User"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "User":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_existing_user(cls, username: str, email: str) -> "User":
        return cls.query.filter(
            (cls.username == username) | (cls.email == email)
        ).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
