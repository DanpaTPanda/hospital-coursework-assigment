import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Doctor class – stores basic doctor details
class Doctor:
    def __init__(self, first_name, surname, speciality):
        self.first_name = first_name
        self.surname = surname
        self.speciality = speciality

    def full_name(self):
        return f"{self.first_name} {self.surname}"

    def __str__(self):
        return f"{self.full_name():<20} | Speciality: {self.speciality}"


# Patient class – stores full patient details
class Patient:
    def __init__(self, first_name, surname, age, mobile, address, symptoms=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.address = address
        self.symptoms = symptoms if symptoms else []
        self.doctor = None

    def full_name(self):
        return f"{self.first_name} {self.surname}"

    def __str__(self):
        symptoms = ", ".join(self.symptoms)
        doctor = self.doctor if self.doctor else "None"
        return (
            f"{self.full_name():<20} | Age: {self.age} | Mobile: {self.mobile} | "
            f"Address: {self.address} | Symptoms: {symptoms} | Doctor: {doctor}"
        )

    def to_dict(self):
        # Convert patient to dictionary for saving
        return {
            "first_name": self.first_name,
            "surname": self.surname,
            "age": self.age,
            "mobile": self.mobile,
            "address": self.address,
            "symptoms": self.symptoms,
            "doctor": self.doctor
        }

    @staticmethod
    def from_dict(data):
        # Rebuild patient object from saved data
        p = Patient(
            data["first_name"],
            data["surname"],
            data["age"],
            data["mobile"],
            data["address"],
            data["symptoms"]
        )
        p.doctor = data.get("doctor")
        return p


# Admin class – handles login and admin info
class Admin:
    def __init__(self, username="mmm", password="mmm123", name="Admin", address="Hospital"):
        self.__username = username
        self.__password = password
        self.name = name
        self.address = address

    def login(self):
        # Allow up to 3 login attempts
        attempts = 0
        while attempts < 3:
            username = simpledialog.askstring("Login", "Enter Username:")
            password = simpledialog.askstring("Login", "Enter Password:", show="*")

            if username == self.__username and password == self.__password:
                messagebox.showinfo("Success", "Login Successful.")
                return True

            attempts += 1
            messagebox.showerror("Login Failed", f"Incorrect login ({attempts}/3)")

        raise Exception("Too many failed login attempts.")


# Save hospital data to hospital_data.json
def save_data(doctors, patients, discharged, filename="hospital_data.json"):
    data = {
        "doctors": [vars(d) for d in doctors],
        "patients": [p.to_dict() for p in patients],
        "discharged": [p.to_dict() for p in discharged]
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Load hospital data from hospital_data.json
def load_data(filename="hospital_data.json"):
    doctors, patients, discharged = [], [], []
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        for d in data.get("doctors", []):
            doctors.append(Doctor(d["first_name"], d["surname"], d["speciality"]))

        for p in data.get("patients", []):
            patients.append(Patient.from_dict(p))

        for p in data.get("discharged", []):
            discharged.append(Patient.from_dict(p))

    except FileNotFoundError:
        # Start empty if no file exists yet
        pass

    return doctors, patients, discharged

# Main GUI class
class HospitalGUI:
    def __init__(self, admin, doctors, patients, discharged):
        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        self.discharged = discharged

        self.root = tk.Tk()
        self.root.title("Hospital Management System")

        tk.Button(self.root, text="Doctor Management", width=60,
                  command=self.manage_doctors).pack(pady=10)
        tk.Button(self.root, text="Patient Management", width=60,
                  command=self.manage_patients).pack(pady=10)
        tk.Button(self.root, text="Assign Doctor", width=60,
                  command=self.assign_doctor).pack(pady=10)
        tk.Button(self.root, text="Discharge Patient", width=60,
                  command=self.discharge_patient).pack(pady=10)
        tk.Button(self.root, text="View Discharged", width=60,
                  command=self.view_discharged).pack(pady=10)
        tk.Button(self.root, text="Update Admin Info", width=60,
                  command=self.update_admin).pack(pady=10)
        tk.Button(self.root, text="Save & Exit", width=60,
                  command=self.save_and_exit).pack(pady=10)

        self.root.mainloop()

    # Doctor management 

    def manage_doctors(self):
        win = tk.Toplevel(self.root)
        win.title("Doctor Management")

        tk.Button(win, text="Add Doctor", command=self.add_doctor).pack(pady=10)
        tk.Button(win, text="View Doctors",
                  command=lambda: self.view_list(self.doctors, "Doctors")).pack(pady=10)
        tk.Button(win, text="Delete Doctor", command=self.delete_doctor).pack(pady=10)

    def add_doctor(self):
        first = simpledialog.askstring("Add Doctor", "First Name:")
        last = simpledialog.askstring("Add Doctor", "Surname:")
        spec = simpledialog.askstring("Add Doctor", "Speciality:")

        if not (first and last and spec):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        self.doctors.append(Doctor(first, last, spec))
        messagebox.showinfo("Success", "Doctor Added.")

    def delete_doctor(self):
        if not self.doctors:
            messagebox.showwarning("Warning", "No doctors available.")
            return

        doctor_list = "\n".join(
            [f"{i+1}. {d.full_name()}" for i, d in enumerate(self.doctors)]
        )
        index = simpledialog.askinteger("Delete Doctor", doctor_list)

        if index and 1 <= index <= len(self.doctors):
            removed = self.doctors.pop(index - 1)
            messagebox.showinfo("Success", f"{removed.full_name()} deleted.")
        else:
            messagebox.showerror("Error", "Invalid selection.")

    # Patient management 

    def manage_patients(self):
        win = tk.Toplevel(self.root)
        win.title("Patient Management")

        tk.Button(win, text="Add Patient", command=self.add_patient).pack(pady=10)
        tk.Button(win, text="View Patients",
                  command=lambda: self.view_list(self.patients, "Patients")).pack(pady=10)
        tk.Button(win, text="View By Family",
                  command=self.view_patients_by_family).pack(pady=10)

    def add_patient(self):
        first = simpledialog.askstring("Add Patient", "First Name:")
        surname = simpledialog.askstring("Add Patient", "Surname:")
        age = simpledialog.askstring("Add Patient", "Age:")

        try:
            age = int(age)
        except:
            messagebox.showerror("Error", "Age must be a number.")
            return

        mobile = simpledialog.askstring("Add Patient", "Mobile:")
        address = simpledialog.askstring("Add Patient", "Address:")
        symptoms = simpledialog.askstring("Add Patient", "Symptoms:")

        symptoms = [s.strip() for s in symptoms.split(",")] if symptoms else []

        self.patients.append(Patient(first, surname, age, mobile, address, symptoms))
        messagebox.showinfo("Success", "Patient Added.")

    # View patients grouped by family name
    def view_patients_by_family(self):
        families = {}

        for p in self.patients:
            families.setdefault(p.surname, []).append(p)

        win = tk.Toplevel(self.root)
        win.title("Patients by Family")
        text = tk.Text(win, width=120)
        text.pack()

        for surname, members in families.items():
            text.insert(tk.END, f"Family: {surname}\n")
            for m in members:
                text.insert(tk.END, f"  - {m}\n")
            text.insert(tk.END, "\n")

    # task brief tasks done 4 

    def view_list(self, lst, title):
        win = tk.Toplevel(self.root)
        win.title(title)
        text = tk.Text(win, width=120)
        text.pack()

        for item in lst:
            text.insert(tk.END, "- " + str(item) + "\n")

    def assign_doctor(self):
        if not self.patients or not self.doctors:
            messagebox.showwarning("Warning", "Need at least one doctor and patient.")
            return

        p_list = "\n".join([f"{i+1}. {p.full_name()}" for i, p in enumerate(self.patients)])
        d_list = "\n".join([f"{i+1}. {d.full_name()}" for i, d in enumerate(self.doctors)])

        p_i = simpledialog.askinteger("Assign Doctor", p_list)
        d_i = simpledialog.askinteger("Assign Doctor", d_list)

        if p_i and d_i:
            self.patients[p_i - 1].doctor = self.doctors[d_i - 1].full_name()
            messagebox.showinfo("Assigned", "Doctor assigned successfully.")

    def discharge_patient(self):
        if not self.patients:
            return

        lst = "\n".join([f"{i+1}. {p.full_name()}" for i, p in enumerate(self.patients)])
        choice = simpledialog.askinteger("Discharge", lst)

        if choice:
            self.discharged.append(self.patients.pop(choice - 1))
            messagebox.showinfo("Success", "Patient discharged.")

    def view_discharged(self):
        self.view_list(self.discharged, "Discharged Patients")

    def update_admin(self):
        name = simpledialog.askstring("Admin", "New Name:")
        address = simpledialog.askstring("Admin", "New Address:")

        if name:
            self.admin.name = name
        if address:
            self.admin.address = address

        messagebox.showinfo("Updated", "Admin info updated.")

    def save_and_exit(self):
        save_data(self.doctors, self.patients, self.discharged)
        self.root.destroy()


# Program start
if __name__ == "__main__":
    # Username: mmm | Password: mmm123
    admin = Admin("mmm", "mmm123")

    try:
        if admin.login():
            doctors, patients, discharged = load_data()
            HospitalGUI(admin, doctors, patients, discharged)
    except Exception as e:
        messagebox.showerror("Error", str(e))
