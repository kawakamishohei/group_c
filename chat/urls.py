from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('list/', views.ChatListView.as_view(), name='chat_list'),
    path('create/', views.ChatCreateView.as_view(), name='chat_create'),
    path('detail/<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    path('comment/create/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('delete/<int:pk>/', views.GoodsDelete.as_view(), name='chat_delete')
]