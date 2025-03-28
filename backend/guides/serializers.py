from rest_framework import serializers
from .models import App, Instruction, Step, Feedback, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Рейтинг має бути в межах 1–5.")
        return value

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Ім’я має містити щонайменше 2 символи.")
        return value

    def validate_comment(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Коментар має містити щонайменше 10 символів.")
        return value


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'order', 'text', 'image']


class InstructionSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    app_name = serializers.CharField(source='app.name', read_only=True)
    app_os = serializers.CharField(source='app.os', read_only=True)

    class Meta:
        model = Instruction
        fields = [
            'id', 'title', 'description', 'category',
            'created_at', 'views', 'app_name', 'app_os', 'steps'
        ]


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'os']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'text', 'instruction', 'created_at']

    def validate_text(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Відгук має бути щонайменше 10 символів.")
        return value