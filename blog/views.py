from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import SearchForm, KijiCreateForm, CommentCreateForm, TagCreateForm, KijiUpdateForm
from .models import Kiji, Comment, Tag, Access


class Home(generic.ListView):
    model = Kiji
    template_name = 'blog/home.html'
    queryset = Kiji.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # フォーム(request.GETやrequest.POST)とすると、
        # このフォームをテンプレートで表示すると、入力済みになっている
        context['form'] = SearchForm(self.request.GET)

        Access.objects.get_or_create(id=1, defaults={'access_no': 0})
        q = Access.objects.get(id=1)
        kaisuu = q.access_no + 1
        q.access_no = kaisuu
        q.save()
        access_text = str(kaisuu)
        context['access_text'] = access_text
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            # 記事タイトルか本文のどちらかにキーワードが含まれていれば表示
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(text__icontains=keyword))
        return queryset

    def users(request, user_age, user_username):
        user = get_object_or_404(User, pk=user_age)
        context2 = {
            'user': user,
        }
        # user2 = get_object_or_404(User, pk=user_username)
        # context3 = {
        #     'user2': user2,
        # }
        return context2


class KijiDetailView(generic.DetailView):
    model = Kiji
    template_name = 'blog/kiji_detail.html'

    def get_object(self, queryset=None):
        # self.kwargsは、URL内の int:pkといった部分が入っている
        kiji = Kiji.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # pkというのは、primarykeyのこと。今回ならidフィールドのこと
        return kiji

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kiji = self.get_object()
        context['tags'] = kiji.tags.all()
        return context


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = TagCreateForm


class KijiCreateView(generic.CreateView):
    model = Kiji
    template_name = 'blog/kiji_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = KijiCreateForm


class KijiUpdate(generic.UpdateView):
    model = Kiji
    form_class = KijiUpdateForm
    template_name = 'blog/kiji_update.html'
    success_url = reverse_lazy('blog:home')


class KijiDelete(generic.DeleteView):
    model = Kiji
    template_name = 'blog/kiji_delete.html'
    success_url = reverse_lazy('blog:home')


class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = CommentCreateForm

    def form_valid(self, form):
        # form.save(commit=False) データベースにはまだ保存しない
        # commit=Falseビューで、モデルのフィールドを埋めるために使う引数
        comment = form.save(commit=False)
        # Commentモデルの、targetフィールドをここで埋める
        # モデル名.objects.get(フィールド=値)  1つだけ、DBから取り出すのに使うのがget
        # url内の<int:pk>は、self.kwargs['pk'] で取得できる
        comment.target = Kiji.objects.get(pk=self.kwargs['pk'])
        comment.save()  # saveしないと保存されない
        return redirect('blog:home')

    def get_initial(self):
        initial = {}
        initial['name'] = self.request.user.username
        return initial
# Create your views here.
