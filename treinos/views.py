from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Exercise, WorkoutTemplate, WorkoutSession, ExerciseLog
from .serializers import ExerciseSerializer, WorkoutTemplateSerializer, WorkoutSessionSerializer, ExerciseLogSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutTemplateViewSet(viewsets.ModelViewSet):
    queryset = WorkoutTemplate.objects.all()
    serializer_class = WorkoutTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseLogViewSet(viewsets.ModelViewSet):
    queryset = ExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer
    permission_classes = [permissions.IsAuthenticated]