from rest_framework import serializers
from .models import Product, Category

class ProductListSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug', 'image']

class ProductDetailSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id', 'name',  'description', 'price', 'slug', 'image']

class CategoryListSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'slug']

class CategoryDetailSerializer(serializers.Serializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'products']