from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime

from cake_shop import settings


class Product(models.Model):
    TYPE_CHOICE_CAKE = 'cake'
    TYPE_CHOICE_BISCUIT= 'buscuit'

    TYPE_CHOICES = (
        (TYPE_CHOICE_CAKE, 'Cake'),
        (TYPE_CHOICE_BISCUIT, 'Buscuit'),
    )

    name = models.CharField(max_length=25,)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField ( blank=True, null=True )
    product_image = models.ImageField( upload_to='images',)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse ( "core:product", kwargs={
    #         "pk": self.pk
    #
    #     } )
    #
    # def get_add_to_cart_url(self):
    #     return reverse ( "core:add-to-cart", kwargs={
    #         "pk": self.pk
    #     } )
    #
    # def get_remove_from_cart_url(self):
    #     return reverse ( "core:remove-from-cart", kwargs={
    #         "pk": self.pk
    #     } )

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.price*(1-self.item.discount)

    def get_final_price(self):
        if self.item.discount:
            return self.get_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True )
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total



