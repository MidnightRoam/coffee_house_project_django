from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView

from coffee_blog.models import Blog, Order


class IndexView(ListView):
    """Home page view"""
    template_name = 'pages/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)[:3]


@method_decorator(login_required(login_url="/accounts/signin"), name='dispatch')
class OrderView(ListView):
    """Order page view"""
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
    """Personal page of blog view"""
    model = Blog
    template_name = 'pages/personal_page.html'
    slug_url_kwarg = 'blog_slug'
    context_object_name = 'post_blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog Page"
        return context


class BlogPostsView(ListView):
    """Blog posts page view"""
    template_name = 'pages/blog_posts.html'
    model = Blog
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class NotFoundPageView(TemplateView):
    """404 page view"""
    template_name = 'pages/page_404.html'


class StoryView(TemplateView):
    """Story page view"""
    template_name = 'pages/story_page.html'

