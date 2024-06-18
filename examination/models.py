from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField(default=datetime(year=2000, month=1, day=1))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Exam(BaseModel):
    subject = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.subject} {self.topic}'


class Question(BaseModel):
    question = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question} {self.difficulty}'


class TestQuestion(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.exam} {self.question}'


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} {self.answers} {self.correct}'


class Result(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    person_answer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.person} {self.exam} {self.question} {self.person_answer}'

"""
tests
id
subject
topic
"""