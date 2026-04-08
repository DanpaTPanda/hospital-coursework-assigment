import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, StringVar, OptionMenu

# = Doctor class: basic doctor info + which patients they look after
class Doctor:
    def __init__(self, name, speciality):
        # store doctor's name and speciality
        self.name = name
        self.speciality = speciality
        # list of patient full names assigned to this doctor
        self.patients = []

    def add_patient(self, patient_name):
        # add a patient to this doctor's list
        self.patients.append(patient_name)

    def remove_patient(self, patient_name):
        # remove a patient from this doctor's list if they exist
        if patient_name in self.patients:
            self.patients.remove(patient_name)

    def __str__(self):
        # nice string format used when viewing doctors
        return f"{self.name} ({self.speciality})"


# = Patient class: stores personal details and linked doctor
class Patient:
    def __init__(self, first_name, last_name, age, mobile, address):
        # basic personal information
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile = mobile
        self.address = address
        # will store name of assigned doctor, or None if not assigned
        self.doctor = None

    def full_name(self):
        # convenience method to return "First Last"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # readable summary used in view windows
        return (
            f"{self.full_name()} - {self.age} years old, "
            f"{self.mobile}, {self.address}, Doctor: {self.doctor}"
        )


# = Admin class: simple admin account for login + info
class Admin:
    def __init__(self, username, password, name):
        # login details and admin name
        self.username = username
        self.password = password
        self.name = name
        # address can be updated later
        self.address = ""

    def login(self):
        # simplified login – always returns True in this version
        # (could be replaced with real username/password checks)
        return True


