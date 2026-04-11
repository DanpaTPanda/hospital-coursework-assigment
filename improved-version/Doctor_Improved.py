#STARTED BASIC
class Doctor:
    def __init__(self, name, speciality, mobile, patients=None):
        self.name = name
        self.speciality = speciality
        self.mobile = mobile

#KEEPINNG THE CODE SIMPLE
        if patients is None:
            self.patients = []
        else:
            self.patients = patients
            
#SAVING DATA INTO JSON
    def to_dict(self):
        return {
            "name": self.name,
            "speciality": self.speciality,
            "mobile": self.mobile,
            "patients": self.patients
        }

#REBUILD DOCTOR OBJECT FROM SAVED FILE
    @staticmethod
    def from_dict(data):
        return Doctor(
            data.get("name"),
            data.get("speciality"),
            data.get("mobile"),
            data.get("patients", [])
        )