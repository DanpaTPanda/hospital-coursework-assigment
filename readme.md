# 🏥 Hospital Management System by michael omotuyi

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue) 
![License](https://img.shields.io/badge/license-MIT-green)

---

### 📌 Overview
> This project was developed as part of the **CMP4266 module**. It focuses on the end-to-end design, development, and rigorous testing of a professional **Hospital Management System**. It demonstrates the evolution of a software product from an 82% academic submission to a 100% optimized architecture.

<img width="783" height="423" alt="image" src="https://github.com/user-attachments/assets/e384f06e-6be1-4072-9209-52a8817f0b41" />


### ⚙️ Core Functionality
The system provides a robust administrative suite, enabling users to manage **Doctor and Patient lifecycles** with precision. From assigning medical staff to overseeing daily hospital operations, every feature is delivered through a **functional, streamlined interface** designed for efficiency.

---

## 🛠️ Technologies Used
* **Language:** Python 3.10+
* **Frameworks/Tools:** (e.g., Spring Boot / Tkinter / MySQL)
* **Data Handling:** JSON (Persistence) 
* **Reporting:** Matplotlib (Analytic charts)

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

---

## 📊 Detailed Feedback & Grading (Transparency)
> **Student:** Michael Omotuyi | **Student ID:** 23152483  
> **Module:** CMP4266 | **Final Mark:** 41/50 (**82%**)
> 
<img width="757" height="303" alt="image" src="https://github.com/user-attachments/assets/43009cf2-82fc-4fdb-9698-a4c783bf5050" />

### 🏆 Grading Breakdown
| Section | Description | Max Mark | Awarded |
| :--- | :--- | :---: | :---: |
| **Part A** | Design Documentation (UML & Flowcharts) | 10 | **10** |
| **Part B** | System Development (Core Logic & GUI) | 30 | **21** |
| **Part C** | Testing and Evaluation | 10 | **10** |
| **TOTAL** | | **50** | **41** |

---

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

## 📌 Notes
* **Original Submission:** The `original-submission` folder contains the exact coursework submitted for grading.
* **Improved Version:** The `improved-version` folder contains ongoing enhancements based on feedback.

---

## 🛠️ The Road to 100% (Post-Feedback Refactor)
*The original submission lost 9 marks in Part B. Below is how I have resolved those specific issues in the **`improved-version`** to reach a professional standard.*

### 1. Data Persistence (Missing in Original Submission)
* **Feedback:** "The hospital system should be able to store and load all patients’ data from and into a file."
* **Improved Fix:** Integrated `json` library to automatically `save_data()` and `load_data()` from `hospital_data.json` upon every administrative action.

### 2. Family Grouping (Missing in Original Submission)
* **Feedback:** "Patients of the same family are grouped together by Admin."
* **Improved Fix:** Developed the `group_by_family()` algorithm in `Admin_Improved.py` which maps patients by surname into a structured dictionary for easy retrieval.

### 3. Management Reporting (Missing in Original Submission)
* **Feedback:** "Missing total number of doctors, patients per doctor, and monthly appointments."
* **Improved Fix:** Created a `get_management_report()` function that calculates these metrics and displays them via a `scrolledtext` dashboard.


## 🚀 Improvements After Feedback

* **Patient Grouping:** Implementing structured family/group associations for easier patient management.
* **Data Persistence:** Adding robust file handling to allow for the saving and loading of system data between sessions.
* **Advanced Reporting:** Enhancing analytical features, such as patient demographics, statistics, and doctor workload tracking.

---
 
## 📂 Project Structure

```text
Hospital-Management-System/
├──BRIEF+feedback/
├── improved-version/
├── originalsubmission/
├── LICENSE
└── README.md
```

---

## 📂 Repository Contents
* [**Documentation Folder**](./BRIEF+feedback/) - Contains brief info and the original feedback doc.
* [**Improved Version**](./improved-version/) - Refactored code with 100% feature completion.
* [**Original Submission**](./originalsubmission/) - The version marked at 82%.

---

## 💡 Reflection & Learning
This project demonstrates my ability to:
* **Design systems** using UML diagrams
* **Develop functional applications** with real-world logic
* **Apply structured testing** methodologies
* **Analyse feedback** and improve software quality



