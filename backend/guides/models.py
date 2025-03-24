from django.db import models
from ckeditor.fields import RichTextField

class App(models.Model):
    name = models.CharField(max_length=100)
    os = models.CharField(max_length=20, choices=[('iOS', 'iOS'), ('Android', 'Android')])

    def __str__(self):
        return f"{self.name} ({self.os})"

class Instruction(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='instructions')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Step(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='steps')
    text = RichTextField()
    image = models.ImageField(upload_to='steps/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Feedback(models.Model):
    text = models.TextField()
    instruction = models.ForeignKey(Instruction, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback #{self.id}"