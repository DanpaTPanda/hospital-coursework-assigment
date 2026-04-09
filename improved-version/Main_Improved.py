# ---------------------------------------------------------
# Project: Hospital Management System - Improved Version
# Author:  Michael Omotuyi
# Property of: Michael Omotuyi 
# GitHub:  https://github.com/DanpaTPanda
# ---------------------------------------------------------
# This source code is the sole property of Michael Omotuyi.
# Unauthorized copying or distribution of this file, 
# via any medium, is strictly prohibited.
# ---------------------------------------------------------s

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, ttk
import matplotlib.pyplot as plt
from Admin_Improved import HospitalSystem
from Doctor_Improved import Doctor
from Patient_Improved import Patient

class LoginWindow:
    def __init__(self, system):
        self.sys = system
        self.root = tk.Tk()
        self.root.title("System Login")
        self.root.geometry("300x280") # Increased height slightly for warning text
        self.root.configure(bg="#2c3e50")

        # Initialize attempt counter
        self.attempts = 0
        self.max_attempts = 3

        tk.Label(self.root, text="ADMIN LOGIN", font=("Helvetica", 12, "bold"), 
                 fg="white", bg="#2c3e50").pack(pady=20)

        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        tk.Label(self.root, text="Username:", fg="white", bg="#2c3e50").pack()
        tk.Entry(self.root, textvariable=self.user_var).pack(pady=5)

        tk.Label(self.root, text="Password:", fg="white", bg="#2c3e50").pack()
        tk.Entry(self.root, textvariable=self.pass_var, show="*").pack(pady=5)

        # We store the button as a variable so we can disable it later
        self.login_btn = tk.Button(self.root, text="Login", command=self.check_login, 
                                   bg="#27ae60", fg="white", width=15)
        self.login_btn.pack(pady=15)

        # Label to show remaining attempts
        self.status_label = tk.Label(self.root, text=f"Attempts remaining: {self.max_attempts}", 
                                     fg="#ecf0f1", bg="#2c3e50", font=("Helvetica", 8))
        self.status_label.pack()

        self.authenticated = False
        self.root.mainloop()

    def check_login(self):
        # Default credentials
        if self.user_var.get() == "mmm" and self.pass_var.get() == "mmm123":
            self.authenticated = True
            self.root.destroy()
        else:
            self.attempts += 1
            remaining = self.max_attempts - self.attempts
            
            if self.attempts >= self.max_attempts:
                messagebox.showerror("System Locked", "Too many failed attempts. Access Denied.")
                self.root.destroy() # Close the app entirely for security
            else:
                self.status_label.config(text=f"Attempts remaining: {remaining}", fg="#e74c3c")
                messagebox.showwarning("Access Denied", f"Invalid Credentials.\n{remaining} attempts left.")

