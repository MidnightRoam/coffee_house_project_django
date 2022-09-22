from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from coffee_blog.models import Blog, Order


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)[:3]


class OrderView(ListView):
    template_name = 'order.html'
    model = Order


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'personal_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog Page"
        return context

