from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import homework

class homeworkListView(generic.ListView):
    templates_name = 'homework/homework_list.html'
    model = homework

