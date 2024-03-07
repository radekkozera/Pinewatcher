from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Company


@method_decorator(csrf_exempt, name="dispatch")
def create_company(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body.decode("utf-8"))
    name = data.get("name")
    industry = data.get("industry")
    location = data.get("location")
    description = data.get("description")
    contact_person = data.get("contact_person")
    krs = data.get("krs")

    company = Company.objects.create(
        name=name,
        industry=industry,
        location=location,
        description=description,
        contact_person=contact_person,
        krs=krs,
    )

    return JsonResponse({"id": company.id}, status=201)

