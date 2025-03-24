from django.db import models

from django.db import models

class Customer(models.Model):
    HINT_CHOICES = [
        ('pet', "What is your pet's name?"),
        ('school', "What was your first school's name?"),
        ('color', "What is your favorite color?")
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    hint_selection = models.CharField(max_length=20, choices=HINT_CHOICES)
    hint_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    subject = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    time_required = models.IntegerField()
    importance = models.IntegerField()
    number_of_topics = models.IntegerField()


    def __str__(self):
        return f"{self.subject} - {self.deadline}"
