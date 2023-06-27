from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm , HomeworkCreateForm
from .models import Post , Homework
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
    success_url = reverse_lazy('homework:homework_list')

class StudentCreateView(generic.CreateView):
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'homework/homework_student.html'
    success_url = reverse_lazy('homework:homework_student')