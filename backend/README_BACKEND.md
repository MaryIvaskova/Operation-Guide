

# Operation Guide — Backend (Django REST API)

Цифровий помічник для користувачів мобільних пристроїв.  
Проєкт на Django + DRF.

## Технології
- Python 3.13
- Django 5.x
- Django REST Framework
- PostgreSQL / SQLite
- drf-yasg (Swagger)
- django-filter

---

## Структура проєкту

backend/
├── operation_guide/   # Django core
├── guides/            # App: Інструкції / Програми / Відгуки
├── db.sqlite3         # SQLite база даних
├── manage.py
├── requirements.txt
└── .env.example

---

## Інсталяція та запуск Backend

### 1. Клонування проєкту

```bash
git clone <repo-url>
cd backend

2. Створення virtualenv

python3 -m venv venv
source venv/bin/activate

3. Встановлення залежностей

pip install -r requirements.txt

4. Створення .env файлу

Приклад:

DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

5. Міграції БД

python manage.py migrate

6. Створення суперкористувача (адмін)

python manage.py createsuperuser

7. Запуск сервера

python manage.py runserver



⸻

Адмінка

http://127.0.0.1:8000/admin/



⸻

API документація

Swagger:

http://127.0.0.1:8000/swagger/

Redoc:

http://127.0.0.1:8000/redoc/



⸻

Основні API Endpoints

Method	Endpoint	Опис
GET	/api/apps/	Cписок застосунків
GET	/api/topics/	Cписок тем
GET	/api/instructions/	Cписок інструкцій
GET	/api/instructions/{id}/	Детальна інструкція
POST	/api/feedback/	Надіслати відгук



⸻

Приклад архітектури моделей
	•	App — застосунок
	•	Topic — тема в середині застосунку
	•	Instruction — покрокова інструкція для теми
	•	Step — крок інструкції
	•	Review — відгук на інструкцію
	•	Feedback — загальний відгук користувача

⸻

Авторизація
	•	Публічне API → доступно без авторизації
	•	Адмінка → лише суперкористувач

⸻

Розробники
