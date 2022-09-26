
from django.urls import path, include
from django.conf.urls.static import static
from .views import IndexView, OrderView, BlogDetailView, ProfileView, SignupView, SigninView


urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('order/', OrderView.as_view(), name='order'),
    path('profile/', ProfileView.as_view(), name="profile-view"),
    path('signup/', SignupView.as_view(), name="signup-view"),
    path('signin/', SigninView.as_view(), name="signin-view"),
    path('<slug:blog_slug>/', BlogDetailView.as_view(), name="blog-detail"),
]
