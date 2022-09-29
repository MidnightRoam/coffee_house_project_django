
from django.urls import path, include
from django.conf.urls.static import static
from .views import IndexView, OrderView, BlogDetailView, NotFoundPageView, BlogPostsView

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('order/', OrderView.as_view(), name='order'),
    # path('signup/', SignupView.as_view(), name="signup-view"),
    # path('signin/', SigninView.as_view(), name="signin-view"),
    path('404/', NotFoundPageView.as_view(), name='404'),
    path('blog-posts/', BlogPostsView.as_view(), name='blog-posts'),
    path('blog/<slug:blog_slug>/', BlogDetailView.as_view(), name="blog-detail"),
]
