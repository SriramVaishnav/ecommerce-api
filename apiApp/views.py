from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductListSerializer, CategoryListSerializer, ProductDetailSerializer
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        serializer = CategoryListSerializer(category)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)
