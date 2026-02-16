from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Databases
doctors = {}
patients = {}
appointments = {}

doctor_id_counter = 500
patient_id_counter = 100
appointment_id_counter = 1000

VALID_TOKEN = "securetoken123"


# ---------------- AUTHENTICATION ----------------
def authenticate():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
        return False
    return True


@app.route("/")
def home():
    return "Healthcare API is running"


# ---------------- DOCTOR CREATION ----------------
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    global doctor_id_counter

    data = request.json

    doctor = {
        "doctor_id": doctor_id_counter,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data["experience"]
    }

    doctors[doctor_id_counter] = doctor
    doctor_id_counter += 1

    return jsonify(doctor), 201


# ---------------- PATIENT REGISTRATION ----------------
@app.route("/v1/patients", methods=["POST"])
def register_patient():
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    global patient_id_counter

    data = request.json

    # Validation
    if data.get("age", 0) < 0:
        return jsonify({"error": "Invalid age"}), 400

    if not data.get("email"):
        return jsonify({"error": "Email required"}), 400

    for p in patients.values():
        if p["phone"] == data["phone"]:
            return jsonify({"error": "Duplicate phone"}), 409

    patient = {
        "patient_id": patient_id_counter,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "phone": data["phone"]
    }

    patients[patient_id_counter] = patient
    patient_id_counter += 1

    return jsonify(patient), 201


# ---------------- BOOK APPOINTMENT ----------------
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    global appointment_id_counter

    data = request.json

    # Check slot conflict
    for a in appointments.values():
        if (
            a["doctor_id"] == data["doctor_id"]
            and a["date"] == data["date"]
            and a["time"] == data["time"]
        ):
            return jsonify({"error": "Slot already booked"}), 409

    appointment = {
        "appointment_id": appointment_id_counter,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"],
        "status": "BOOKED"
    }

    appointments[appointment_id_counter] = appointment
    appointment_id_counter += 1

    return jsonify(appointment), 201


# ---------------- VIEW APPOINTMENT ----------------
@app.route("/v1/appointments/<int:appointment_id>", methods=["GET"])
def view_appointment(appointment_id):
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    appointment = appointments.get(appointment_id)

    if not appointment:
        return jsonify({"error": "Not Found"}), 404

    return jsonify(appointment), 200


# ---------------- RESCHEDULE APPOINTMENT ----------------
@app.route("/v1/appointments/<int:appointment_id>", methods=["PUT"])
def reschedule_appointment(appointment_id):
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    appointment = appointments.get(appointment_id)

    if not appointment:
        return jsonify({"error": "Not Found"}), 404

    data = request.json

    # Check slot conflict
    for a in appointments.values():
        if (
            a["doctor_id"] == appointment["doctor_id"]
            and a["date"] == data["date"]
            and a["time"] == data["time"]
            and a["appointment_id"] != appointment_id
        ):
            return jsonify({"error": "Slot already booked"}), 409

    appointment["date"] = data["date"]
    appointment["time"] = data["time"]

    return jsonify(appointment), 200


# ---------------- CANCEL APPOINTMENT ----------------
@app.route("/v1/appointments/<int:appointment_id>", methods=["DELETE"])
def cancel_appointment(appointment_id):
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    appointment = appointments.get(appointment_id)

    if not appointment:
        return jsonify({"error": "Already cancelled"}), 410

    del appointments[appointment_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
