from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductListView, ProductCreateView, ProductUpdateView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(), name='list.product'),
    path('', ProductCreateView.as_view(), name='product.create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product.update'),
]



