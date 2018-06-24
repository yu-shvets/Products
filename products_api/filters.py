from django_filters import rest_framework as filters
from datetime import datetime, timedelta


class CustomDateRangeFilter(filters.DateRangeFilter):
    options = {
        '': ('Any date', lambda qs, name: qs),
        1: ('Today', lambda qs, name: qs.filter(**{
            '%s__year' % name: datetime.now().year,
            '%s__month' % name: datetime.now().month,
            '%s__day' % name: datetime.now().day
        })),
        2: ('Last 3 days', lambda qs, name: qs.filter(**{
            '%s__gte' % name: datetime.now() - timedelta(days=3),
            '%s__lt' % name: datetime.now(),
        })),
        3: ('Last week', lambda qs, name: qs.filter(**{
            '%s__gte' % name: datetime.now() - timedelta(days=7),
            '%s__lt' % name: datetime.now(),
        })),
        }


class CurrentDateRangeFilter(filters.DateRangeFilter):
    options = {
        '': ('Any date', lambda qs, name: qs),
        1: ('Today', lambda qs, name: qs.filter(**{
            '%s__year' % name: datetime.now().year,
            '%s__month' % name: datetime.now().month,
            '%s__day' % name: datetime.now().day
        })),
        }