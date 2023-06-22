from django.shortcuts import render
from django.views import generic
from .models import Chat
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class ChatListView(generic.ListView):
    model = Chat
    template_name = 'chat/chat_list.html'