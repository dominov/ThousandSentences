from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    name = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    min_completed_sentences = models.PositiveIntegerField(default=6)

    def __str__(self):
        return f"{self.level.name} - {self.name}"


# TODO: change phrase_spanish to spanish_phrase
# TODO: change phrase_english to english_phrase
class Sentence(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    phrase_spanish = models.TextField()
    phrase_english = models.TextField()
    keywords = models.CharField(max_length=20, blank=True, null=True)
    difficulty = models.PositiveIntegerField(default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"({self.topic}) {self.phrase_spanish[:40]}... - {self.phrase_english[:40]}..."


class StudentStatistics(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    failed_attempts = models.PositiveIntegerField(default=0)
    total_attempts = models.PositiveIntegerField(default=0)
    last_attempt_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.sentence.phrase_spanish}"
