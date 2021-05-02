from datetime import datetime

from myapp import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    _password = db.Column("password", db.Text(), nullable=False)
    is_active = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow())

    def __repr__(self):
        return "<User: {}>".format(self.email)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
