from django.db import models


class CommunicationDevice(models.Model):
    FORM_TYPES = [
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]

    form_factor = models.CharField(max_length=100, choices=FORM_TYPES)

    location = models.OneToOneField("Location", on_delete=models.SET_NULL, null=True)

    telemetry = models.OneToOneField("Telemetry", on_delete=models.SET_NULL, null=True)


class Telemetry(models.Model):
    timestamp = models.DateTimeField()

    humidity = models.IntegerField()

    temparture = models.IntegerField()

    pressure = models.IntegerField()

    def __str__(self):
        return (
            f"{self.timestamp} - {self.humidity} - {self.temparture} - {self.pressure}"
        )


class Location(models.Model):
    timestamp = models.DateTimeField()

    lattitude = models.FloatField()

    longitude = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - {self.lattitude} - {self.longitude}"
