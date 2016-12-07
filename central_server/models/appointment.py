from central_server import db
from utils import logger

class Appointment(db.Model):
    __tablename__ = 'Appointment'

    pacient_id = db.Column(
        db.ForeignKey("central_server.models.pacient.Pacient"),
        primary_key=True)
    doctor_id = db.Column(
        db.ForeignKey("central_server.models.doctor.Doctor"),
        primary_key=True)
    date = db.Column(db.Date(), primary_key=True)
    time = db.Column(db.String(7))
    office = db.Column(db.String(50))

    def __init__(self, pacient_id, doctor_id, date, time, office):
        self.pacient_id = pacient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.office = office

    def __repr__(self):
        """Return representation of appointment object"""
        return "<Appointment {}>".format(self)

    def to_dict(self):
        """Convert appointment object into dictionary"""
        return dict([
            ("pacient_id", self.pacient_id),
            ("doctor_id", self.doctor_id),
            ("date", self.date),
            ("time", self.time),
            ("office", self.office),
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

