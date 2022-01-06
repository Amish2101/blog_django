from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import blogs
from django.views import generic
from django.utils import timezone

# Create your views here.

class homepage(generic.ListView):
    template_name = 'blogs/index.html'

    def get_queryset(self):
        return blogs.objects.filter(
            bdate__lte = timezone.now()
        ).order_by('-bdate')[:5]


class blogspage(generic.ListView):
    template_name = 'blogs/blogs.html'
    context_object_name = 'data'

    def get_queryset(self):
        return blogs.objects.filter(bdate__lte=timezone.now())

class detailspage(generic.DetailView):
    template_name = 'blogs/details.html'
    context_object_name = 'data'

    def get_queryset(self):
        return blogs.objects.all()

class blogger(generic.ListView):
    template_name = 'blogs/blogger.html'
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.all()

class bloggerdetails(generic.DetailView):
    template_name = 'blogs/bloggerdetails.html'
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.all()

    
