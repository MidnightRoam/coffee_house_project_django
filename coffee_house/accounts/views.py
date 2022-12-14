from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from coffee_blog.models import Order


class SignUpView(CreateView):
    """User registration logic"""
    form_class = UserRegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:signin')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "* Please enter the valid data")
        return redirect('accounts:signup')


class SignInView(View):
    """User login logic"""
    form_class = UserLoginForm
    template_name = 'accounts/signin.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username, password=password)

                if user and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('index-view'))
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "* Username or password incorrect")

        form = UserLoginForm()
        return render(request, "accounts/signin.html", {"form": form})


# class ProfileView(ListView):
#     """User personal profile view"""
#     template_name = 'accounts/profile.html'
#
#     def post(self, request):
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('accounts:profile-view'))
#
#     # def get(self, request):
#     #     form = UserProfileForm(instance=request.user)
#     #     return form
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = UserProfileForm()
#         return context
#
#     def get_queryset(self):
#         pass


@login_required(login_url='/accounts/signin')
def profile(request, count=15):
    """User profile view"""
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile-view'))
        else:
            print(form.errors.as_data())
    else:
        form = UserProfileForm(instance=request.user)
    user_orders = Order.objects.filter(user=request.user).order_by("-id")[:count]
    context = {'form': form,
               'orders': user_orders}
    return render(request, 'accounts/profile.html', context)
