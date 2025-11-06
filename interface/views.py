from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductData, Tags
from .forms import searchForm

def index(request):
    items = ProductData.objects.distinct().all()
    cate = ProductData.objects.values_list('category', flat=True).distinct()
    tags = Tags.objects.values_list('name', flat=True).distinct()
    search = False
    return render(request, "index.html", {"items": items, "cate": cate, "tags": tags, "search": search})

# Create your views here.

def searchDatabase(request):
    print("Search Database View Accessed")
    if request.method == "POST":
        form = searchForm(request.POST)
        #print(form)
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            selected_categories = form.cleaned_data.get('category')
            selected_tags = form.cleaned_data.get('tags')
            print(selected_categories)
            items = ProductData.objects.all()
            
            if search_query:
                items = items.filter(product_name__icontains=search_query) | items.filter(description__icontains=search_query)
            
            if selected_categories:
                items = items.filter(category__in=selected_categories)
            
            if selected_tags:
                items = items.filter(tags__name__in=selected_tags).distinct()
            
            cate = ProductData.objects.values_list('category', flat=True).distinct()
            tags = Tags.objects.values_list('name', flat=True).distinct()
            search = True
            
            return render(request, "index.html", {"items": items, "cate": cate, "tags": tags, "search": search})
    else:
        form = searchForm()
    
    return render(request, "index.html", {"form": form})