from schedulemanager import db


class Service(db.Model):
    # schema for the service type model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(30), unique=True, nullabale=False)
    vehicles = db.relationship("Vehicle", backref="service", cascade="all, delete", lazy=True)  # noqa

    def __repr__(self):
        return self.service_name


class Vehicle(db.Model):
    # schema for the Vehicle model
    id = db.Column(db.Integer, primary_key=True)
    vehicle_reg = db.Column(db.String(8), unique=True, nullable=False)
    vehicle_description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    service_completed = db.Column(db.Boolean, default=False, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id", ondelete="CASCADE"), nullable=False)  # noqa

    def __repr__(self):
        return "#{0} - Vehicle: {1} | Urgent: {2}".format(
            self.vehicle_reg, self.vehicle_description, self.due_date
        )
