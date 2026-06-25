from django.contrib import admin
from .models import Product, CartItem
from .models import Product, CartItem, Order, Review, Notification
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Notification)