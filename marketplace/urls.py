from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),

    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'remove-from-cart/<int:cart_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'my-orders/',
        views.my_orders,
        name='my_orders'
    ),

    path(
        'seller-dashboard/',
        views.seller_dashboard,
        name='seller_dashboard'
    ),

    path(
        'edit-product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
    path(
        'confirm-order/<int:order_id>/',
        views.confirm_order,
        name='confirm_order'
    ),

    path(
        'complete-order/<int:order_id>/',
        views.complete_order,
        name='complete_order'
    ),

    path(
        'add-review/<int:order_id>/',
        views.add_review,
        name='add_review'
    ),
    path(
        'notifications/',
        views.notifications,
        name='notifications'
    ),
    path(
        'cancel-order/<int:order_id>/',
        views.cancel_order,
        name='cancel_order'
    ),
    path(
        'missed-pickup/<int:order_id>/',
        views.missed_pickup,
        name='missed_pickup'
    ),
    path(
        'buy-now/<int:product_id>/',
        views.buy_now,
        name='buy_now'
    ),
]