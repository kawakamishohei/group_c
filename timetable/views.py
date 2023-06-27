from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Timetable, Subject
from .forms import TimetableCreateForm, SubjectCreateForm, TimetableUpdateForm

# class Test(TemplateView):
#     template_name = 'timetable/test.html'

class TimetableCreateView(CreateView):
    model = Timetable
    template_name = 'timetable/timetable_create.html'
    success_url = reverse_lazy('timetable:timetable_list')
    form_class = TimetableCreateForm

class TimetableListView(ListView):
    model = Timetable
    template_name = 'timetable/timetable_list.html'

class TimetableDeleteView(DeleteView):
    model = Timetable
    template_name = 'timetable/timetable_delete.html'
    success_url = reverse_lazy('timetable:timetable_list')

class TimetableDetailView(DetailView):
    model = Timetable
    template_name = 'timetable/timetable_detail.html'

class TimetableUpdateView(UpdateView):
    model = Timetable
    form_class = TimetableUpdateForm
    template_name = 'timetable/timetable_update.html'
    success_url = reverse_lazy('timetable:timetable_list')

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'timetable/subject_create.html'
    success_url = reverse_lazy('timetable:subject_list')
    form_class = SubjectCreateForm

class SubjectListView(ListView):
    model = Subject
    template_name = 'timetable/subject_list.html'

class LunchmenuDetailview(DetailView):
    model = Timetable
    template_name = 'timetable/lunchmenu_detail.html'
#
# class LunchmenuCreateView(CreateView):
#     model = Lunchmenu
#     form_class = LunchmenuCreateForm
#     template_name = 'timetable/lunchmenu_create.html'
#     success_url = reverse_lazy('timetable:lunchmenu_list')
#
#     # def form_valid(self, form):
#     #     lunchmenu = form.save(commit=False)  # データベースには保存しない
#     #     lunchmenu.target = Timetable.objects.get(pk=self.kwargs['pk'])
#     #     lunchmenu.save()
#     #     return redirect('timetable:lunchmenu_create')
#
# class LunchmenuListView(ListView):
#     model = Lunchmenu
#     template_name = 'timetable/Lunchmenu_list.html'




