from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage
from apps.core.views import contact, about
from apps.store.views import product_detail, category_detail

from apps.cart.views import cart_detail

from apps.store.api import api_add_to_cart

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('cart/', cart_detail, name='cart'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),

    # api

    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),

    # store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),

]
