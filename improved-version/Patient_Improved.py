#UPDATED THIS AFTER TESTING DATA SAVING
class Patient:
    def __init__(self, first_name, surname, age, mobile, address, symptoms=None, doctor=None, appointments=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.address = address

#PREVENTS EVERY PATIENT FROM SHARING THE SAME SYMPTOMS LIST BY MISTAKE
        self.symptoms = symptoms if symptoms else []
        self.doctor = doctor
        self.appointments = appointments if appointments else {}

    def full_name(self):
        return f"{self.first_name} {self.surname}"
    
    def __str__(self):
        return f"[Patient] {self.full_name()} - Mob: {self.mobile}"

#CONVERT PATIENT INTO DICTIONARY FOR JSON SAVING
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "surname": self.surname,
            "age": self.age,
            "mobile": self.mobile,
            "address": self.address,
            "symptoms": self.symptoms,
            "doctor": self.doctor,
            "appointments": self.appointments
        }
    
#REBUILD PATIENT FROM STORED FILE
    @staticmethod
    def from_dict(data):
        return Patient(
            data.get("first_name"),
            data.get("surname"),
            data.get("age"),
            data.get("mobile"),
            data.get("address"),
            data.get("symptoms", []),
            data.get("doctor"),
            data.get("appointments", {})
        )