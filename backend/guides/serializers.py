from rest_framework import serializers
from .models import Instruction, Program, Step, Feedback, Review, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


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
    program_name = serializers.CharField(source='program.name', read_only=True)
    program_os = serializers.CharField(source='program.os', read_only=True)

    class Meta:
        model = Instruction
        fields = [
            'id', 'title', 'description', 'category',
            'created_at', 'views', 'program_name', 'program_os', 'steps'
        ]


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'os']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'text', 'instruction', 'created_at']

    def validate_text(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Відгук має бути щонайменше 10 символів.")
        return value