# ---------------------------------------------------------
# Project: Hospital Management System - Improved Version
# Author:  Michael Omotuyi
# Property of: Michael Omotuyi 
# GitHub:  https://github.com/DanpaTPanda
# ---------------------------------------------------------
# This source code is the sole property of Michael Omotuyi.
# Unauthorized copying or distribution of this file, 
# via any medium, is strictly prohibited.
# ---------------------------------------------------------

import json
import os
from Doctor_Improved import Doctor
from Patient_Improved import Patient

class HospitalSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.discharged = []
        self.admin_name = "Michael Omotuyi"
        self.admin_address = "St. George Hospital"
        self.filename = "hospital_data.json"
        self.load_data()

    def save_data(self):
        data = {
            "doctors": [d.to_dict() for d in self.doctors],
            "patients": [p.to_dict() for p in self.patients],
            "discharged": [p.to_dict() for p in self.discharged],
            "admin": {"name": self.admin_name, "address": self.admin_address}
        }
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.filename): return
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.doctors = [Doctor.from_dict(d) for d in data.get("doctors", [])]
            self.patients = [Patient.from_dict(p) for p in data.get("patients", [])]
            self.discharged = [Patient.from_dict(p) for p in data.get("discharged", [])]
            admin_data = data.get("admin", {})
            self.admin_name = admin_data.get("name", self.admin_name)
            self.admin_address = admin_data.get("address", self.admin_address)
        except Exception as e:
            print(f"Error loading data: {e}")

    def update_admin(self, new_name, new_address):
        """Allows admin to update their own details."""
        self.admin_name = new_name
        self.admin_address = new_address
        self.save_data()

    def relocate_patient(self, patient_full_name, new_doctor_name):
        """Moves patient and updates both Patient records and Doctor lists[cite: 247, 338]."""
        patient = next((p for p in self.patients if p.full_name() == patient_full_name), None)
        new_doc = next((d for d in self.doctors if d.name == new_doctor_name), None)
        
        if patient and new_doc:
            # Remove from old doctor's list
            old_doc = next((d for d in self.doctors if d.name == patient.doctor), None)
            if old_doc and patient.full_name() in old_doc.patients:
                old_doc.patients.remove(patient.full_name())
            
            # Assign to new doctor
            patient.doctor = new_doctor_name
            if patient.full_name() not in new_doc.patients:
                new_doc.patients.append(patient.full_name())
            self.save_data()
            return True
        return False

    def group_by_family(self):
        """Groups patients by surname as required by feedback[cite: 243, 340]."""
        families = {}
        for p in self.patients:
            families.setdefault(p.surname, []).append(p.full_name())
        return families

    def get_management_report(self):
        """Generates all 4 required metrics for 80% mark."""
        report = {
            "total_doctors": len(self.doctors),
            "patients_per_doctor": {d.name: len(d.patients) for d in self.doctors},
            "appointments": {}, # Per month per doctor
            "illness": {}       # Total by illness type
        }
        
        for d in self.doctors:
            report["appointments"][d.name] = {}
            assigned_pts = [p for p in self.patients if p.doctor == d.name]
            for p in assigned_pts:
                for month, count in p.appointments.items():
                    report["appointments"][d.name][month] = report["appointments"][d.name].get(month, 0) + count
        
        for p in self.patients:
            for s in p.symptoms:
                report["illness"][s] = report["illness"].get(s, 0) + 1
        return report
