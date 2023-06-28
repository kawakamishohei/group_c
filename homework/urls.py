from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('homework', views.IndexView.as_view(), name='homework'),
    path('homework_list/', views.PostListView.as_view(), name='homework_list'),
    path('homework_create/', views.PostCreateView.as_view(), name='homework_create'),
    path('homework_student/', views.StudentCreateView.as_view(), name='homework_student'),
    path('homework_teacher/', views.TeacherListView.as_view(), name='homework_teacher'),

]

