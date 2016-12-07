from central_server import db
from utils import logger

class Doctor(db.Model):
    __tablename__ = 'Doctor'

    id = db.Column(db.Integer, primary_key=True)
    speciality = db.Column(db.String(50))

    def __init__(self, speciality):
        self.speciality = speciality

    def __repr__(self):
        """Return representation of doctor object"""
        return "<Doctor {}>".format(self)

    def to_dict(self):
        """Convert doctor object into dictionary"""
        return dict([
            ("speciality", self.speciality),
        ])

    def save(self):
        """Saves object into database"""
        try:
            db.session.add(self)
            db.session.commit()
            logger.debug("Saved {}.".format(repr(self)))
        except Exception, e:
            logger.error("Error on saving {} (ROLLBACK): {}".format(
                self.__class__.__name__, e))
            db.session.remove()

