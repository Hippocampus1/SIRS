from central_server import db
from utils import logger

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    birth_date = db.Column(db.Date())

    def __init__(self, username, password, email, first_name=None,
                 last_name=None, birth_date=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __repr__(self):
        """Return representation of user object"""
        return "<User {}>".format(self.username)

    def to_dict(self):
        """Convert user object into dictionary"""
        return dict([
            ("username", self.username),
            ("email", self.email),
            ("first_name", self.first_name),
            ("last_name", self.last_name),
            ("birth_date", self.birth_date)
        ])

    def save(self):
        """Saves object into database"""
        db.session.add(self)
        db.session.commit()
        logger.debug("Saved {}.".format(repr(self)))
