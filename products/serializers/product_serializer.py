from rest_framework import serializers

from products.models import Product
from products.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product

    fields = ['title', 'description', 'price', 'active', 'category']
