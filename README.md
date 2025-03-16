# HMS Module (Hospital Management System) for Odoo

## 📌 Overview
This is a **Hospital Management System (HMS) Module** developed for **Odoo**. It provides a complete solution for managing patients, doctors, and hospital departments. The module includes advanced features like patient logging history, state tracking, access control, and integration with the CRM module.

## 🚀 Features
### 🔹 **Patients Management**
- Create and manage patient records.
- Store patient details such as:
  - First Name & Last Name
  - Birthdate (Auto calculates Age)
  - Medical History (HTML field)
  - Blood Type (Dropdown)
  - PCR (Checkbox)
  - CR Ratio (Mandatory if PCR is checked)
  - Address & Image Upload
  - Linked Doctors & Departments
- Patient status tracking (**Undetermined, Good, Fair, Serious**) with automatic log recording.
- Restrict selecting a **closed department**.
- **Doctors field (Many2many tags) is readonly** until a department is selected.
- **History field is hidden** if age is below 50.
- **PCR is auto-checked** if age is below 30, with a warning message.

### 🔹 **Doctors & Departments Management**
- **Doctors**:
  - Manage doctor profiles (First Name, Last Name, Image)
  - Linked to patients and departments
- **Departments**:
  - Manage hospital departments (Name, Capacity, Is Opened)
  - Linked to patients and doctors
  - Capacity is displayed in the patient view

### 🔹 **Patient Logging System**
- Tracks all status changes with timestamps.
- Log history includes:
  - **Created By, Date, Description**
  - Automatically logs status changes (e.g., "State changed to Serious")

### 🔹 **Access Control & Security**
- **Two User Groups:**
  1. **User Group:**
     - Can create/read/update **own** patient records.
     - Can **read-only** departments & doctors.
     - Cannot see **doctor fields** in the patient form.
     - Cannot access **Doctors menu**.
  2. **Manager Group:**
     - Full CRUD access to patients, departments, and doctors.
     - Can view **doctor fields** in patient forms.
     - Can access **Doctors menu**.

### 🔹 **CRM Integration**
- Patients linked with **CRM Customers**.
- New field in CRM customer model: **related_patient_id**.
- Prevent linking a patient to a CRM customer if their email is already assigned to another customer.
- Show the **website field** in the customer list view.
- Make **Tax ID field mandatory** for CRM customers.

### 🔹 **Patient Report Generation**
- Generate **PDF reports** for patients.
- Report includes:
  - Patient details
  - Linked doctors & departments
  - Patient status log history

## 📂 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TarekMo334455/hms-odoo-module.git
   ```
2. Copy the module into your Odoo **addons** directory.
3. Restart Odoo and install the module.
4. Assign appropriate **user roles** (User/Manager) in the settings.

## 🛠️ Configuration
- Ensure the **CRM module** is installed for full integration.
- Set user permissions via **Settings > Users & Companies**.

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact
For any inquiries, reach out at **tarekmo334455@gmail.com**.

---

🚀 **Transform hospital management with Odoo HMS Module!**


