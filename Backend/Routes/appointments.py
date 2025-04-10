from flask import Blueprint, request, jsonify
from Models.models import db, Appointment
from datetime import datetime
appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([a.serialize() for a in appointments])

@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment():
  data = request.get_json()
  user_id = data.get('user_id')
  service_id = data.get('service_id')
  appointment_time = data.get('appointment_time')

  try:
        appointment_time = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M:%S')
  except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"}), 400



  from Models.models import User, Service
  user = User.query.get(user_id)
  service = Service.query.get(service_id)
  if not user:
        return jsonify({"error": "User not found"}), 404
  if not service:
        return jsonify({"error": "Service not found"}), 404

  try:
        new_appointment = Appointment(
            user_id=user_id,
            service_id=service_id,
            appointment_time=appointment_time
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment created successfully', 'appointment_id': new_appointment.id}), 201
  except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500