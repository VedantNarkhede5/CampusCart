from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product, CartItem, Order, Review, Notification
from .forms import ProductForm, ReviewForm
from django.db.models import Sum
from django.db.models import Avg
from .models import Product, CartItem, Order, Review
from .forms import ConfirmOrderForm
from .recommendation import get_home_recommendations

@login_required
def add_product(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.seller = request.user

            product.save()

            return redirect('/home/')

    else:

        form = ProductForm()

    return render(
        request,
        "add_product.html",
        {"form": form}
    )

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    average_rating = Review.objects.filter(
        seller=product.seller
    ).aggregate(
        Avg('rating')
    )['rating__avg']

    recommendations = get_home_recommendations(
        product.id
    )
    

    return render(
        request,
        "product_detail.html",
        {
            "product": product,
            "average_rating": average_rating,
            "recommendations": recommendations
        }
    )


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if product.seller == request.user:
        return redirect(
            f'/product/{product.id}/'
        )

    CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('/cart/')


@login_required
def cart(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items
        }
    )

@login_required
def remove_from_cart(request, cart_id):

    cart_item = get_object_or_404(
        CartItem,
        id=cart_id,
        user=request.user
    )

    cart_item.delete()

    return redirect('/cart/')

@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        payment_method = request.POST.get(
            "payment_method"
        )

        for item in cart_items:

            Order.objects.create(
                buyer=request.user,
                seller=item.product.seller,
                product=item.product,
                payment_method=payment_method
            )

            Notification.objects.create(
                user=item.product.seller,
                message=f"New order received for {item.product.title}."
            )
            item.product.is_sold = True
            item.product.save()

        cart_items.delete()

        return redirect('/my-orders/')

    
    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items
        }
    )

@login_required
def my_orders(request):

    orders = Order.objects.filter(
        buyer=request.user
    ).order_by('-created_at')

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )


@login_required
def seller_dashboard(request):

    active_products = Product.objects.filter(
        seller=request.user,
        is_sold=False
    )

    sold_products = Product.objects.filter(
        seller=request.user,
        is_sold=True
    )

    orders_received = Order.objects.filter(
        seller=request.user
    ).order_by('-created_at')

    revenue = sold_products.aggregate(
        total=Sum('price')
    )['total'] or 0

    return render(
        request,
        'seller_dashboard.html',
        {
            'active_products': active_products,
            'sold_products': sold_products,
            'orders_received': orders_received,
            'revenue': revenue
        }
    )

@login_required
def edit_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        seller=request.user
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('/seller-dashboard/')

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'edit_product.html',
        {'form': form}
    )

@login_required
def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        seller=request.user
    )

    product.delete()

    return redirect('/seller-dashboard/')

@login_required
def confirm_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        seller=request.user
    )

    if request.method == "POST":

        form = ConfirmOrderForm(
            request.POST,
            instance=order
        )

        if form.is_valid():

            order = form.save(commit=False)

            order.status = "Confirmed"

            order.save()

            Notification.objects.create(
                user=order.buyer,
                message=f"Your order for {order.product.title} has been confirmed."
            )

            return redirect('/seller-dashboard/')

    else:

        form = ConfirmOrderForm(
            instance=order
        )

    return render(
        request,
        "confirm_order.html",
        {
            "form": form,
            "order": order
        }
    )



@login_required
def complete_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        buyer=request.user
    )

    order.status = "Completed"
    order.save()

    return redirect('/my-orders/')



@login_required
def add_review(request, order_id):

    print("Order ID:", order_id)
    print("Current User:", request.user)

    order = get_object_or_404(
        Order,
        id=order_id
    )

    print("Order Buyer:", order.buyer)
    print("Order Status:", order.status)

    if order.buyer != request.user:
        return redirect('/my-orders/')

    if order.status != "Completed":
        return redirect('/my-orders/')

    if Review.objects.filter(order=order).exists():
        return redirect('/my-orders/')

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.order = order
            review.buyer = request.user
            review.seller = order.seller

            review.save()

            Notification.objects.create(
                user=order.seller,
                message=f"You received a new review for {order.product.title}."
            )

            return redirect('/my-orders/')

    else:
        form = ReviewForm()

    return render(
        request,
        'add_review.html',
        {
            'form': form,
            'order': order
        }
    )

@login_required
def notifications(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'notifications.html',
        {
            'notifications': notifications
        }
    )

@login_required
def cancel_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        buyer=request.user
    )

    if order.status == "Pending":

        order.status = "Cancelled"
        order.save()

    return redirect('/my-orders/')


@login_required
def missed_pickup(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        seller=request.user
    )

    if order.status == "Confirmed":

        order.status = "Missed Pickup"
        order.save()

    return redirect('/seller-dashboard/')
    

@login_required
def buy_now(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('/checkout/')