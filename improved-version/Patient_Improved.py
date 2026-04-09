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

class Patient:
    def __init__(self, first_name, surname, age, mobile, address, symptoms=None, doctor=None, appointments=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.address = address
        self.symptoms = symptoms if symptoms else []
        self.doctor = doctor
        self.appointments = appointments if appointments else {} # e.g., {"January": 2}

    def full_name(self):
        return f"{self.first_name} {self.surname}"

    def to_dict(self):
        return {
            "first_name": self.first_name, "surname": self.surname, "age": self.age,
            "mobile": self.mobile, "address": self.address, "symptoms": self.symptoms,
            "doctor": self.doctor, "appointments": self.appointments
        }

    @staticmethod
    def from_dict(data):
        return Patient(
            data.get("first_name"), data.get("surname"), data.get("age"),
            data.get("mobile"), data.get("address"), data.get("symptoms", []),
            data.get("doctor"), data.get("appointments", {})
        )
