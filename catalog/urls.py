from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryListView, CategoryDetailView, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]

urlpatterns += router.urls



