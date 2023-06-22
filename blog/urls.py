from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]