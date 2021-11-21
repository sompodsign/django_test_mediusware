from django.views import generic
from django.db.models import Q
from django.shortcuts import render
# from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework.response import Response

from product.models import Variant, Product, ProductVariant
from ..serializers import ProductSerializer, ProductVariantSerializer


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
        products = Product.objects.all()
        title = self.request.GET.get('title', '')
        variant = self.request.GET.get('variant', '')
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 999999999)
        date = self.request.GET.get('date', '')
        if title:
            products = products.filter(title__icontains=title)
        elif price_from and price_to:
            products = products.filter(productvariantprice__price__range=(price_from, price_to))
        elif variant:
            products = products.filter(productvariant__variant_title=variant)
        elif date:
            products = products.filter(created_at__gte=date)
            return products
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = Variant.objects.all()
        context['colors'] = ProductVariant.objects.filter()
        return context


class ProductCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer


class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get_queryset(self):
        data = Product.objects.all()
        return data

