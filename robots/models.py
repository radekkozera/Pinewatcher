from django.db import models

class Robot(models.Model):
    TYPE_CHOICES = [
        ("four_wheel", "Four Wheel"),
        ("amphibia", "Amphibia"),
        ("tracked", "Tracked"),
        ("flying", "Flying"),
    ]

    serial_number = models.CharField(max_length=100)

    production_date = models.DateField()

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    communication_device = models.OneToOneField(
        'communication.CommunicationDevice', on_delete=models.SET_NULL, null=True, related_name="robot"
    )

    company = models.ForeignKey(
        'companies.Company', on_delete=models.CASCADE, related_name="robots"
    )

    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="robots"
    )

    def __str__(self):
        return f"{self.serial_number} - {self.type}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name
