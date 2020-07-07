from django.db import models

# Create your models here.


class Crude(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name