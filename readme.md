# 🏥 Hospital Management System

---

### 📌 Overview
> This project was developed as part of the **CMP4266 module**. It focuses on the end-to-end design, development, and rigorous testing of a professional **Hospital Management System**.

<img width="783" height="423" alt="image" src="https://github.com/user-attachments/assets/e384f06e-6be1-4072-9209-52a8817f0b41" />


### ⚙️ Core Functionality
The system provides a robust administrative suite, enabling users to manage **Doctor and Patient lifecycles** with precision. From assigning medical staff to overseeing daily hospital operations, every feature is delivered through a **functional, streamlined interface** designed for efficiency.

---
## 🎯 Features

### 🔐 Administrative Controls
* **Admin Login System:** Secure access for authorized personnel.
* **Management:** Full CRUD (Create, Read, Update, Delete) functionality for doctor profiles.
* **Profile Management:** Capability to update admin credentials and details.

### 🏥 Patient Management
* **Patient Oversight:** View comprehensive patient information at a glance.
* **Doctor Assignment:** Effortlessly assign specific doctors to patients.
* **Discharge System:** Manage the discharge process and maintain a historical **Discharged Patient List**.

### 💻 User Experience
* **Graphical User Interface (GUI):** A clean, intuitive interface for non-technical users.

📊 Assessment Result 

Grade received: 41/50 (82%) 

<img width="757" height="303" alt="image" src="https://github.com/user-attachments/assets/43009cf2-82fc-4fdb-9698-a4c783bf5050" />

## 📝 Feedback Summary

### ✅ Strengths
* **Design Documentation:** Received full marks (10/10).
* **Testing:** Received full marks (10/10).
* **Core Implementation:** Strong delivery of essential system features.
* **User Interface:** Successfully developed a functional GUI.
* **Organization:** Well-structured and professional submission.

---

### ⚠️ Areas for Improvement
* **Test Case Coverage:** Some features outlined in test cases were not fully implemented.
* **Data Persistence:** Currently lacks saving/loading functionality for system data.
* **Reporting:** Limited functionality regarding automated reports.

## 💬 Marker Comment

> "Excellent effort. There are some functions in the test case report that are not implemented in the main file. Overall, well done!" 

---
🧪 Test Cases 
| ID   | Feature                         | Description                                      | Expected Result                                      | Outcome |
|------|----------------------------------|--------------------------------------------------|------------------------------------------------------|--------|
| TC1  | Valid Login                     | Login with correct username and password         | User successfully logs into the system               | ✅ Pass |
| TC2  | Invalid Login                   | Enter incorrect username/password                | Error message displayed                              | ✅ Pass |
| TC3  | Login Attempt Limit             | Exceed maximum login attempts                    | "Too many failed login attempts" message shown       | ✅ Pass |
| TC4  | Add & View Doctor               | Add a new doctor and view doctor list            | Doctor successfully added and displayed              | ✅ Pass |
| TC5  | Add & View Patient              | Add a new patient and view patient list          | Patient successfully added and displayed             | ✅ Pass |
| TC6  | Patient Family Grouping         | Filter patients by similar family name           | Patients grouped by family name                      | ⚠️ Not Implemented |
| TC7  | Assign Doctor to Patient        | Assign a doctor to a selected patient            | Doctor correctly assigned to patient                 | ✅ Pass |
| TC8  | Discharge Patient               | Remove patient and view discharged list          | Patient removed and appears in discharged list       | ✅ Pass |
| TC9  | Update Admin Information        | Update admin name and address                    | Admin details successfully updated                   | ✅ Pass |
| TC10 | Save and Exit                   | Save system data and exit application            | Data saved successfully before exit                  | ✅ Pass |
 
## ⚠️ Reflection

> [!IMPORTANT]
> **Clarification on Patient Grouping**
> 
> * **The Challenge:** Feedback indicated that patient family grouping was missing. While a basic version existed—utilizing name-based filtering—it did not fully satisfy the structured requirements expected for the submission.
> * **The Lesson:** This highlighted the importance of clear feature demonstration and ensuring that implementation matches the specific technical definitions provided in a brief.
> * **The Solution:** I am currently refactoring this feature in the **improved-version** to move beyond simple filtering and provide a robust, structured grouping logic.

--- 

## 🚀 Improvements After Feedback

* **Patient Grouping:** Implementing structured family/group associations for easier patient management.
* **Data Persistence:** Adding robust file handling to allow for the saving and loading of system data between sessions.
* **Advanced Reporting:** Enhancing analytical features, such as patient demographics, statistics, and doctor workload tracking.

---
 
## 📂 Project Structure

```text
Hospital-Management-System/
├── original-submission/
├── improved-version/
└── README.md
```

📎 Documentation 
📄 Full detailed test cases and coursework files are available in the /docs folder. 

## 💡 Reflection & Learning
This project demonstrates my ability to:
* **Design systems** using UML diagrams
* **Develop functional applications** with real-world logic
* **Apply structured testing** methodologies
* **Analyse feedback** and improve software quality

---

## 🛠️ Technologies Used
* **Language:** (e.g., Python / Java / C#)
* **Frameworks/Tools:** (e.g., Spring Boot / Tkinter / MySQL)

---

## 📌 Notes
* **Original Submission:** The `original-submission` folder contains the exact coursework submitted for grading.
* **Improved Version:** The `improved-version` folder contains ongoing enhancements based on feedback.

---

## 📊 Final Grade & Feedback Analysis
> **Module:** CMP4266 | **Mark:** 41/50 (**82%**) | **Date:** 28/01/2026

### ✅ Grading Breakdown
| Category | Criteria | Max Mark | Awarded |
| :--- | :--- | :---: | :---: |
| **Part A** | Design Documentation (Flowcharts & UML) | 10 | **10** |
| **Part B** | System Development (Core Logic & GUI) | 30 | **21** |
| **Part C** | Testing and Evaluation | 10 | **10** |
| **TOTAL** | | **50** | **41** |

### 🔍 Gap Analysis (The Path to 100%)
The feedback highlighted specific areas where the original submission (v1) could be improved. I have addressed these in the **Improved Version (v2)**:

* **Data Persistence (0/3 Marks in v1):** * *Issue:* Data did not save between sessions.
    * *Fix:* Implemented `json` data persistence in `Admin_Improved.py` via `save_data()` and `load_data()`.
* **Family Grouping (0/2 Marks in v1):** * *Issue:* Patients were not grouped by family names.
    * *Fix:* Added `group_by_family()` function using a dictionary-mapping algorithm.
* **Management Reporting (1/3 Marks in v1):** * *Issue:* Missing specific metrics like appointments per month.
    * *Fix:* Integrated `get_management_report()` to calculate total doctors, patients per doctor, and monthly appointments.

### 💬 Marker's Final Comment
> *"Excellent effort. There are some functions in the test case report that are not implemented in the main file. Overall, well done!"*

---

## 📎 Original Documents
For full transparency, the original academic documents are available here:
* [Original Feedback Sheet (PDF)](./docs/Michael_Omotuyi_Feedback.pdf)
* [Design Flowcharts (Word)](./docs/12_week_Flowchart.docx)
