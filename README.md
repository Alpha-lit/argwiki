# 🎬 Disney Wiki Clone

A Django-powered **wiki-style platform** for Disney-inspired content.  
Browse news, cast members, characters, and tapes in a structured and stylish way.

---

## 🚀 Features

- 📰 **News**: List and detail pages for news articles  
- 🎭 **Cast**: Browse cast members and their roles, with individual detail pages  
- 👤 **Characters**: Explore characters with detailed descriptions  
- 📼 **Tapes**: Browse and view tape details  
- 🎨 **UI**: TailwindCSS-styled templates with a consistent base layout  

---

## 🏗️ Project Structure
```bash
argwiki/
│── disney/ # Project settings
│
├── story/ # Core app (base, home, shared templates)
│ └── templates/
│ ├── base.html
│ ├── room.html
│
├── news/
│ └── templates/news/
│ ├── list.html
│ ├── detail.html
│
├── cast/
│ └── templates/cast/
│ ├── list.html
│ ├── detail.html
│
├── characters/
│ └── templates/characters/
│ ├── list.html
│ ├── detail.html
│
├── tapes/
│ └── templates/tapes/
│ ├── list.html
│ ├── detail.html
│
└── manage.py
---
```
---

## ⚙️ Tech Stack

- **Backend**: Django 5.x (Python 3.10+)  
- **Frontend**: Django Templates + TailwindCSS classes  
- **Database**: SQLite (default)  
- **Version Control**: Git  

---

## 🛠️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/disney-wiki.git
cd disney-wiki

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
Now visit 👉 http://127.0.0.1:8000/
