from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Test(TemplateView):
    template_name = 'timetable/test.html'