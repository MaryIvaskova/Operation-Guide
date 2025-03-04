
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Менеджер для кастомного користувача
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Користувач повинен мати email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

# Кастомна модель користувача
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Видаляємо стандартне ім'я користувача
    role = models.CharField(
        max_length=10,
        choices=[("admin", "Адміністратор"), ("superuser", "Суперкористувач")],
        default="admin"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# 📌 Інші моделі (Пристрої, Застосунки, Інструкції тощо)
class Device(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    os = models.CharField(max_length=10, choices=[('iOS', 'iOS'), ('Android', 'Android')])

    def __str__(self):
        return f"{self.model} ({self.os})"

class App(models.Model):
    name = models.CharField(max_length=255)
    os = models.CharField(max_length=10, choices=[('iOS', 'iOS'), ('Android', 'Android')])

    def __str__(self):
        return self.name

class Instruction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class InstructionStep(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    step_text = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['step_number']

class Feedback(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')])
    date = models.DateTimeField(auto_now_add=True)

class Shortcut(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class AdBlock(models.Model):
    ad_text = models.TextField()
    image_url = models.URLField()
    target_url = models.URLField()
    display_message = models.CharField(
        max_length=255, default="Ось так виглядає реклама, на неї не варто натискати"
    )

class SupportLink(models.Model):
    platform = models.CharField(max_length=10, choices=[('Telegram', 'Telegram'), ('Viber', 'Viber')])
    link = models.URLField()