from flask import Flask
from flask_cors import CORS
from config import Config
from models import db, Service

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"


@app.route("/services")
def get_services():
    services = Service.query.all()
    return [s.serialize() for s in services]


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
