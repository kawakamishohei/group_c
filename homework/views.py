from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post
from django.views.generic import TemplateView

class IndexView(generic.TemplateView):
    template_name = 'homework/homework.html'
    success_url = reverse_lazy('homework:homework')
    model = Post

class PostListView(generic.ListView):
    template_name = 'homework/homework_list.html'
    success_url = reverse_lazy('homework:homework_list')
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'homework/homework_create.html'
    success_url = reverse_lazy('homework:homework_create')