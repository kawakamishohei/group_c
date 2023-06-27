from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'timetable'

urlpatterns =[
    # path('test/', views.Test.as_view(), name='test'),
    path('timetable_create/', views.TimetableCreateView.as_view(), name='timetable_create'),
    path('timetable_list/', views.TimetableListView.as_view(), name='timetable_list'),
    path('timetable_detail/<int:pk>/', views.TimetableDetailView.as_view(), name='timetable_detail'),
    path('timetable_delete/<int:pk>/', views.TimetableDeleteView.as_view(), name='timetable_delete'),
    path('timetable_update/<int:pk>/', views.TimetableUpdateView.as_view(), name='timetable_update'),
    path('subject_create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject_list/', views.SubjectListView.as_view(), name='subject_list'),
    # path('lunchmenu_create/', views.LunchmenuCreateView.as_view(), name='lunchmenu_create'),
    # path('lunchmenu_create/<int:pk>', views.LunchmenuCreateView.as_view(), name='lunchmenu_create'),
    # path('lunchmenu_list/', views.LunchmenuListView.as_view(), name='lunchmenu_list'),
    path('lunchmenu_detail/<int:pk>/', views.LunchmenuDetailview.as_view(), name='lunchmenu_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)