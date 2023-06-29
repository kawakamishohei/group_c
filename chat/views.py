from django.shortcuts import render, redirect
from django.views import generic
from .models import Chat, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ChatCreateForm, CommentCreateForm, SearchForm
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
class ChatListView(generic.ListView):
    model = Chat
    template_name = 'chat/chat_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        form = SearchForm(self.request.GET)
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            queryset = queryset.filter(
                # 記事のタイトルか、本文のどちらかにキーワードが含まれているものを絞り込む
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


class ChatDetailView(generic.CreateView):
    model = Chat
    template_name = 'chat/chat_detail.html'
    form_class = CommentCreateForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        chat = Chat.objects.get(pk=self.kwargs['pk'])
        comment.target = chat
        form.save()
        return redirect('chat:chat_detail', pk=chat.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = Chat.objects.get(pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        initial = {}
        initial['name'] = self.request.user.username
        return initial


class ChatCreateView(generic.CreateView):
    model = Chat
    template_name = 'chat/chat_create.html'
    success_url = reverse_lazy('chat:chat_list')
    form_class = ChatCreateForm

    def get_initial(self):
        initial = {}
        initial['upname'] = self.request.user.username
        return initial

class ChatDelete(generic.DeleteView):
    # フォームは必要なし
    model = Chat
    template_name = 'chat/chat_delete.html'
    success_url = reverse_lazy('chat:chat_list')

