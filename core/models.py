from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to="app_icons/")
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
from ckeditor.fields import RichTextField

class Instruction(models.Model):
    app = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="instructions")
    title = models.CharField(max_length=255)
    steps = RichCKEditor()
    image = models.ImageField(upload_to="instruction_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.app.name} - {self.title}"