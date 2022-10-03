from django.urls import path, include
from .views import IndexView, OrderView, BlogDetailView, NotFoundPageView, BlogPostsView, StoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('order/', OrderView.as_view(), name='order'),
    path('404/', NotFoundPageView.as_view(), name='404'),
    path('story/', StoryView.as_view(), name='story-view'),
    path('blog-posts/', BlogPostsView.as_view(), name='blog-posts'),
    path('blog/<slug:blog_slug>/', BlogDetailView.as_view(), name="blog-detail"),
]
