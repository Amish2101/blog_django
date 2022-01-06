from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('/', views.homepage.as_view(), name='home' ),
    path('/blogs/', views.blogspage.as_view(), name='blogspages'),
    path('/blogs/<int:pk>/', views.detailspage.as_view(), name='details'),
    path('/blogger/', views.blogger.as_view(), name='blogger'),
    path('/blogger/details/<int:pk>', views.bloggerdetails.as_view(), name='bloggerdetails'),
]
