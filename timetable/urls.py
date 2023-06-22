from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns =[
    path('test/', views.Test.as_view(), name='test')
]