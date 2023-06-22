from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'blog/home.html'
# Create your views here.
