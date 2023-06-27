from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    path('tag/create/', login_required(views.TagCreateView.as_view()), name='tag_create'),
    path('kiji/create/', login_required(views.KijiCreateView.as_view()), name='kiji_create'),
    path('kiji/detail/<int:pk>', login_required(views.KijiDetailView.as_view()), name='kiji_detail'),
    path('kiji_update/<int:pk>/', login_required(views.KijiUpdate.as_view()), name='kiji_update'),
    path('kiji_delete/<int:pk>/',login_required(views.KijiDelete.as_view()), name='kiji_delete'),
    path('comment/create/<int:pk>',login_required(views.CommentCreateView.as_view()), name='comment_create'),
]