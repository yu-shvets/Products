from django.contrib import admin
from django.conf.urls import url
from products_api.views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    url(r'^api/products/create/$', ProductListCreate.as_view()),
    url(r'^api/products/update/(?P<pk>[0-9]+)/$', ProductRetrieveUpdateDestroy.as_view()),
    url(r'^api/products/delete/(?P<pk>[0-9]+)/$', ProductRetrieveUpdateDestroy.as_view()),

    url(r'^admin/', admin.site.urls),
]
