import tkinter as tk
from tkinter import simpledialog, messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt

# Patient class – stores personal details and appointment history
class Patient:

    # Initialise patient details
    def __init__(self, first_name, surname, age, mobile, address, symptoms=None, doctor=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.address = address
        self.symptoms = symptoms if symptoms else []
        self.doctor = doctor
        self.appointments = {}

    # Returns patient's full name
    def full_name(self):
        return f"{self.first_name} {self.surname}"

    # Nicely formatted string used when viewing patients
    def __str__(self):
        symptoms = ", ".join(self.symptoms) if self.symptoms else "None"
        doctor = self.doctor if self.doctor else "None"
        appointments = (
            ", ".join(f"{m}: {c}" for m, c in self.appointments.items())
            if self.appointments else "None"
        )

        return (
            f"{self.full_name():<20} | Age: {self.age} | Mobile: {self.mobile} | "
            f"Address: {self.address} | Symptoms: {symptoms} | "
            f"Doctor: {doctor} | Appointments: {appointments}"
        )

    # Increase appointment count for a given month
    def add_appointment(self, month):
        self.appointments[month] = self.appointments.get(month, 0) + 1

    # Convert patient object to dictionary for saving
    def to_dict(self):
        return self.__dict__

    # Create Patient object from dictionary data
    @staticmethod
    def from_dict(data):
        patient = Patient(
            data["first_name"],
            data["surname"],
            data["age"],
            data["mobile"],
            data["address"],
            data.get("symptoms", []),
            data.get("doctor")
        )
        patient.appointments = data.get("appointments", {})
        return patient


# Doctor class – stores doctor info and assigned patients
class Doctor:

    def __init__(self, name, speciality, mobile):
        self.name = name
        self.speciality = speciality
        self.mobile = mobile
        self.patients = []

    # Add patient name to doctor's list
    def add_patient(self, patient_name):
        if patient_name not in self.patients:
            self.patients.append(patient_name)

    # Remove patient name from doctor's list
    def remove_patient(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)

    # Formatted string used when viewing doctors
    def __str__(self):
        return (
            f"{self.name:<20} | Speciality: {self.speciality} | "
            f"Mobile: {self.mobile} | Patients: {len(self.patients)}"
        )

    # Convert doctor object to dictionary
    def to_dict(self):
        return self.__dict__

    # Create Doctor object from dictionary data
    @staticmethod
    def from_dict(data):
        doctor = Doctor(data["name"], data["speciality"], data["mobile"])
        doctor.patients = data.get("patients", [])
        return doctor


# Admin class – handles login and profile info
class Admin:

    def __init__(self, username="mmm", password="mmm123", name="Admin", address="Hospital"):
        self.username = username
        self.password = password
        self.name = name
        self.address = address

    # Login with maximum 3 attempts
    def login(self):
        for attempt in range(3):
            username = simpledialog.askstring("Login", "Enter username:")
            password = simpledialog.askstring("Login", "Enter password:", show="*")

            if username == self.username and password == self.password:
                messagebox.showinfo("Login", "Login successful.")
                return True

            messagebox.showwarning("Login Failed", f"Attempt {attempt + 1} of 3")

        messagebox.showerror("Access Denied", "Too many failed login attempts.")
        return False

    # Update admin name and address
    def update_profile(self, name, address):
        if name:
            self.name = name
        if address:
            self.address = address


# Core hospital system logic
class HospitalSystem:

    def __init__(self):
        self.doctors = []
        self.patients = []
        self.discharged = []
        self.admin = Admin()
        self.load()

    # Add doctor to system
    def add_doctor(self, name, speciality, mobile):
        self.doctors.append(Doctor(name, speciality, mobile))
        self.save()

    # Add patient to system
    def add_patient(self, first, surname, age, mobile, address, symptoms):
        self.patients.append(Patient(first, surname, age, mobile, address, symptoms))
        self.save()

    # Assign doctor to patient
    def assign_doctor(self, patient_name, doctor_name):
        patient = next((p for p in self.patients if p.full_name() == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)

        if patient and doctor:
            for d in self.doctors:
                d.remove_patient(patient_name)

            patient.doctor = doctor_name
            doctor.add_patient(patient_name)
            self.save()
            return True
        return False

    # Discharge patient from active list
    def discharge_patient(self, full_name):
        for patient in self.patients:
            if patient.full_name() == full_name:
                self.discharged.append(patient)
                self.patients.remove(patient)
                self.save()
                return True
        return False

    # Save all data to JSON
    def save(self):
        data = {
            "doctors": [d.to_dict() for d in self.doctors],
            "patients": [p.to_dict() for p in self.patients],
            "discharged": [p.to_dict() for p in self.discharged],
            "admin": self.admin.__dict__
        }
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    # Load data from JSON if file exists
    def load(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            self.doctors = [Doctor.from_dict(d) for d in data.get("doctors", [])]
            self.patients = [Patient.from_dict(p) for p in data.get("patients", [])]
            self.discharged = [Patient.from_dict(p) for p in data.get("discharged", [])]

        except FileNotFoundError:
            pass


# GUI class – handles all Tkinter windows
class HospitalGUI:

    def __init__(self, system):
        self.sys = system

        # Require admin login before opening GUI
        if not self.sys.admin.login():
            return

        self.root = tk.Tk()
        self.root.title("Hospital Management System")

        buttons = [
            ("Add Doctor", self.add_doctor),
            ("View Doctors", self.view_doctors),
            ("Add Patient", self.add_patient),
            ("View Patients", self.view_patients),
            ("Assign Doctor", self.assign_doctor),
            ("Discharge Patient", self.discharge_patient),
            ("Add Appointment", self.add_appointment),
            ("Update Admin Info", self.update_admin),
            ("Exit", self.root.destroy)
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).pack(fill="x", pady=4)

        self.root.mainloop()

    # Display list of items in a new window
    def view_list(self, data, title):
        win = tk.Toplevel(self.root)
        win.title(title)
        text = tk.Text(win, width=300)
        text.pack()

        if not data:
            text.insert(tk.END, "No records found.")
            return

        for item in data:
            text.insert(tk.END, str(item) + "\n")

    def view_doctors(self):
        self.view_list(self.sys.doctors, "Doctors")

    def view_patients(self):
        self.view_list(self.sys.patients, "Patients")

    def add_doctor(self):
        name = simpledialog.askstring("Doctor", "Name:")
        speciality = simpledialog.askstring("Doctor", "Speciality:")
        mobile = simpledialog.askstring("Doctor", "Mobile:")

        if not (name and speciality and mobile):
            messagebox.showerror("Error", "All fields are required.")
            return

        self.sys.add_doctor(name, speciality, mobile)
        messagebox.showinfo("Success", "Doctor added.")

    def add_patient(self):
        try:
            age = int(simpledialog.askstring("Patient", "Age:"))
        except:
            messagebox.showerror("Error", "Age must be a number.")
            return

        first = simpledialog.askstring("Patient", "First name:")
        surname = simpledialog.askstring("Patient", "Surname:")
        mobile = simpledialog.askstring("Patient", "Mobile:")
        address = simpledialog.askstring("Patient", "Address:")
        symptoms = simpledialog.askstring("Patient", "Symptoms:")

        symptoms = [s.strip() for s in symptoms.split(",")] if symptoms else []

        self.sys.add_patient(first, surname, age, mobile, address, symptoms)
        messagebox.showinfo("Success", "Patient added.")

    def assign_doctor(self):
        patient = simpledialog.askstring("Assign", "Patient full name:")
        doctor = simpledialog.askstring("Assign", "Doctor name:")

        if self.sys.assign_doctor(patient, doctor):
            messagebox.showinfo("Done", "Doctor assigned.")
        else:
            messagebox.showerror("Error", "Assignment failed.")

    def discharge_patient(self):
        name = simpledialog.askstring("Discharge", "Patient full name:")
        if self.sys.discharge_patient(name):
            messagebox.showinfo("Done", "Patient discharged.")
        else:
            messagebox.showerror("Error", "Patient not found.")

    def add_appointment(self):
        name = simpledialog.askstring("Appointment", "Patient full name:")
        patient = next((p for p in self.sys.patients if p.full_name() == name), None)

        if not patient:
            messagebox.showerror("Error", "Patient not found.")
            return

        date_str = simpledialog.askstring("Appointment", "Date (DD/MM/YYYY):")
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            patient.add_appointment(date.strftime("%B"))
            self.sys.save()
            messagebox.showinfo("Success", "Appointment added.")
        except:
            messagebox.showerror("Error", "Invalid date format.")

    def update_admin(self):
        name = simpledialog.askstring("Admin", "New name:")
        address = simpledialog.askstring("Admin", "New address:")
        self.sys.admin.update_profile(name, address)
        self.sys.save()
        messagebox.showinfo("Updated", "Admin details updated.")

# Run the program
if __name__ == "__main__":
    system = HospitalSystem()
    HospitalGUI(system)
