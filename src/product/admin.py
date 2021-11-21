from django.contrib import admin
from product.models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'get_price')

    def get_price(self, obj):
        return obj

    # get_price.price = 'Price'  # Renames column head

    # Filtering on side - for some reason, this works
    # list_filter = ['title', 'author__name']


admin.site.register(Product, ProductAdmin)
