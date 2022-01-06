from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class comment(models.Model):
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.comments




class blogs(models.Model):
    btitle = models.CharField(max_length=200)
    bdate = models.DateTimeField(default=timezone.now())
    btext = models.TextField(max_length=500)
    bautor = models.ForeignKey(User, verbose_name=("author_id"), on_delete=models.CASCADE)
    comment = models.ManyToManyField(comment)

    def __str__(self):
        return self.btitle


    class Meta:
        ordering = ['-bdate']

    def get_absolute_url(self):
        return reverse("model_detail_view", args=[str(self.id)])



