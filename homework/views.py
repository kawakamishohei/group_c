from django.shortcuts import render
from django.views import generic

class homeworkListView(generic.ListView):
    templates_name = 'homework/homework_list.html'
# Create your views here.
