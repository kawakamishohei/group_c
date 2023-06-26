from django.shortcuts import render, redirect
from django.views import generic
from .models import Chat, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ChatCreateForm, CommentCreateForm
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

class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    form_class = CommentCreateForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        chat = Chat.objects.get(pk=self.kwargs['pk'])
        comment.target = chat
        form.save()
        return redirect('chat:chat_detail',pk = chat.pk)

class GoodsDelete(generic.DeleteView):
    # フォームは必要なし
    model = Chat
    template_name = 'chat/chat_delete.html'
    success_url = reverse_lazy('chat:chat_list')

