from django.shortcuts import render
from .models import Project

from django.views.generic import ListView, DetailView

from django.views.generic import ListView, DetailView, CreateView


class ProjectListView(ListView):
    model = Project
    template_name = "projects/projects.html"  
    context_object_name = "projects"  
    ordering = ["-start_date"]  


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"  
    context_object_name = "project"
    




from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProjectForm




class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
