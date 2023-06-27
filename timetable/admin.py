from django.contrib import admin
from timetable.models import Timetable, Subject

# Register your models here.
admin.site.register(Timetable)
# admin.site.register(Lunchmenu)
admin.site.register(Subject)