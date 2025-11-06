from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductData, Tags
from .forms import searchForm

def index(request):
    items = ProductData.objects.distinct().all() # Get all distinct products
    cate = ProductData.objects.values_list('category', flat=True).distinct() # Get distinct categories
    tags = Tags.objects.values_list('name', flat=True).distinct() # Get distinct tags
    search = False
    return render(request, "index.html", {"items": items, "cate": cate, "tags": tags, "search": search})

# Create your views here.

def searchDatabase(request):
    print("Search Database View Accessed")
    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query') # Get the search query
            selected_categories = form.cleaned_data.get('category') # Get selected categories
            selected_tags = form.cleaned_data.get('tags') # Get selected tags
            items = ProductData.objects.all()
            
            if search_query:
                items = items.filter(product_name__icontains=search_query) | items.filter(description__icontains=search_query) #filter with or statement looking through name and description
            
            if selected_categories:
                items = items.filter(category__in=selected_categories) #filter by selected categories
            
            if selected_tags:
                items = items.filter(tags__name__in=selected_tags).distinct() #filter by selected tags
            
            cate = ProductData.objects.values_list('category', flat=True).distinct()
            tags = Tags.objects.values_list('name', flat=True).distinct()
            search = True
            
            return render(request, "index.html", {"items": items, "cate": cate, "tags": tags, "search": search}) # returns filtered items
    else:
        form = searchForm()
    
    return render(request, "index.html", {"form": form})