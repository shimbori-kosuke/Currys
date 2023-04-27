from .forms import UserModelForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    form_class = UserModelForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/index.html'