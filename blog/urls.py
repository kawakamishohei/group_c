from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('kiji/create/', views.KijiCreateView.as_view(), name='kiji_create'),
    path('kiji/detail/<int:pk>', views.KijiDetailView.as_view(), name='kiji_detail'),
    path('kiji_update/<int:pk>/', views.KijiUpdate.as_view(), name='kiji_update'),
    path('kiji_delete/<int:pk>/',views.KijiDelete.as_view(), name='kiji_delete'),
    path('comment/create/<int:pk>',views.CommentCreateView.as_view(), name='comment_create'),
]