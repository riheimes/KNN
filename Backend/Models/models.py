from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price
        }
    
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Added ForeignKey
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)  # Added ForeignKey
    appointment_time = db.Column(db.DateTime, nullable=False)


    user = db.relationship('User', backref='appointments', lazy=True)
    service = db.relationship('Service', backref='appointments', lazy=True)


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "service_id": self.service_id,
            "appointment_time": self.appointment_time.strftime('%Y-%m-%d %H:%M:%S')
        }

