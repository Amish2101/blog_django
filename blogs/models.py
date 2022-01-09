from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.


class author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=500)

    # def get_absolute_url(self):
    #     return reverse('bloggerdetails', args=[str(self.id)])
    
    def __str__(self):
        return self.user.username


class blogs(models.Model):
    btitle = models.CharField(max_length=200, default= True)
    bdate = models.DateTimeField(default=timezone.now())
    btext = models.TextField(max_length=500, default= True)
    user = models.ForeignKey(author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.btitle


    class Meta:
        ordering = ['-bdate']

    # def get_absolute_url(self):
    #     return reverse('bloggerdetails', args=[str(self.id)])

class comment(models.Model):
    comments = models.TextField(max_length=500, null= True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # post_date = models.DateTimeField()
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, default=True )
    
    def __str__(self):
        return self.comments
        
    # class Meta:
    #     ordering = ["-post_date"]

    def __str__(self):
        title_limit = 75
        if len(self.comments) > title_limit:
            tstring = self.comments[:title_limit]
        else:
            tstring = self.comments
        return tstring





