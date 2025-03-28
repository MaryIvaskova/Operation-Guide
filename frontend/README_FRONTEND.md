# 📘 Frontend API Documentation

This README is for frontend developers to integrate with the Django REST backend.

---

## 📱 Endpoints Overview

### 🔹 GET `/instructions/`
Get a list of all instructions.

**Supports:**
- Filtering: `app__name`, `category`, `app__os`
- Search: `title`, `description`
- Ordering: `created_at`, `views`
- Pagination: `?page=1&page_size=10`

---

### 🔹 GET `/instructions/<id>/`
Fetch single instruction with all steps, ordered.

---

### 🔹 GET `/apps/`
Fetch all available apps (used for filtering or tagging).

---

### 🔹 POST `/feedback/`
Send general feedback or link it to an instruction.

**Payload:**
```json
{
  "text": "Helpful guide!",
  "instruction": 1  // optional
}
```

---

### 🔹 GET `/reviews/`
Get all reviews.

---

### 🔹 POST `/reviews/`
Submit a review (with rating 1-5)

**Payload:**
```json
{
  "name": "John",
  "rating": 4,
  "comment": "Loved it!",
  "instruction": 2
}
```

---

## 🛡️ Admin Panel

- Path: `/admin/`
- Rich text editing enabled for steps (CKEditor)
- Step image preview shown in admin
- Only superusers can delete instructions

---

## 🔧 Stack

- Django + Django REST Framework
- CKEditor
- PostgreSQL or SQLite
- Django Filters (search, ordering, filter)
- Pagination ready