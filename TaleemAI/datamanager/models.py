from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    skill_level = models.CharField(max_length=20, default='beginner')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Syllabus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topics_json = models.JSONField()

    def __str__(self):
        return f"Syllabus for {self.user.username}"


class QuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    score = models.IntegerField()
    answers_json = models.JSONField()

    def __str__(self):
        return f"QuizResponse by {self.user.username} on {self.topic}"


class MCQ(models.Model):
    question = models.TextField()
    options_json = models.JSONField()
    correct_answer = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.question[:50]
    
    




