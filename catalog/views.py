from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from .models import Product
from .serializers import ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.GET.get('category')
        color = self.request.GET.get('color')
        material = self.request.GET.get('material')

        if category:
            queryset = queryset.filter(category_id=category)
        if color:
            queryset = queryset.filter(color=color)
        if material:
            queryset = queryset.filter(material=material)

        return queryset

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer