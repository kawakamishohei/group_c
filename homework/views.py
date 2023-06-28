from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm , HomeworkCreateForm
from .models import Post , Homework
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST

class IndexView(generic.TemplateView):
    template_name = 'homework/homework.html'
    success_url = reverse_lazy('homework:homework')
    model = Post

class PostListView(generic.ListView):
    model = Post
    template_name = 'homework/homework_list.html'
    success_url = reverse_lazy('homework:homework_list')

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'homework/homework_create.html'
    success_url = reverse_lazy('homework:homework_list')

class StudentCreateView(generic.CreateView):
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'homework/homework_student.html'
    success_url = reverse_lazy('homework:homework_teacher')

class TeacherListView(generic.ListView):
    model = Homework
    template_name = 'homework/homework_teacher.html'
    success_url = reverse_lazy('homework:homework_teacher')
