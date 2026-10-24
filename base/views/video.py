from django.shortcuts import render
from ..models import Category  # Import the Category model from one directory up

def video_page(request):
    categories = Category.objects.prefetch_related('videos').all()  # Fetch categories with videos
    return render(request, 'base/video_page.html', {'categories': categories})

def doubt_corner(request):
    return render(request, 'base/doubt_corner.html') 