from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_active', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description', 'price', 'stock',
            'is_available', 'featured', 'color', 'material',
            'main_image', 'image2', 'image3', 'image4',
            'created_at', 'updated_at'
        ]
