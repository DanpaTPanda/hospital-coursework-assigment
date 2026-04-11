# Project: Hospital Management System - Improved Version - with all the missing taks been completed
# Author:  Michael Omotuyi
# Property of: Michael Omotuyi 
# GitHub:  https://github.com/DanpaTPanda
# Please do not copy or distribute without permission.
# Note: this code was done in spyder

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, ttk
import matplotlib.pyplot as plt
from Admin_Improved import HospitalSystem
from Doctor_Improved import Doctor
from Patient_Improved import Patient

#LOGIN
class LoginWindow:
    def __init__(self, system):
        self.sys = system
        self.root = tk.Tk()
        self.root.title("System Login")
        self.root.geometry("300x280") 
        self.root.configure(bg="#2c3e50")

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

        self.login_btn = tk.Button(self.root, text="Login", command=self.check_login, 
                                   bg="#27ae60", fg="white", width=15)
        self.login_btn.pack(pady=15)

        self.status_label = tk.Label(self.root, text=f"Attempts remaining: {self.max_attempts}", 
                                     fg="#ecf0f1", bg="#2c3e50", font=("Helvetica", 8))
        self.status_label.pack()

        self.authenticated = False
        self.root.mainloop()
        
#HARDCODED FOR NOW IT THOSE THE JOB
    def check_login(self):
        if self.user_var.get() == "mmm" and self.pass_var.get() == "mmm123":
            self.authenticated = True
            self.root.destroy()
        else:
            self.attempts += 1
            remaining = self.max_attempts - self.attempts
            
            if self.attempts >= self.max_attempts:
                messagebox.showerror("System Locked", "Too many failed attempts. Access Denied.")
                self.root.destroy() 
            else:
                self.status_label.config(text=f"Attempts remaining: {remaining}", fg="#e74c3c")
                messagebox.showwarning("Access Denied", f"Invalid Credentials.\n{remaining} attempts left.")

