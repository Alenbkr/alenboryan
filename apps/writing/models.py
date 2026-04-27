from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title  = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='blog'
)
    created_at = models.DateTimeField(auto_now_add=True)