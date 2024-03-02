from django.contrib import admin
from companies.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "industry", "location", "contact_person", "krs"]
