from django.urls import path

from .views import SignUpView, SignInView, profile

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('profile/', profile, name="profile-view"),
]