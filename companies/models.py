from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    industry = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)

    contact_person = models.CharField(max_length=100)

    krs = models.CharField(max_length=100)

    def __str__(self):
        return self.name