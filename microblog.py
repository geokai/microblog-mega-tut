from app import app, db     # noqa
from app.models import User, Post   # noqa


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
