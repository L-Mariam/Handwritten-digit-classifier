from django.db import models

# Create your models here.
class Counter(models.Model):
    key = models.Charfield(max_length=10)
    value = models.IntegerField
    