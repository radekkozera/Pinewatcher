from django.contrib import admin
from robots.models import Robot, Manufacturer

# Register your models here.


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number",
        "production_date",
        "type",
        "company",
        "manufacturer",
    ]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_person"]
