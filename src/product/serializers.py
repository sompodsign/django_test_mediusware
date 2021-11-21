from rest_framework import serializers
from .models import Product, Variant, ProductVariant, ProductVariantPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True)
    product = ProductSerializer

    class Meta:
        model = ProductVariant
        fields = ['variant_title']


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    product_variant_one = ProductVariantSerializer
    product_variant_two = ProductVariantSerializer
    product_variant_three = ProductVariantSerializer

    class Meta:
        model = ProductVariantPrice
        fields = ['price', 'stock']
