from django.views import generic
from django.urls import reverse_lazy
from .forms import MyUserCreationForm
from .models import CustomUser  # importsuru
from django.contrib.auth.views import LoginView, LogoutView


class AccountCreateView(generic.CreateView):
    Model = CustomUser  # カスタムユーザーにする
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    # next_page = '/accounts/login/'
    # ログアウト後に、移動するページ
    next_page = reverse_lazy('accounts:login')


class Clear(generic.TemplateView):
    template_name = 'accounts/clear.html'



# Create your views here.
