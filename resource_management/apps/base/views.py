from django.views import generic

from apps.inventory.models import Category


class NavbarMixin(generic.View):
    def get_context_data(self, **kwargs):
        context = super(NavbarMixin, self).get_context_data(**kwargs)
        context['inventory_types'] = Category.objects.values_list('name')
        return context


class Index(generic.TemplateView, NavbarMixin):
    template_name = 'base/index.html'
