from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
