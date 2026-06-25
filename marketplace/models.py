from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Notes', 'Notes'),
        ('Books', 'Books'),
        ('Papers', 'Papers'),
        ('Stationery', 'Stationery'),
    ]

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Good', 'Good'),
        ('Acceptable', 'Acceptable'),
    ]

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    condition = models.CharField(
        max_length=50,
        choices=CONDITION_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='products/'
    )

    is_urgent = models.BooleanField(
        default=False
    )

    is_sold = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class CartItem(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    added_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
    
class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Missed Pickup', 'Missed Pickup'),
    ]

    PAYMENT_CHOICES = [
        ('Cash on Pickup', 'Cash on Pickup'),
        ('UPI on Pickup', 'UPI on Pickup'),
    ]
    
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        default='Cash on Pickup'
    )

    meeting_location = models.CharField(
        max_length=200,
        blank=True
    )

    meeting_time = models.CharField(
        max_length=100,
        blank=True
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer_orders'
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller_orders'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"
    

class Review(models.Model):

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_received'
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_given'
    )

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.rating} Stars"
    

class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.CharField(
        max_length=255
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.message
    

class UserActivity(models.Model):

    ACTIVITY_CHOICES = [
        ('View', 'View'),
        ('Cart', 'Cart'),
        ('Buy', 'Buy'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )