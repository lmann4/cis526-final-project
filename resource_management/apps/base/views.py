from django.views import generic

from apps.inventory.models import Category


class NavbarMixin:
    def get_categories(self, **kwargs):
        categories = Category.objects.all()
        print(categories)
        return categories


class Index(generic.TemplateView, NavbarMixin):
    template_name = 'base/index.html'

    def get_categories(self, **kwargs):
        categories = Category.objects.all()
        print(categories)
        return categories
