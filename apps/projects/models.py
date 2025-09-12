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