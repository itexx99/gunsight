# GunSight

GunSight is a Django-based online tracking system for a gun engraving and electroplating company. It allows staff to manage and track gun parts, orders, finishes, colors, and designs from start to finish.

---

## 🚀 Features

- Track custom gun orders by order number
- View parts, finishes, and status updates
- Admin interface for managing data
- Easily extendable and customizable

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.2
- SQLite (default dev database)
- HTML/CSS (Django templates)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/gunsight.git
cd gunsight
```

2. **Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create an admin**
```bash
python manage.py createsuperuser #Follow instructions
```

6. **Start the development server**
```bash
python manage.py runserver
```
Web Address: http://127.0.0.1:8000/ # for development

📌 Roadmap
 - Add status workflow: Received → In Progress → Complete

 - Implement file/image upload for engravings

 - Add user authentication

 - Build customer portal for tracking orders

🧠 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
