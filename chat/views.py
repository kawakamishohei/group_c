from django.shortcuts import render
from django.views import generic
from .models import Chat
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ChatCreateForm
# Create your views here.
class ChatListView(generic.ListView):
    model = Chat
    template_name = 'chat/chat_list.html'

class ChatDetailView(generic.DetailView):
    model = Chat
    template_name = 'chat/chat_detail.html'

class ChatCreateView(generic.CreateView):
    model = Chat
    template_name = 'chat/chat_create.html'
    success_url = reverse_lazy('chat:chat_list')
    form_class = ChatCreateForm
