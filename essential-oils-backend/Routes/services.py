from flask import request, jsonify
from models import Service

@app.route("/services", methods=["GET"])
def get_services():
    services = Service.query.all()
    return jsonify([s.serialize() for s in services])

@app.route("/services", methods=["POST"])
def add_service():
    data = request.get_json()
    new_service = Service(
        title=data["title"],
        description=data.get("description"),
        price=data["price"]
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.serialize()), 201
