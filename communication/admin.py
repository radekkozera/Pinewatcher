from django.contrib import admin
from communication.models import CommunicationDevice, Telemetry, Location

@admin.register(CommunicationDevice)
class CommunicationDeviceAdmin(admin.ModelAdmin):
    list_display = ["form_factor", "location", "telemetry"]

@admin.register(Telemetry)
class TelemetryAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "humidity", "temparture", "pressure"]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "lattitude", "longitude"]