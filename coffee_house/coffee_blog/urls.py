
from django.urls import path, include
from django.conf.urls.static import static
from coffee_blog.views import IndexView, OrderView, BlogDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('order/', OrderView.as_view(), name='order'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog-detail")
]
