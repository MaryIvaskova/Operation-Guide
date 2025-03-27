# 🛠️ Operation Guide — Backend API

> REST API для системи створення та перегляду інструкцій з кроками, відгуками та оцінками.

---

## 📦 Стек технологій

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Django CKEditor**
- **django-filter**

---

## 🚀 Запуск проєкту

```bash
# Встановлення залежностей
pip install -r requirements.txt

# Міграції
python manage.py migrate

# Створити адміністратора
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

---

## 🔐 Адмін-панель

- **URL**: `http://127.0.0.1:8000/admin/`
- Доступні моделі:
  - App
  - Instruction (з Step inline)
  - Feedback
  - Review

---

## 🌐 API Endpoint'и

| Метод | URL | Опис |
|-------|-----|------|
| `GET` | `/api/instructions/` | Список інструкцій (фільтрація, пошук, пагінація) |
| `GET` | `/api/instructions/<id>/` | Деталі інструкції з кроками |
| `GET` | `/api/apps/` | Список додатків |
| `POST` | `/api/feedback/` | Надіслати фідбек |
| `GET/POST/PUT/DELETE` | `/api/reviews/` | CRUD по відгуках |

---

## 🔍 Пошук, фільтрація, сортування

### `/api/instructions/`

- **Пошук**: `?search=VPN`
- **Фільтр**:
  - `?app__name=Telegram`
  - `?app__os=Android`
  - `?category=Зв’язок`
- **Сортування**:
  - `?ordering=created_at`
  - `?ordering=-views`

---

## 📥 Пагінація

- За замовчуванням: 10 елементів на сторінку
- `?page=2`

---

## 📘 Моделі

### Instruction
- `title`, `description`, `category`
- `created_at`, `views`
- `app: ForeignKey`

### Step
- `text: RichText`, `image`, `order`
- `instruction: ForeignKey`

### App
- `name`, `os (iOS / Android)`

### Review
- `name`, `rating (1–5)`, `comment`, `instruction`, `created_at`

### Feedback
- `text`, `instruction`, `created_at`, `is_moderated`

---

## ✅ Валідація

- `rating`: `MinValueValidator(1)`, `MaxValueValidator(5)`
- Всі моделі — серіалізовані через DRF
- CKEditor підтримка в адмінці (Step.text)

---