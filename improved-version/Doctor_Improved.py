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

class Doctor:
    def __init__(self, name, speciality, mobile, patients=None):
        self.name = name
        self.speciality = speciality
        self.mobile = mobile
        # Stores names of patients assigned to this doctor
        self.patients = patients if patients else []

    def to_dict(self):
        """Converts object to dictionary for JSON saving."""
        return {
            "name": self.name,
            "speciality": self.speciality,
            "mobile": self.mobile,
            "patients": self.patients
        }

    @staticmethod
    def from_dict(data):
        """Creates object from dictionary."""
        return Doctor(
            data.get("name"),
            data.get("speciality"),
            data.get("mobile"),
            data.get("patients", [])
        )
