from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    TRACKING_CHOICHES = [
        ('STRENGTH', 'Força (Séries, Reps, Carga)'),
        ('TIME', 'Tempo (Duração)'),
        ('COMPLETION', 'Conclusão (Check)'),
    ]

    name = models.CharField(max_length=100)
    body_part = models.CharField(max_length=50)
    tracking_type = models.CharField(max_length=20, choices=TRACKING_CHOICHES)

    def __str__(self):
        return self.name
    

class WorkoutTemplate(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class WorkoutSession(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(WorkoutTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
    

class ExerciseLog(models.Model):

    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_number = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField(null=True, blank=True) 
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    duration_secods = models.PositiveSmallIntegerField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercise.name} | Série {self.set_number}"