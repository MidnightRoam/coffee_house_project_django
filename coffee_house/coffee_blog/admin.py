from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe

from .models import Blog, Order, Product, ProductCategory

admin.site.register(Order)
admin.site.register(ProductCategory)

class BlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ("title", "is_published", "created_at", "updated_at", "get_blog_image")
    list_filter = ("is_published", "created_at", "updated_at")
    list_editable = ['is_published']
    search_fields = ["title"]

    def get_blog_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_blog_image.short_description = "Post image"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "category")


admin.site.site_title = "Coffee House"
admin.site.site_header = "Coffee House | Administration"