class HospitalGUI:
    def __init__(self, system):
        self.sys = system
        self.root = tk.Tk()
        self.root.title("Hospital Management System - improved version")
        self.root.geometry("600x750")
        self.root.configure(bg="#f4f7f6")

        # Custom Styling
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=5)
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), background="#f4f7f6", foreground="#2c3e50")

        # --- Header Section ---
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="HOSPITAL HQ", font=("Helvetica", 18, "bold"), 
                 fg="white", bg="#2c3e50").pack(pady=10)
        tk.Label(header_frame, text=f"Administrator: {self.sys.admin_name}", 
                 fg="#bdc3c7", bg="#2c3e50", font=("Helvetica", 9)).pack()

        # --- Main Container ---
        main_frame = tk.Frame(self.root, bg="#f4f7f6", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Helper to create section titles
        def create_section(parent, title):
            lbl = tk.Label(parent, text=title, font=("Helvetica", 11, "bold"), 
                           bg="#f4f7f6", fg="#7f8c8d")
            lbl.pack(anchor="w", pady=(15, 5))
            line = tk.Frame(parent, height=1, bg="#dcdde1")
            line.pack(fill=tk.X, pady=(0, 10))

        # --- Section: Management ---
        create_section(main_frame, "STAFF & PATIENT MANAGEMENT")
        btn_grid = tk.Frame(main_frame, bg="#f4f7f6")
        btn_grid.pack(fill=tk.X)

        commands = [
            ("👨‍⚕️ Add Doctor", self.add_doctor),
            ("👥 Register Patient", self.add_patient),
            ("📋 View Doctors", lambda: self.view_list("doctors")),
            ("📋 View Patients", lambda: self.view_list("patients")),
            ("🔄 Relocate Patient", self.assign_relocate),
            ("🚪 Discharge", self.discharge_patient)
        ]

        # Arrange buttons in 2 columns
        for i, (text, cmd) in enumerate(commands):
            btn = tk.Button(btn_grid, text=text, command=cmd, width=22, height=2, 
                            bg="white", relief="flat", highlightthickness=1, 
                            highlightbackground="#dcdde1", activebackground="#ecf0f1")
            btn.grid(row=i//2, column=i%2, padx=5, pady=5)

        # --- Section: Specialized Functions ---
        create_section(main_frame, "OPERATIONS & GROUPS")
        
        tk.Button(main_frame, text="👨‍👩‍👧‍👦 Group Patients by Family", command=self.group_family, 
                  width=48, bg="#3498db", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)
        
        tk.Button(main_frame, text="📤 View Discharge History", command=self.view_discharged, 
                  width=48, bg="white", relief="flat", highlightthickness=1).pack(pady=5)

        # --- Section: Analytics ---
        create_section(main_frame, "REPORTS & SETTINGS")
        
        tk.Button(main_frame, text="📊 Generate Management Report", command=self.show_reports, 
                  width=48, bg="#27ae60", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)
        
        tk.Button(main_frame, text="⚙️ Update Admin Profile", command=self.update_admin_info, 
                  width=48, bg="white", relief="flat", highlightthickness=1).pack(pady=5)

        # --- Footer ---
        tk.Button(self.root, text="QUIT & SAVE SYSTEM", command=self.save_and_exit, 
                  bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold"), height=2).pack(fill=tk.X, side=tk.BOTTOM)

        self.root.mainloop()

    # (Keep internal logic methods from the previous version, they are already fixed!)
    def view_list(self, list_type):
        win = tk.Toplevel(self.root)
        win.title(f"Database View: {list_type.title()}")
        items = self.sys.doctors if list_type == "doctors" else self.sys.patients
        txt = scrolledtext.ScrolledText(win, width=70, height=25, font=("Courier New", 10))
        txt.pack(padx=20, pady=20)
        
        output = f"{list_type.upper()} RECORDS\n" + "="*50 + "\n\n"
        for i in items:
            data = i.to_dict()
            for key, val in data.items():
                output += f"{key.replace('_', ' ').title():<15}: {val}\n"
            output += "-"*50 + "\n"
        txt.insert(tk.END, output if items else "Database empty.")
        txt.config(state=tk.DISABLED)

    def add_doctor(self):
        n = simpledialog.askstring("Staff", "Doctor Name:")
        if n:
            s = simpledialog.askstring("Staff", "Speciality:")
            m = simpledialog.askstring("Staff", "Mobile:")
            self.sys.doctors.append(Doctor(n, s, m))
            self.sys.save_data()
            messagebox.showinfo("Success", "New staff record created.")

    def add_patient(self):
        f = simpledialog.askstring("Patient", "First Name:")
        if f:
            l = simpledialog.askstring("Patient", "Surname:")
            a = simpledialog.askinteger("Patient", "Age:")
            m = simpledialog.askstring("Patient", "Mobile:")
            ad = simpledialog.askstring("Patient", "Address:")
            self.sys.patients.append(Patient(f, l, a, m, ad))
            self.sys.save_data()
            messagebox.showinfo("Success", "Patient record created.")

    def show_reports(self):
        rep_win = tk.Toplevel(self.root)
        rep_win.title("Executive Management Report")
        report = self.sys.get_management_report()
        
        txt = scrolledtext.ScrolledText(rep_win, width=60, height=20, font=("Courier New", 10))
        txt.pack(padx=20, pady=20)
        
        res = "HOSPITAL ANALYTICS SUMMARY\n" + "="*40 + "\n"
        res += f"Active Staff Count   : {report['total_doctors']}\n"
        res += f"Total Active Patients : {len(self.sys.patients)}\n\n"
        
        res += "PATIENT LOAD PER DOCTOR:\n"
        for d, c in report["patients_per_doctor"].items():
            res += f" - {d:<20}: {c} patients\n"
            
        res += "\nAPPOINTMENT VOLUME (BY MONTH):\n"
        for d, months in report["appointments"].items():
            m_data = ", ".join([f"{m}: {c}" for m, c in months.items()])
            res += f" - {d:<20}: {m_data if m_data else 'No data'}\n"

        txt.insert(tk.END, res)
        tk.Button(rep_win, text="📈 Open Illness Distribution Chart", command=self.plot_illness, 
                  bg="#27ae60", fg="white", padx=10).pack(pady=10)

    def plot_illness(self):
        report = self.sys.get_management_report()
        if not report["illness"]: 
            messagebox.showwarning("Data", "No illness data found.")
            return
        plt.figure(figsize=(8, 6))
        plt.pie(report["illness"].values(), labels=report["illness"].keys(), autopct='%1.1f%%', colors=['#3498db', '#e74c3c', '#2ecc71', '#f1c40f'])
        plt.title("Patient Population by Symptoms")
        plt.show()

    def group_family(self):
        families = self.sys.group_by_family()
        if not families:
            messagebox.showinfo("Groups", "No patient data.")
            return
        output = "FAMILY GROUPINGS\n" + "="*30 + "\n"
        for fam, members in families.items():
            output += f"Surname [{fam}]: {', '.join(members)}\n"
        messagebox.showinfo("Family Groups", output)

    def update_admin_info(self):
        n = simpledialog.askstring("Admin", "Name:", initialvalue=self.sys.admin_name)
        a = simpledialog.askstring("Admin", "Address:", initialvalue=self.sys.admin_address)
        if n and a:
            self.sys.update_admin(n, a)
            messagebox.showinfo("Update", "System credentials updated.")

    def assign_relocate(self):
        p_name = simpledialog.askstring("Transfer", "Patient Full Name:")
        d_name = simpledialog.askstring("Transfer", "New Doctor Name:")
        if self.sys.relocate_patient(p_name, d_name):
            messagebox.showinfo("Transfer Complete", f"{p_name} is now under the care of {d_name}.")
        else:
            messagebox.showerror("Error", "Check name spelling for patient or doctor.")

    def discharge_patient(self):
        n = simpledialog.askstring("Discharge", "Full Name of Patient:")
        p = next((pt for pt in self.sys.patients if pt.full_name() == n), None)
        if p:
            self.sys.patients.remove(p)
            self.sys.discharged.append(p)
            self.sys.save_data()
            messagebox.showinfo("Discharged", f"{n} has been moved to historical records.")

    def view_discharged(self):
        win = tk.Toplevel(self.root)
        win.title("Archived Discharge Data")
        content = "\n".join([f"• {p.full_name()}" for p in self.sys.discharged])
        txt = scrolledtext.ScrolledText(win, width=40, height=15)
        txt.pack(padx=20, pady=20)
        txt.insert(tk.END, content if content else "No discharge records found.")

    def save_and_exit(self):
        self.sys.save_data()
        self.root.destroy()

if __name__ == "__main__":
    # 1. Initialize the data system first
    system = HospitalSystem()
    
    # 2. Launch the Login Gate
    login = LoginWindow(system)
    
    # 3. Only launch the main GUI if the user successfully logged in
    if login.authenticated:
        HospitalGUI(system)
