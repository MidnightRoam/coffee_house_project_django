from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from .forms import UserLoginForm, UserRegistrationForm


class SignUpView(ListView):
    form = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def get_queryset(self):
        pass


class SignInView(ListView):
    """User authorization logic"""
    template_name = 'accounts/signin.html'

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index-view'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserLoginForm()
        return context

    def get_queryset(self):
        pass


class ProfileView(ListView):
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        pass
