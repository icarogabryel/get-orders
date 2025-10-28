from django.contrib.auth.models import User
from django.db import models

from ..dishes.models import Dish


class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PREPARING = 'PREPARING', 'Preparing'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELED = 'CANCELED', 'Canceled'


class Order(models.Model):
    id: models.AutoField
    dishes: models.QuerySet['OrderDish']
    user = models.ForeignKey(User, related_name='orders', on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    @property
    def customer_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def total_price(self):
        return sum(order_dish.dish.price * order_dish.quantity for order_dish in self.dishes.all())

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"


class OrderDish(models.Model):
    id: models.AutoField
    order = models.ForeignKey(Order, related_name='dishes', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['order', 'dish__name']

    def __str__(self):
        return f"{self.quantity} x {self.dish.name} for Order {self.order.id}"
