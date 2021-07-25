from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime

# Create your models here.
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

    def get_absolute_url(self):
        return reverse ( "core:product", kwargs={
            "pk": self.pk

        } )

    def get_add_to_cart_url(self):
        return reverse ( "core:add-to-cart", kwargs={
            "pk": self.pk
        } )

    def get_remove_from_cart_url(self):
        return reverse ( "core:remove-from-cart", kwargs={
            "pk": self.pk
        } )

class OrderProduct ( models.Model ):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Order(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name

# Дата
# Номер
# Клиент номер - външен ключ клиенти връзка 1:много
# Продукт номер - външен ключ продукти връзка 1:много
# Цена
# Отстъпка
# Количество
# Статус - изпълнена/неизпълнена