from typing import ParamSpecKwargs
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import author, blogs, comment
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def homepage(request):
    return render(request, 'blogs/index.html')



class blogspage(generic.ListView):
    model = blogs
    paginate_by = 5
    # template_name = 'blogs/blogs.html'
    # context_object_name = 'data'

    # def get_queryset(self):
    #     return blogs.objects.filter(bdate__lte=timezone.now())

class detailspage(generic.DetailView):
    model = blogs
    # template_name = 'blogs/details.html'
    # context_object_name = 'data'

    # def get_queryset(self):
    #     return blogs.objects.filter(bautor = id)

class blogger(generic.ListView):
    model = author
    paginate_by = 5
    # template_name = 'blogs/blogger.html'
    # context_object_name = 'user'

    # def get_queryset(self):
    #     return User.objects.all()


class bloggerdetails(generic.ListView):
    model = blogs
    paginate_by = 5
    template_name = 'blogs/bloggerdetails.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(author, pk = id)
        return blogs.objects.filter(user=target_author)

    def get_context_data(self, **kwargs):
        context = super(bloggerdetails, self).get_context_data(**kwargs)
        context["user"] = get_object_or_404(author, pk = self.kwargs['pk']) 
        return context
    
    

# def bloggerdetails(request, pk):
#     print("this is a pk key value" ,pk)
#     users = get_object_or_404(User,id=pk)
#     print(users)
#     user = blogs.objects.filter(bautor = pk)
#     print(user)
#     return render(request, 'blogs/bloggerdetails.html', {'user':user, 'users':users})


class blogcomment(LoginRequiredMixin, CreateView):
    model = comment
    fields = ['comment',]

    def get_context_data(self, **kwargs):
        context = super(blogcomment, self).get_context_data(**kwargs)
        context["blog"] = get_object_or_404(blogs, pk = self.kwargs['pk']) 
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.blog = get_object_or_404(blogs, pk = self.kwargs['pk'])
        return super(blogcomment, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.kwargs['pk'],})