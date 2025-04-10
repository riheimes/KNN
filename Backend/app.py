from flask import Flask
from flask_cors import CORS
from config import Config
from Models.models import db, User, Service, Appointment
from Routes.services import services_bp
from Routes.appointments import appointments_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)


app.register_blueprint(services_bp, url_prefix="/services")
app.register_blueprint(appointments_bp, url_prefix="/appointments")


@app.route("/")
def home():
    return "Backend is running!"


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

