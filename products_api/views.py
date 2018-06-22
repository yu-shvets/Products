from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django_filters import rest_framework as filters
from datetime import datetime


class CurrentDateRangeFilter(filters.DateRangeFilter):
    options = {
        '': ('Any date', lambda qs, name: qs),
        1: ('Today', lambda qs, name: qs.filter(**{
            '%s__year' % name: datetime.now().year,
            '%s__month' % name: datetime.now().month,
            '%s__day' % name: datetime.now().day
        })),
        }


class ProductDateFilter(filters.FilterSet):
    added = filters.DateRangeFilter(label='Date created')
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