class HospitalGUI:
    def __init__(self, system):
        self.sys = system
        self.root = tk.Tk()
        self.root.title("Hospital Management System - Improved")
        self.root.geometry("600x800")
        self.root.configure(bg="#f4f7f6")

        #BASIC STYLING SETUP
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=5)
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), background="#f4f7f6", foreground="#2c3e50")

        #HEADER 
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="HOSPITAL HQ", font=("Helvetica", 18, "bold"), 
                 fg="white", bg="#2c3e50").pack(pady=10)
        tk.Label(header_frame, text=f"Administrator: {self.sys.admin_name}", 
                 fg="#bdc3c7", bg="#2c3e50", font=("Helvetica", 9)).pack()

        #MAIN WRAPPER
        main_frame = tk.Frame(self.root, bg="#f4f7f6", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        def create_section(parent, title):
            lbl = tk.Label(parent, text=title, font=("Helvetica", 11, "bold"), 
                           bg="#f4f7f6", fg="#7f8c8d")
            lbl.pack(anchor="w", pady=(15, 5))
            line = tk.Frame(parent, height=1, bg="#dcdde1")
            line.pack(fill=tk.X, pady=(0, 10))

        #BUTTONS FOR MANAGEMENT
        create_section(main_frame, "DOCTOR + PATIENT + APPOINTMENT")
        btn_grid = tk.Frame(main_frame, bg="#f4f7f6")
        btn_grid.pack(fill=tk.X)

        commands = [
            ("👨‍⚕️ Doctor Management", self.doctor_sub_menu), # Replaced standalone Doctor buttons
            ("👥 Register Patient", self.add_patient),
            ("📋 View Active Patients", lambda: self.view_list("patients")),
            ("📅 Log Appointment", self.log_appointment), 
            ("🔄 Relocate Patient", self.assign_relocate),
            ("🚪 Discharge", self.discharge_patient)
        ]

        for i, (text, cmd) in enumerate(commands):
            btn = tk.Button(btn_grid, text=text, command=cmd, width=22, height=2, 
                            bg="white", relief="flat", highlightthickness=1, 
                            highlightbackground="#dcdde1", activebackground="#ecf0f1")
            btn.grid(row=i//2, column=i%2, padx=5, pady=5)

        #OTHER FEATURES
        create_section(main_frame, "FAMILY + ARCHIVED")
        
        tk.Button(main_frame, text="👨‍👩‍👧‍👦 Group Patients by Family", command=self.group_family, 
                  width=48, bg="#3498db", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)
        
        tk.Button(main_frame, text="📤 View Discharge History", command=self.view_discharged, 
                  width=48, bg="white", relief="flat", highlightthickness=1).pack(pady=5)

        #REPORTS & SETTINGS (Both Text and Diagram options available)
        create_section(main_frame, "REPORTS + SETTINGS")
        
        tk.Button(main_frame, text="📊 Text Management Report", command=self.show_reports, 
                  width=48, bg="#34495e", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)

        tk.Button(main_frame, text="📈 View Data Charts", command=self.view_all_diagrams, 
                  width=48, bg="#27ae60", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)
        
        tk.Button(main_frame, text="⚙️ Update Admin Profile", command=self.update_admin_info, 
                  width=48, bg="white", relief="flat", highlightthickness=1).pack(pady=5)

        #EXIT
        tk.Button(self.root, text="EXIT & SAVE SYSTEM", command=self.save_and_exit, 
                  bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold"), height=2).pack(fill=tk.X, side=tk.BOTTOM)

        self.root.mainloop()

    def doctor_sub_menu(self):
        # SUB-MENU 
        win = tk.Toplevel(self.root)
        win.title("STAFF ADMIN")
        win.geometry("350x250")
        win.configure(bg="#ecf0f1")
        tk.Label(win, text="DOCTOR OPERATIONS", font=("Helvetica", 12, "bold"), bg="#ecf0f1").pack(pady=15)
        tk.Button(win, text="ADD NEW DOCTOR", command=self.add_doctor, width=25, height=2).pack(pady=5)
        tk.Button(win, text="VIEW DOCTORS", command=lambda: self.view_list("doctors"), width=25, height=2).pack(pady=5)
        tk.Button(win, text="REMOVE DOCTOR", command=self.delete_doctor, width=25, height=2, fg="red").pack(pady=5)

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
        name = simpledialog.askstring("Staff", "Doctor Name:")
        if name:
            spec = simpledialog.askstring("Staff", "Speciality:")
            mob = simpledialog.askstring("Staff", "Mobile:")
            self.sys.doctors.append(Doctor(name, spec, mob))
            self.sys.save_data()
            messagebox.showinfo("Success", "New staff record created.")

    def delete_doctor(self):
        # REMOVE DOC
        if not self.sys.doctors: 
            messagebox.showinfo("Empty", "No doctors available to remove.")
            return
        list_str = "\n".join([f"{i+1}. {d.name}" for i, d in enumerate(self.sys.doctors)])
        idx = simpledialog.askinteger("DELETE", f"SELECT NUMBER TO DELETE:\n\n{list_str}")
        if idx and 1 <= idx <= len(self.sys.doctors):
            removed = self.sys.doctors.pop(idx-1)
            self.sys.save_data()
            messagebox.showinfo("OK", f"Doctor {removed.name} removed.")

    def add_patient(self):
        fname = simpledialog.askstring("Patient", "First Name:")
        if fname:
            lname = simpledialog.askstring("Patient", "Surname:")
            age = simpledialog.askinteger("Patient", "Age:")
            mob = simpledialog.askstring("Patient", "Mobile:")
            addr = simpledialog.askstring("Patient", "Address:")
            sym = simpledialog.askstring("Patient", "Symptoms (Comma Separated):")
            
            p = Patient(fname, lname, age if age else 0, mob if mob else "N/A", addr if addr else "N/A")
            if sym:
                p.symptoms = [s.strip() for s in sym.split(",")]
                
            self.sys.patients.append(p)
            self.sys.save_data()
            messagebox.showinfo("Success", "Patient record created.")

    def log_appointment(self):
        # LOG SETUP
        n = simpledialog.askstring("INPUT", "PATIENT FULL NAME:")
        if not n: return
        m = simpledialog.askstring("INPUT", "MONTH (JAN, FEB...):")
        if not m: return
        for p in self.sys.patients:
            if p.full_name().lower() == n.lower():
                p.appointments[m.upper()] = p.appointments.get(m.upper(), 0) + 1
                self.sys.save_data()
                messagebox.showinfo("OK", "Appointment Logged.")
                return
        messagebox.showerror("ERROR", "Patient Not Found.")

    def show_reports(self):
        # TEXT REPORT OPTION
        rep_win = tk.Toplevel(self.root)
        rep_win.title("Executive Management Report")
        report = self.sys.get_management_report()
        
        txt = scrolledtext.ScrolledText(rep_win, width=65, height=20, font=("Courier New", 10))
        txt.pack(padx=20, pady=20)
        
        res = "HOSPITAL ANALYTICS SUMMARY\n" + "="*50 + "\n"
        res += f"Active Staff Count    : {report['total_doctors']}\n"
        res += f"Total Active Patients : {len(self.sys.patients)}\n\n"
        
        res += "PATIENT LOAD PER DOCTOR:\n"
        for doc_name, count in report["patients_per_doctor"].items():
            res += f" - {doc_name:<20}: {count} patients\n"
            
        res += "\nAPPOINTMENT VOLUME (BY MONTH):\n"
        for doc_name, months in report["appointments"].items():
            m_data = ", ".join([f"{m}: {c}" for m, c in months.items()])
            res += f" - {doc_name:<20}: {m_data if m_data else 'No data'}\n"

        txt.insert(tk.END, res)
        txt.config(state=tk.DISABLED)

    def view_all_diagrams(self):
        # VISUAL DATA CHARTS
        report = self.sys.get_management_report()
        
        # Create a figure with multiple subplots
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('HOSPITAL MANAGEMENT ANALYTICS', fontsize=16, fontweight='bold')

        # Diagram B: Patients per Doctor (Bar Chart)
        docs = list(report["patients_per_doctor"].keys())
        counts = list(report["patients_per_doctor"].values())
        axs[0, 0].bar(docs, counts, color='#3498db')
        axs[0, 0].set_title('Patients per Doctor')
        axs[0, 0].tick_params(axis='x', rotation=30)

        # Diagram D: Illness Types (Pie Chart)
        illnesses = list(report["illness"].keys())
        ill_counts = list(report["illness"].values())
        if illnesses:
            axs[0, 1].pie(ill_counts, labels=illnesses, autopct='%1.1f%%', startangle=140)
            axs[0, 1].set_title('Illness Distribution')
        else:
            axs[0, 1].text(0.5, 0.5, 'No Illness Data', ha='center')

        # Diagram C: Appointments per Month (Aggregated Line Chart)
        has_data = False
        for doc, months in report["appointments"].items():
            if months:
                has_data = True
                axs[1, 0].plot(list(months.keys()), list(months.values()), marker='o', label=doc)
        
        if has_data:
            axs[1, 0].set_title('Appointments per Month')
            axs[1, 0].legend(fontsize='x-small')
        else:
            axs[1, 0].text(0.5, 0.5, 'No Appointment Data', ha='center')

        # A: Total Statistics
        axs[1, 1].axis('off')
        stats_text = f"SYSTEM TOTALS\n{'-'*20}\nDoctors: {report['total_doctors']}\nPatients: {len(self.sys.patients)}"
        axs[1, 1].text(0.1, 0.5, stats_text, fontsize=14, fontweight='bold', family='monospace')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    def group_family(self):
        # FAMILY VIEW 
        fams = self.sys.group_by_family()
        win = tk.Toplevel(self.root)
        win.title("FAMILY DIRECTORY")
        txt = scrolledtext.ScrolledText(win, width=65, height=30, font=("Helvetica", 10))
        txt.pack(padx=20, pady=20)
        
        output = "HOSPITAL FAMILY GROUPS\n" + "="*50 + "\n\n"
        if not fams:
            output += "NO PATIENTS REGISTERED."
        else:
            for surname, names in fams.items():
                output += f"FAMILY NAME : {surname.upper()}\n"
                output += f"MEMBERS     : {', '.join(names)}\n"
                output += "-"*50 + "\n"
        
        txt.insert(tk.END, output)
        txt.config(state=tk.DISABLED)
    def update_admin_info(self):
        new_name = simpledialog.askstring("Admin", "Name:", initialvalue=self.sys.admin_name)
        new_addr = simpledialog.askstring("Admin", "Address:", initialvalue=self.sys.admin_address)
        if new_name and new_addr:
            self.sys.update_admin(new_name, new_addr)
            messagebox.showinfo("Update", "System credentials updated.")

    def assign_relocate(self):
        p_name = simpledialog.askstring("Transfer", "Patient Full Name:")
        d_name = simpledialog.askstring("Transfer", "New Doctor Name:")
        
        success = self.sys.relocate_patient(p_name, d_name)
        if success:
            messagebox.showinfo("Transfer Complete", f"{p_name} is now under the care of {d_name}.")
        else:
            messagebox.showerror("Error", "Could not find that patient or doctor. Check spelling.")

    def discharge_patient(self):
        target_name = simpledialog.askstring("Discharge", "Full Name of Patient:")
        
        if not target_name:
            return

        # FIND THE PATIENT OBJECT
        found_patient = None
        for p in self.sys.patients:
            if p.full_name().lower() == target_name.lower():
                found_patient = p
                break
                
        if found_patient:
            if found_patient.doctor:
                for d in self.sys.doctors:
                    if d.name == found_patient.doctor:
                        # Check if the name exists in the doctor's list before removing
                        if found_patient.full_name() in d.patients:
                            d.patients.remove(found_patient.full_name())
                        break
            
            self.sys.patients.remove(found_patient)
            self.sys.discharged.append(found_patient)
            self.sys.save_data()
            
            messagebox.showinfo("Discharged", f"{found_patient.full_name()} has been moved to historical records.")
        else:
            messagebox.showerror("Not Found", "Patient not found in system.")

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
    system = HospitalSystem()
    login = LoginWindow(system)
    
    if login.authenticated:
        HospitalGUI(system)