from flask import Blueprint, request, jsonify

bp = Blueprint('appointments', __name__)
from . import db
from models import Appointment
from datetime import datetime

@bp.route('/appointments', methods=['POST'])
def create_appointment():
  data = request.get_json()
  user_id = data.get('user_id')
  service_id = data.get('service_id')
  appointment_time = data.get('appointment_time')

  try:
    appointment_time = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M:%S')
  except ValueError:
    return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"}), 400
  
  new_appointment = Appointment(
    user_id=user_id,
    service_id=service_id,
    appointment_time=appointment_time
  )
  db.session.add(new_appointment)
  db.session.commit()
  return jsonify({'message': 'Appointment created successfully', 'appointment_id': new_appointment.id}), 201