# = Main Tkinter GUI for the hospital system
class HospitalGUI:
    def __init__(self, admin, doctors, patients, discharged):
        # store references to all data lists and admin
        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        self.discharged = discharged

        # require login before showing main window
        if not self.admin.login():
            return

        # main window setup
        self.root = tk.Tk()
        self.root.title("Hospital Management System")

        # main menu buttons – each opens different functionality
        tk.Button(self.root, text="Manage Doctors", width=50,
                  command=self.manage_doctors).pack(pady=5)
        tk.Button(self.root, text="Manage Patients", width=50,
                  command=self.manage_patients).pack(pady=5)
        tk.Button(self.root, text="Assign Doctor", width=50,
                  command=self.assign_doctor).pack(pady=5)
        tk.Button(self.root, text="View Discharged Patients", width=50,
                  command=self.view_discharged).pack(pady=5)
        tk.Button(self.root, text="Update Admin Info", width=50,
                  command=self.update_admin).pack(pady=5)
        tk.Button(self.root, text="Exit", width=50,
                  command=self.root.destroy).pack(pady=5)

        # start Tkinter event loop
        self.root.mainloop()

    # = DOCTOR MANAGEMENT =

    def manage_doctors(self):
        # open a new window just for doctor actions
        window = Toplevel(self.root)
        window.title("Doctor Management")

        tk.Button(window, text="Add Doctor",
                  command=self.add_doctor).pack(pady=5)
        tk.Button(window, text="View Doctors",
                  command=lambda: self.view_list(self.doctors, "Doctors")).pack(pady=5)

    def add_doctor(self):
        # collect doctor details from user
        name = simpledialog.askstring("Add Doctor", "Doctor Name:")
        speciality = simpledialog.askstring("Add Doctor", "Speciality:")

        # basic validation
        if name and speciality:
            self.doctors.append(Doctor(name, speciality))
            messagebox.showinfo("Success", f"Doctor {name} added.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    # = PATIENT MANAGEMENT =

    def manage_patients(self):
        # open a new window just for patient actions
        window = Toplevel(self.root)
        window.title("Patient Management")

        tk.Button(window, text="Add Patient",
                  command=self.add_patient).pack(pady=5)
        tk.Button(window, text="Discharge Patient",
                  command=self.discharge_patient).pack(pady=5)
        tk.Button(window, text="View Patients",
                  command=lambda: self.view_list(self.patients, "Patients")).pack(pady=5)

    def add_patient(self):
        # collect patient details
        first = simpledialog.askstring("Add Patient", "First Name:")
        last = simpledialog.askstring("Add Patient", "Last Name:")
        age = simpledialog.askinteger("Add Patient", "Age:")
        mobile = simpledialog.askstring("Add Patient", "Mobile Number:")
        address = simpledialog.askstring("Add Patient", "Address:")

        # check that all details are present
        if first and last and age and mobile and address:
            self.patients.append(Patient(first, last, age, mobile, address))
            messagebox.showinfo("Success", f"Patient {first} {last} added.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def discharge_patient(self):
        # move a patient from active list to discharged list
        if not self.patients:
            messagebox.showwarning("No Patients", "There are no active patients.")
            return

        # build list of active patient names
        names = [p.full_name() for p in self.patients]

        window = Toplevel(self.root)
        window.title("Discharge Patient")

        tk.Label(window, text="Select Patient to Discharge:").pack(pady=5)

        # dropdown for selecting patient to discharge
        selected_var = StringVar(window)
        selected_var.set(names[0])

        OptionMenu(window, selected_var, *names).pack(pady=5)

        # inner function that actually performs the discharge
        def discharge():
            # find selected patient object
            patient = next(p for p in self.patients
                           if p.full_name() == selected_var.get())
            # remove from active list and add to discharged list
            self.patients.remove(patient)
            self.discharged.append(patient)

            messagebox.showinfo("Discharged",
                                f"{patient.full_name()} has been discharged.")
            window.destroy()

        tk.Button(window, text="Discharge", command=discharge).pack(pady=5)

    # ASSIGNING DOCTORS 
    def assign_doctor(self):
        # link a doctor to a patient using dropdowns
        if not self.patients or not self.doctors:
            messagebox.showwarning("Warning", "You need at least one doctor and one patient.")
            return

        window = Toplevel(self.root)
        window.title("Assign Doctor")

        # select patient
        tk.Label(window, text="Select Patient:").pack(pady=5)
        patient_var = StringVar(window)
        patient_var.set(self.patients[0].full_name())
        OptionMenu(window, patient_var,
                   *[p.full_name() for p in self.patients]).pack(pady=5)

        # select doctor
        tk.Label(window, text="Select Doctor:").pack(pady=5)
        doctor_var = StringVar(window)
        doctor_var.set(self.doctors[0].name)
        OptionMenu(window, doctor_var,
                   *[d.name for d in self.doctors]).pack(pady=5)

        def assign():
            # find chosen patient and doctor objects
            patient = next(p for p in self.patients
                           if p.full_name() == patient_var.get())
            doctor = next(d for d in self.doctors
                          if d.name == doctor_var.get())

            # remove patient from any previous doctor
            for d in self.doctors:
                d.remove_patient(patient.full_name())

            # link patient and doctor
            patient.doctor = doctor.name
            doctor.add_patient(patient.full_name())

            messagebox.showinfo(
                "Assigned",
                f"Doctor {doctor.name} assigned to {patient.full_name()}."
            )
            window.destroy()

        tk.Button(window, text="Assign", command=assign).pack(pady=5)

    # = VIEW HELPERS
    def view_list(self, items, title):
        window = Toplevel(self.root)
        window.title(title)

        text_box = tk.Text(window, width=80)
        text_box.pack()

        for item in items:
            text_box.insert(tk.END, str(item) + "\n")

    def view_discharged(self):
        # show all discharged patients using shared helper
        self.view_list(self.discharged, "Discharged Patients")

    # ADMIN UPDATES, just like the brief asked

    def update_admin(self):
        # allow admin to change their stored name/address
        name = simpledialog.askstring("Update Admin", "New Name:")
        address = simpledialog.askstring("Update Admin", "New Address:")

        if name:
            self.admin.name = name
        if address:
            self.admin.address = address

        messagebox.showinfo("Updated", "Admin information updated.")

# the names for doc and patients is AI-generated
if __name__ == "__main__":
    admin = Admin("mmm", "mmm123", "Hospital")

    # sample doctors list and sample patients list, not perfect but works for now

    doctors = [
        Doctor("John Smith", "Internal Med."),
        Doctor("Jane Doe", "Pediatrics"),
        Doctor("Alex Carter", "Cardiology"),
        Doctor("Emily Davis", "Neurology"),
        Doctor("Robert Wilson", "Orthopedics"),
        Doctor("Linda Thompson", "Dermatology"),
        Doctor("Chris Walker", "General Surgery"),
        Doctor("Olivia Brown", "Radiology"),
        Doctor("Daniel Martinez", "Oncology")
    ]
    patients = [
        Patient("Sara", "Smith", 20, "07123456789", "12 Main St"),
        Patient("Mike", "Jones", 37, "07234567890", "34 Oak Rd"),
        Patient("Liam", "Taylor", 45, "07111222333", "56 Birch Ln"),
        Patient("Emma", "Johnson", 29, "07999888777", "78 Pine St"),
        Patient("Noah", "Williams", 62, "07812223344", "90 Maple Ave"),
        Patient("Ava", "Brown", 33, "07455667788", "21 Willow Crescent"),
        Patient("Ethan", "Davis", 51, "07733445566", "14 Cedar Grove"),
        Patient("Mia", "Miller", 18, "07290909090", "3 Riverbank Rd"),
        Patient("Lucas", "Wilson", 40, "07566778899", "8 Hilltop Drive")
    ]

    # start with no discharged patients
    discharged = []

    HospitalGUI(admin, doctors, patients, discharged)
