from django.db import models
from ckeditor.fields import RichTextField

class Instruction(models.Model):
    CATEGORY_CHOICES = [
        ('viber', 'Viber'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('settings', 'Налаштування'),
    ]
    
    OS_CHOICES = [
        ('android', 'Android'),
        ('ios', 'iOS'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='settings')  # Додаємо default
    os_type = models.CharField(max_length=10, choices=OS_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    steps = RichTextField()  # Використовуємо RichTextField для контенту
    image = models.ImageField(upload_to="instructions_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматичне заповнення

    def __str__(self):
        return f"{self.title} ({self.os_type})"