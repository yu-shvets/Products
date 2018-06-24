from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django_filters import rest_framework as filters
from .filters import CustomDateRangeFilter, CurrentDateRangeFilter


class ProductDateFilter(filters.FilterSet):
    added = CustomDateRangeFilter(label='Date created')
    updated = CurrentDateRangeFilter(label='Date updated')

    class Meta:
        model = Product
        fields = ('added', 'updated')


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductDateFilter


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
