from django.urls import path, include
from rest_framework import routers
from .viewsets.product_viewset import ProductViewSet
from .viewsets.category_viewset import CategoryViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]