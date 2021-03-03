from django.contrib import admin

from apps.store.models import Category
from apps.store.models import Product

admin.site.register(Category)
admin.site.register(Product)
