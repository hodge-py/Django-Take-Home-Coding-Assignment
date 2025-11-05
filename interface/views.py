from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductData, Tags


def index(request):
    items = ProductData.objects.distinct().all()
    cate = ProductData.objects.values_list('category', flat=True).distinct()
    tags = Tags.objects.values_list('name', flat=True).distinct()
    return render(request, "index.html", {"items": items, "cate": cate, "tags": tags})

# Create your views here.
