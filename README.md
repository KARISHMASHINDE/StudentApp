# StudentApp
Student Management System

# Objective
This is a Simple Student Management System Developed for Educational Purpose using Python (Django).

Features of this Project
Admin Users Can Do following Actions

See Overall Summary Charts of Students, Courses,
Manage Students/ Can Add Students
Manage Course / Can Add Course
See List of Student along with Detail
Admin Login
Admin DashBoard with Student and Course Count
How to Install and Run this project?
# Pre-Requisites:

--> Install Git Version Control [ https://git-scm.com/ ]

--> Install Python Latest Version [ https://www.python.org/downloads/ ]

--> Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

# Installation
Create a Folder where you want to save the project

Create a Virtual Environment and Activate

Install Virtual Environment First
$ pip install virtualenv

--> Activate Virtual Environment

$ source venv/scripts/activate

Clone this project
$ git clone https://github.com/KARISHMASHINDE/StudentApp.git Then, Enter into the project

$ cd django-student-management-system

Install Requirements from 'requirements.txt'
$ pip install -r requirements.txt

Add the hosts
Got to settings.py file (In this project setting.py file is present in "StudentManagement" Folder) Then, On allowed hosts, ALLOWED_HOSTS = [] Add [‘’]. ALLOWED_HOSTS = ['']

Now Run Server $ python3 manage.py runserver

Login Credentials

Create Super User (Admin)

$ python manage.py createsuperuser

Then Add Email, Username and Password or Use Default Credentials For SuperAdmin

Email: admin@gmail.com

Password: admin123

