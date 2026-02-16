import requests

BASE_URL = "http://127.0.0.1:5000/v1"
HEADERS = {"Authorization": "Bearer securetoken123"}

doctor_id = None
patient_id = None
appointment_id = None


def test_full_healthcare_workflow():
    global doctor_id, patient_id, appointment_id

    # 1. Create Doctor
    doctor_payload = {
        "name": "Dr. Mehta",
        "specialization": "Cardiologist",
        "experience": 12
    }

    r = requests.post(f"{BASE_URL}/doctors", json=doctor_payload, headers=HEADERS)
    assert r.status_code == 201
    doctor_id = r.json()["doctor_id"]

    # 2. Register Patient
    patient_payload = {
        "name": "Rion",
        "age": 30,
        "email": "rion@test.com",
        "phone": "9999999999"
    }

    r = requests.post(f"{BASE_URL}/patients", json=patient_payload, headers=HEADERS)
    assert r.status_code == 201
    patient_id = r.json()["patient_id"]

    # 3. Book Appointment
    appointment_payload = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": "2026-03-10",
        "time": "10:00"
    }

    r = requests.post(f"{BASE_URL}/appointments", json=appointment_payload, headers=HEADERS)
    assert r.status_code == 201
    appointment_id = r.json()["appointment_id"]

    # 4. View Appointment
    r = requests.get(f"{BASE_URL}/appointments/{appointment_id}", headers=HEADERS)
    assert r.status_code == 200

    # 5. Reschedule Appointment
    reschedule_payload = {
        "date": "2026-03-11",
        "time": "11:00"
    }

    r = requests.put(
        f"{BASE_URL}/appointments/{appointment_id}",
        json=reschedule_payload,
        headers=HEADERS
    )
    assert r.status_code == 200

    # 6. Cancel Appointment
    r = requests.delete(
        f"{BASE_URL}/appointments/{appointment_id}",
        headers=HEADERS
    )
    assert r.status_code == 204
