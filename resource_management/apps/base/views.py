from django.views import generic

from apps.inventory.models import Category


class NavbarMixin:
    def categories(self):
        return Category.objects.all()


class Index(generic.TemplateView, NavbarMixin):
    template_name = 'base/index.html'
