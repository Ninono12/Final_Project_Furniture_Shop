from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView,
    ProductViewSet
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('', include(router.urls)),
]


