from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from.models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import BlogForm
class BlogListView(ListView):
    model = Blog
    template_name ="writing/blog.html"
    context_object_name  = "blog"
    ordering = ["-start_date"]
    
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "writing/blog_detail.html"  
    context_object_name = "project"
    
   

class BlogCreateView(LoginRequiredMixin, CreateView): 
    model = Blog
    form_class = BlogForm
    template_name = 'writing/blog.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
