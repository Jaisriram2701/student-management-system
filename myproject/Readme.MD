# Student Management System (SMS)

This is a simple and clean web-based Student Management System built using **Django**.  
The project allows you to manage student details with options to add, update, delete, restore, and permanently remove records.  
It is designed with a clean UI and basic styling suitable for learning and portfolio purposes.

---

##  Features

- Add new student records  
- Update existing student details  
- Soft delete (move records to Trash)  
- Restore deleted records  
- Permanently delete records  
- Simple and clean table-based UI  
- Success and alert message notifications  

---

##  Technologies Used

- Python  
- Django  
- HTML5  
- CSS3  
- SQLite (default Django database)

---

## 📂 Project Structure

## 📂 Project Structure

```plaintext
myproject/
├── manage.py
├── db.sqlite3
│
├── myproject/                  # Project settings and URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── base/                       # Main app (student-related logic)
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/              # App-level templates (user pages)
│       ├── home.html
│       ├── update.html
│       ├── delete.html
│       ├── trash.html
│       ├── addstudent.html
│       └── about.html
│
├── templates/                  # Shared/root templates
│   ├── main.html               # Base layout
│   └── nav.html                # Navigation bar
│
└── static/                     # Static files
    ├── style.css
    └── images/                 # Backgrounds, icons, logos
        ├── home_bg1.png
        ├── school_banner.png
        └── other_images...
