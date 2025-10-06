from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView

class ProjectListView(ListView):
    model = Project
    template_name = "projects/projects.html"  
    context_object_name = "projects"  
    ordering = ["-start_date"]  


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"  
    context_object_name = "project"
    


