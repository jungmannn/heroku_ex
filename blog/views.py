from django.shortcuts import render#, get_object_or_404, redirect
from .models import Blog

# Create your views here.
def home(request):
    return render(request, 'home.html')
def board(request):
    blogs = Blog.objects
    return render(request, 'board.html', {'blogs' : blogs})