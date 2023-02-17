from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    authentication_classes = [#SessionAuthentication,
                              #BasicAuthentication,
                              TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
