# management/models.py
from django.db import models

class Study(models.Model):
    study_name = models.CharField(max_length=200)
    study_phase = models.CharField(max_length=100)
    sponsor_name = models.CharField(max_length=200)
    study_description = models.TextField()

    def __str__(self):
        return self.study_name


