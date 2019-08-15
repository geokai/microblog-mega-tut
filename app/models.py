from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    """Define the schema of the User database."""
    # __tablename__ = "prime_user" # optional rename of the table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        """Override the print output of the User instance object"""
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """Generate a password hash based on the password provided."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hash of a password for verification."""
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        """Generate a user avatar via 'gravatar.com' using a users email hash."""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    """Define the schema of the Post database."""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """Override the print output of the Post instance object"""
        return '<Post {}>'.format(self.body)
