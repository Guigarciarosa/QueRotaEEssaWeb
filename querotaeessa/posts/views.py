from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.

def homepage(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request,"posts/homepage.html", {'posts':posts})
    