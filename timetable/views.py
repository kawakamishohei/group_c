from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Timetable, Subject
from .forms import TimetableCreateForm, SubjectCreateForm, TimetableUpdateForm, TimetableSearchForm, YearMonthForm

# class Test(TemplateView):
#     template_name = 'timetable/test.html'

class TimetableCreateView(CreateView):
    model = Timetable
    template_name = 'timetable/timetable_create.html'
    success_url = reverse_lazy('timetable:timetable_list')
    form_class = TimetableCreateForm

# class TimetableListView(ListView):
#     model = Timetable
#     template_name = 'timetable/timetable_list.html'
#     form_class = TimetableSearchForm
#     paginate_by = 30

    # #検索機能とページング機能の搭載
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = TimetableSearchForm(self.request.GET)
    #     return context
    #
    # def get_queryset(self):
    #     # 絞り込みのために上書き
    #     queryset = super().get_queryset()
    #
    #     # GETパラメータを、フォームに紐づける
    #     form = TimetableSearchForm(self.request.GET)
    #     form.is_valid()  # フォームからデータを取り出すのに必要な行
    #
    #     # 値 = フォームオブジェクト.cleaned_data.get('フィールド名')
    #     day = form.cleaned_data.get('day')
    #     if day:
    #         # .filter(フィールド名=値)
    #         queryset = queryset.filter(day=day)
    #     return queryset

#     def get(self, request, *args, **kwargs):
#
#         context = {}
#
#         form = YearMonthForm(request.GET)
#         if form.is_valid():
#             cleaned = form.clean()
#
#             context["topics"] = Timetable.objects.filter(day__year=cleaned["year"], day__month=cleaned["month"]).order_by(
#                 "-day")
#         else:
#             context["timetable"] = Timetable.objects.order_by("-day")
#
#         # 月別アーカイブの表示
#         # 最新と最古のデータを手に入れる。
#         newest = Timetable.objects.order_by("-day").first()
#         oldest = Timetable.objects.order_by("day").first()
#
#         year_month_list = []
#
#         if newest and oldest:
#
#             newest_day = newest.day
#             now_year = oldest.day.year
#             now_month = oldest.day.month
#
#             # 最古から1ヶ月ずつずらして最新になったら終わり
#             while True:
#                 year_month = {}
#                 year_month["link"] = "?year=" + str(now_year) + "&month=" + str(now_month)
#                 year_month["label"] = str(now_year) + "年" + str(now_month) + "月"
#
#                 copied = year_month.copy()
#
#                 year_month_list.append(copied)
#
#                 if now_month >= newest_day.month and now_year >= newest_day.year:
#                     break
#                 else:
#                     if now_month == 12:
#                         now_year += 1
#                         now_month = 1
#                     else:
#                         now_month += 1
#
#         context["year_month_list"] = year_month_list
#
#         return render(request, "timetable/timetable_list.html", context)
#
#     def post(self, request, *args, **kwargs):
#
#         form = TimetableUpdateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#         print(form.errors)
#
#         return redirect("timetable:timetable_list")
#
# index = TimetableListView.as_view()

class TimetableView(View):
    model = Timetable
    template_name = 'timetable/timetable_list.html'
    form_class = TimetableSearchForm
    paginate_by = 30

    # #検索機能とページング機能の搭載
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = TimetableSearchForm(self.request.GET)
    #     return context
    #
    # def get_queryset(self):
    #     # 絞り込みのために上書き
    #     queryset = super().get_queryset()
    #
    #     # GETパラメータを、フォームに紐づける
    #     form = TimetableSearchForm(self.request.GET)
    #     form.is_valid()  # フォームからデータを取り出すのに必要な行
    #
    #     # 値 = フォームオブジェクト.cleaned_data.get('フィールド名')
    #     day = form.cleaned_data.get('day')
    #     if day:
    #         # .filter(フィールド名=値)
    #         queryset = queryset.filter(day=day)
    #     return queryset

    def get(self, request, *args, **kwargs):

        context = {}

        form = YearMonthForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()

            context["timetable"] = Timetable.objects.filter(day__year=cleaned["year"], day__month=cleaned["month"]).order_by(
                "-day")
        else:
            context["timetable"] = Timetable.objects.order_by("-day")

        # 月別アーカイブの表示
        # 最新と最古のデータを手に入れる。
        newest = Timetable.objects.order_by("-day").first()
        oldest = Timetable.objects.order_by("day").first()

        year_month_list = []

        if newest and oldest:

            newest_day = newest.day
            now_year = oldest.day.year
            now_month = oldest.day.month

            # 最古から1ヶ月ずつずらして最新になったら終わり
            while True:
                year_month = {}
                year_month["link"] = "?year=" + str(now_year) + "&month=" + str(now_month)
                year_month["label"] = str(now_year) + "年" + str(now_month) + "月"

                copied = year_month.copy()

                year_month_list.append(copied)

                if now_month >= newest_day.month and now_year >= newest_day.year:
                    break
                else:
                    if now_month == 12:
                        now_year += 1
                        now_month = 1
                    else:
                        now_month += 1

        context["year_month_list"] = year_month_list

        return render(request, "timetable/timetable_list.html", context)

    def post(self, request, *args, **kwargs):

        form = TimetableCreateForm(request.POST)

        if form.is_valid():
            form.save()

        print(form.errors)

        return redirect("timetable:timetable_list")

index = TimetableView.as_view()

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




