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


from flask import request, jsonify

@app.route("/services", methods=["GET"])
def get_services():
    services = Service.query.all()
    return jsonify([s.serialize() for s in services])

@app.route("/services", methods=["POST"])
def add_service():
    data = request.get_json()
    if not data.get("title") or not data.get("price"):
        return jsonify({"error": "Title and price are required"}), 400

    new_service = Service(
        title=data["title"],
        description=data.get("description"),
        price=data["price"]
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.serialize()), 201


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
