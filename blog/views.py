from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import SearchForm, ArticleCreateForm, CommentCreateForm, TagCreateForm, ArticleUpdateForm
from .models import Article, Comment, Tag


class Home(generic.ListView):
    model = Article
    template_name = 'blog/home.html'
    queryset = Article.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # フォーム(request.GETやrequest.POST)とすると、
        # このフォームをテンプレートで表示すると、入力済みになっている
        context['form'] = SearchForm(self.request.GET)
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


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = TagCreateForm


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = ArticleCreateForm


class ArticleUpdate(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:home')

class ArticleDelete(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
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
        comment.target = Article.objects.get(pk=self.kwargs['pk'])

        comment.save()  # saveしないと保存されない
        return redirect('blog:home')
# Create your views here.
