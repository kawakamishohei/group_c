from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('homework', views.homeworkListView.as_view(), name='homework'),

]