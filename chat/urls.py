from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('list/', views.ChatListView.as_view(), name='chat_list'),
]