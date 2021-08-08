from django.core.exceptions import ValidationError
from django.test import TestCase

from cake_shop_app.models import Product, OrderItem
from cake_shop_auth.models import CakeShopUser


# https://adamj.eu/tech/2020/01/13/make-django-tests-always-rebuild-db/

class ProductTests(TestCase):
    valid_name = 'Product 1'
    valid_type = 'cake'
    valid_description = 'Product description'
    valid_price = 1.0
    valid_discount = 0.2
    valid_product_image = 'http://image.com'

    def test_whenPriceIsLessThan0_expectToRaise(self):
        price = -1.0

        product = Product(
            name=self.valid_name,
            type= self.valid_type,
            description=self.valid_description,
            price=price,
            discount = self.valid_discount,
            product_image=self.valid_product_image,
        )

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)

    def test_whenPriceIsGreatThan0_expectSuccess(self):
        price = 1.0

        product = Product(
            name=self.valid_name,
            type= self.valid_type,
            description=self.valid_description,
            price=price,
            discount = self.valid_discount,
            product_image=self.valid_product_image,
        )

        product.full_clean()
        product.save()

    def test_whenPriceIsEquile0_expectSuccess(self):
        price = 0.0

        product = Product(
            name=self.valid_name,
            type= self.valid_type,
            description=self.valid_description,
            price=price,
            discount = self.valid_discount,
            product_image=self.valid_product_image,
        )

        product.full_clean()
        product.save()

    def test_whenDiscountIsLessThan0_expectToRaise(self):
        discount = -0.1

        product = Product(
            name=self.valid_name,
            type= self.valid_type,
            description=self.valid_description,
            price=self.valid_price,
            discount = discount,
            product_image=self.valid_product_image,
        )

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)

    def test_whenDiscountIsGreatThan0_expectSuccess(self):
        discount = 0.1

        product = Product(
            name=self.valid_name,
            type= self.valid_type,
            description=self.valid_description,
            price=self.valid_price,
            discount = discount,
            product_image=self.valid_product_image,
        )

        product.full_clean()
        product.save()
# Тези горе няма смисъл да се тестват - build in

    def test_name(self):

        product = Product (
            name=self.valid_name,
            type=self.valid_type,
            description=self.valid_description,
            price=self.valid_price,
            discount=self.valid_discount,
            product_image=self.valid_product_image,
        )

        self.assertEqual(product.name, 'Product 1')



# class OrderItemTests(TestCase):
#     product = Product(1, 'Product 1','cake','Product description', 1.0, 0.2, 'http://image.com')
#     user = CakeShopUser(email='o.yordanova@activabg.com', password='1234')
#     valid_item =1
#     valid_user = 1
#     valid_quantity = 5
#     valid_date_added =datetime.now()
#     order_item = OrderItem(1, valid_quantity, valid_date_added,valid_item,valid_user )
#
#     def test_get_total_item_price(self):
#         self.assertEqual ( selfэсе.order_item.get_total_item_price() , 5 )
#
#     def test_get_discount_item_price(self):
#         self.assertEqual (self.order_item.get_discount_item_price() , 4 )

