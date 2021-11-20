from django.views import generic
from django.shortcuts import render

from product.models import Variant, Product


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/list.html'
    paginate_by = 10
    ordering = ['-price']

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 100000000)
        new_context = Product.objects.filter(
            title__icontains=title,
            productvariantprice__price__lt=price_from,
        )
        return new_context
