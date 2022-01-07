from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('/', views.homepage, name='home' ),
    path('/blogs/', views.blogspage.as_view(), name='blogspages'),
    path('/blog/<int:pk>/', views.detailspage.as_view(), name='details'),
    path('/blogger/', views.blogger.as_view(), name='blogger'),
    path('/blogger/<int:pk>', views.bloggerdetails.as_view(), name='bloggerdetails'),
    path('/blog/', views.blogcomment.as_view(), name="blogcomment")
]
