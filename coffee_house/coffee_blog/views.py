from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from coffee_blog.models import Blog, Order


class IndexView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)[:3]


class OrderView(ListView):
    template_name = 'pages/order.html'
    model = Order
    context_object_name = 'products'

    # def get_queryset(self):
    #     return Product.objects.all()[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Order page'
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'pages/personal_page.html'
    slug_url_kwarg = 'blog_slug'
    context_object_name = 'post_blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog Page"
        return context


class NotFoundPageView(ListView):
    template_name = 'pages/page_404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Not Found 404"
        return context

    def get_queryset(self):
        pass


class BlogPostsView(ListView):
    """Blog posts page view"""
    template_name = 'pages/blog_posts.html'
    model = Blog
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)
