from app import db


class User(db.Model):
    """User class forms the User database model setup"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """Reformat the print output of the object"""
        return '<User {}>'.format(self.username)
