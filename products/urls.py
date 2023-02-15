from django.urls import path, include
from rest_framework import routers
from .viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]