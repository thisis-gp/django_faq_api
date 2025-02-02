# Django FAQ API

## 📌 Overview

The Django FAQ API is a RESTful API that allows users to manage Frequently Asked Questions (FAQs) with multi-language support. It features:

- WYSIWYG Editor for rich-text formatting (using django-ckeditor)

- Automatic translations using Google Translate API

- Caching for optimized performance with Redis

- API endpoints to retrieve FAQs with language selection support

- Django Admin panel for easy management

## 🚀 Features

- Read FAQs via a REST API

- Multi-language translation support (English, Malayalam, Tamil etc.)

- WYSIWYG editor for enhanced formatting

- Caching for fast responses

- Django Admin interface for managing FAQs

## ⚙️ Installation Steps

### 1️⃣ Clone the Repository

```
git clone https://github.com/thisis-gp/django_faq_api.git
cd django_faq_api
```

### 2️⃣ Create and Activate a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure Database & Migrations

```
python manage.py makemigrations faq
python manage.py migrate
```
**Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

### 5️⃣ Set Up Redis for Caching (Optional but Recommended)

- Install Redis:

```
sudo apt install redis  # Linux
brew install redis  # macOS
```

- Start Redis Server:
```
redis-server
```

- Ensure Redis is running by testing:

```
redis-cli ping  # Should return PONG
```

### 6️⃣ Run the Development Server

```
python manage.py runserver
```

## 📌 API Endpoints

### ✅ List FAQs
```
GET /api/faqs/
```

Response:
```
[
  {
        "id": 1,
        "question": "What is your return policy?",
        "answer": "<h2 style=\"font-style:italic\"><strong>Our return policy is very generous...</strong></h2>",
        "question_ml": "നിങ്ങളുടെ റിട്ടേൺ നയം എന്താണ്?",
        "question_ta": "உங்கள் வருவாய் கொள்கை என்ன?"
    },
]
```

### ✅ Retrieve FAQs in a Specific Language
```
GET /api/faqs/?lang=ml (for Malayalam)
```

Response:
```
[
  {
        "id": 1,
        "question": "നിങ്ങളുടെ റിട്ടേൺ നയം എന്താണ്?",
        "answer": "<h2 style=\"font-style:italic\"><strong>Our return policy is very generous...</strong></h2>",
        "question_ml": "നിങ്ങളുടെ റിട്ടേൺ നയം എന്താണ്?",
        "question_ta": "உங்கள் வருவாய் கொள்கை என்ன?"
    },
]
```

### ✅ Create a New FAQ

FAQs are created and managed through the Django admin interface.

1.  Access the admin panel at `http://127.0.0.1:8000/admin/`.
2.  Log in using the superuser credentials you created.
3.  Navigate to the "FAQ" section.
4.  Add new FAQs, providing the question (in English) and the answer (using the CKEditor WYSIWYG editor).
5.  Translations for configured languages (e.g. Malayalam and Tamil) will be automatically generated and stored upon saving.

## 📖 Contribution Guidelines

We welcome contributions! To contribute:

- Fork this repository.

- Create a new branch:
  ```
  git checkout -b feature-new-feature
  ```

- Commit your changes with meaningful messages:
  ```
  git commit -m "feat: Add support for Hindi translations"
  ```
  
- Push to your branch and submit a Pull Request.

## Docker (Optional - for local development)

1.  **Build and run with Docker Compose:**

    ```bash
    docker-compose up -d --build
    ```

2.  **Access:** The application will be available at `http://localhost:8000`.

## 🛠 Technologies Used

- Django & Django REST Framework

- CKEditor (WYSIWYG Editor for Rich Text)

- Google Translate API (Automatic translations)

- Redis (Caching for fast API responses)

- pytest (For unit testing)

## ⚡️ License

This project is licensed under the MIT License.

## Guide to create FAQ API using Django

[Click Here](https://alike-chameleon-f15.notion.site/BharatFD-Assignment-18dd71a6ceaa808692aada8da7a6de6b?pvs=4)

## 🎯 Author

Developed by D A GURUPRIYAN.

