from rest_framework.viewsets import ModelViewSet

from products.models import Category
from products.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()