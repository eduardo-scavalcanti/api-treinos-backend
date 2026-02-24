from rest_framework import serializers
from .models import Exercise, WorkoutTemplate, WorkoutSession, ExerciseLog


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise

        fields = ['id', 'name', 'body_part', 'tracking_type']


class WorkoutTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTemplate

        fields = ['id', 'user', 'name', 'is_active']


class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession

        fields = ['id', 'user', 'template', 'date']


class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLog

        fields = ['id', 'session', 'exercise', 'set_number', 'reps', 'weight', 'duration_seconds', 'is_completed']