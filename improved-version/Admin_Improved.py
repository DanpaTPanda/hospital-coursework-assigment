import json
import os
from Doctor_Improved import Doctor
from Patient_Improved import Patient


class HospitalSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.discharged = []

#ADMIN INFO
        self.admin_name = "Michael Omotuyi"
        self.admin_address = "Hospital HQ"

        self.filename = "hospital_data.json"

        self.load_data()

#SAVE 
    def save_data(self):
        data = {
            "doctors": [d.to_dict() for d in self.doctors],
            "patients": [p.to_dict() for p in self.patients],
            "discharged": [p.to_dict() for p in self.discharged],
            "admin": {
                "name": self.admin_name,
                "address": self.admin_address
            }
        }

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

#LOAD 
    def load_data(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            self.doctors = [Doctor.from_dict(d) for d in data.get("doctors", [])]
            self.patients = [Patient.from_dict(p) for p in data.get("patients", [])]
            self.discharged = [Patient.from_dict(p) for p in data.get("discharged", [])]

            admin = data.get("admin", {})
            self.admin_name = admin.get("name", self.admin_name)
            self.admin_address = admin.get("address", self.admin_address)

        except Exception as e:
            print("data load issue:", e)

#UPDATE ADMIN 
    def update_admin(self, name, address):
        self.admin_name = name
        self.admin_address = address
        self.save_data()
        
#FAMALY
    def group_by_family(self):
        families = {}
        for p in self.patients:
            if p.surname not in families:
                families[p.surname] = []
            families[p.surname].append(p.full_name())
        return families

#RELOCATE PATIENT
    def relocate_patient(self, patient_name, doctor_name):

        patient = None
        doctor = None

        for p in self.patients:
            if p.full_name() == patient_name:
                patient = p
                break

        for d in self.doctors:
            if d.name == doctor_name:
                doctor = d
                break

        if not patient or not doctor:
            return False

#REMOVE FROM PAST DOCTOR IF STILL IN SYSTEM
        if patient.doctor:
            for d in self.doctors:
                if d.name == patient.doctor:
                    if patient.full_name() in d.patients:
                        d.patients.remove(patient.full_name())
                    break

        patient.doctor = doctor_name

        if patient.full_name() not in doctor.patients:
            doctor.patients.append(patient.full_name())

        self.save_data()
        return True

#REPORT
    def get_management_report(self):

        report = {
            "total_doctors": len(self.doctors),
            "patients_per_doctor": {},
            "appointments": {},
            "illness": {}
        }

        for d in self.doctors:
            report["patients_per_doctor"][d.name] = len(d.patients)
            report["appointments"][d.name] = {}

            for p in self.patients:
                if p.doctor == d.name:
                    for month, count in p.appointments.items():
                        report["appointments"][d.name][month] = (
                            report["appointments"][d.name].get(month, 0) + count
                        )

        for p in self.patients:
            for s in p.symptoms:
                report["illness"][s] = report["illness"].get(s, 0) + 1

        return report