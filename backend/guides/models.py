from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from ckeditor.fields import RichTextField

class Program(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex=r'^[\w\s\-]+$',
            message='Назва може містити лише літери, цифри, пробіли та дефіси.'
        )]
    )
    os = models.CharField(
        max_length=20,
        choices=[('iOS', 'iOS'), ('Android', 'Android')]
    )

    def __str__(self):
        return f"{self.name} ({self.os})"

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.title


class Instruction(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='instructions')
    title = models.CharField(
        max_length=255,
        validators=[RegexValidator(
            regex=r'^.{5,}$',
            message='Заголовок має бути не коротший 5 символів.'
        )]
    )
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title


class Step(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='steps')
    text = RichTextField()
    image = models.ImageField(upload_to='steps/', blank=True, null=True)
    order = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        ordering = ['order']


class Feedback(models.Model):
    text = models.TextField(
        validators=[RegexValidator(
            regex=r'^.{10,}$',
            message='Відгук має бути не менше 10 символів.'
        )]
    )
    instruction = models.ForeignKey(Instruction, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)


class Review(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex=r'^.{2,}$',
            message='Імʼя має бути не менше 2 символів.'
        )]
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(
        validators=[RegexValidator(
            regex=r'^.{10,}$',
            message='Коментар має бути не менше 10 символів.'
        )]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} – {self.rating}★"