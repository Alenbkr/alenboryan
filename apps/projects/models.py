from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='projects'
)

    technologies_used = models.CharField(max_length=255,  null=True, blank=True)

    github_link = models.URLField(max_length=200,  null=True, blank=True)
    demo_link = models.URLField(max_length=200, null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    photo = models.ImageField(upload_to='project_photos/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Проект без названия"


