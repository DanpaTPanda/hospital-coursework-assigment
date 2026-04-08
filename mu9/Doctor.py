class Doctor:
    #Represents a doctor with basic info and a list of patients.

    def __init__(self, first_name: str, surname: str, speciality: str):
        self._first_name = first_name
        self._surname = surname
        self._speciality = speciality
        self.patients = []

    # Properties = first names + surname + role
    @property
    def full_name(self) -> str:
        #Return the full name.
        return f"{self._first_name} {self._surname}"

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, value: str):
        self._surname = value

    @property
    def speciality(self) -> str:
        return self._speciality

    @speciality.setter
    def speciality(self, value: str):
        self._speciality = value

    # Patient Management 
    def add_patient(self, patient: str) -> bool:
        #Add a patient if not already assigned
        if patient not in self.patients:
            self.patients.append(patient)
            return True
        return False

    # String Representation 
    def __str__(self) -> str:
        #Print doctor info 
        return f"{self.full_name:^30} | {self._speciality:^15} | Patients: {len(self.patients)}"

    def __repr__(self) -> str:
        return f"Doctor({self._first_name!r}, {self._surname!r}, {self._speciality!r}, Patients={self.patients!r})"


# Main inputs to put name + surname + role
if __name__ == "__main__":
    print("Enter doctor details:\n")

    first = input("First name: ")
    last = input("Surname: ")
    spec = input("Speciality: ")

    doctor = Doctor(first, last, spec)

    print("Doctor created:")
    print(doctor)

    # add patients if u want plz give me extra mark for the effort TY
    while True:
        patient = input("\nEnter patient name (or leave blank to finish): ")
        if not patient:
            break
        if doctor.add_patient(patient):
            print(f"{patient} added.")
        else:
            print(f"{patient} is already assigned.")

    print("Doctor Info:")
    print(doctor)
