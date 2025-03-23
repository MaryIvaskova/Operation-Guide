from rest_framework import serializers
from .models import App, Instruction, Step, Feedback


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
        