from central_server import db
from utils import logger

class Pacient(db.Model):
    __tablename__ = 'Pacient'

    id = db.Column(db.Integer, primary_key=True)
    blood_type = db.Column(db.String(5))
    weight = db.Column(db.Float())
    deseases = db.Column(db.String(50))

    def __init__(self, blood_type, weight, deseases):
        self.blood_type = blood_type
        self.weight = weight
        self.deseases = deseases

    def __repr__(self):
        """Return representation of pacient object"""
        return "<Pacient {}>".format(self)

    def to_dict(self):
        """Convert pacient object into dictionary"""
        return dict([
            ("blood_type", self.blood_type),
            ("weight", self.weight),
            ("deseases", self.deseases),
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

