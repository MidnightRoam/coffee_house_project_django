from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import ListView, CreateView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


class SignUpView(ListView):
    """User registration logic"""
    form = UserRegistrationForm()
    template_name = 'accounts/signup.html'

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('accounts:signin'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserRegistrationForm()
        return context

    def get_queryset(self):
        pass


class SignInView(ListView):
    """User login logic"""
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


# class ProfileView(ListView):
#     """User personal profile view"""
#     template_name = 'accounts/profile.html'
#
#     def get(self, request):
#         return UserProfileForm(instance=request.user)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = UserProfileForm()
#         return context
#
#     def get_queryset(self):
#         pass


@login_required(login_url='/accounts/signin')
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile-view'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)
