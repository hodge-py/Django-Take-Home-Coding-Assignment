from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductData


def index(request):
    items = ProductData.objects.all()
    return render(request, "index.html", {"items": items})

# Create your views here.
