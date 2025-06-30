# 🖼️ Django Gallery App

A Django-based gallery web app where authenticated users can upload, edit, and delete images, organized by categories. Built with Django’s built-in authentication system and file handling.

## 🚀 Features

- 🔐 User registration, login, and logout
- 📸 Upload images with titles, descriptions, and categories
- ✏️ Update and delete own images
- 📂 Categorize images (e.g., Nature, Architecture, People)
- 🧑‍💻 Users can only manage their own uploads
- 🎨 Clean and responsive UI (Bootstrap)

## 🛠️ Tech Stack

- **Backend:** Django 4.x+
- **Database:** SQLite (default)
- **Frontend:** Django Templates + Bootstrap
- **Auth:** Django built-in authentication
- **Image Handling:** Django `ImageField`, media routing

## 📁 Project Structure
gallery_project/
├── myapp/ # Main app (models, views, templates)
├── media/ # Uploaded images
├── static/ # Static files
├── templates/ # Shared templates
├── gallery_project/ # Django settings
├── manage.py
└── requirements.txt

🧠 How It Works
- Users can register/login to access the gallery dashboard.
- Uploaded images are tied to the user who posted them.
- Images are grouped into categories using a ForeignKey relationship.
- CRUD permissions are scoped per user—no editing others' images.

⚙️ Setup Instructions

git clone https://github.com/sophonie-1/gallery.git
cd gallery

Set Up Environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


Apply Migrations

python manage.py migrate

















