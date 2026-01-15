from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='project_photos/', null=True, blank=True)
    technologies_used = models.CharField(max_length=255)
    demo_link = models.URLField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Project(models.Model):
    # Старые поля
    name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    technologies_used = models.CharField(max_length=255, null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)
    demo_link = models.URLField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='project_photos/', null=True, blank=True)
    
    # Новые поля
    title = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        # Показываем сначала title, если нет — name
        return self.title if self.title else self.name

