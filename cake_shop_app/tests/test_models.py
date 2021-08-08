from django.core.exceptions import ValidationError
from django.test import TestCase

from cake_shop_app.models import Product, OrderItem, Order
from cake_shop_auth.models import CakeShopUser


# https://adamj.eu/tech/2020/01/13/make-django-tests-always-rebuild-db/
from profiles.models import Profile


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

class OrderItemTests(TestCase):
    user = CakeShopUser(email='o.yordanova@activabg.com', password='1234')
    product = Product(1, 'Product 1','cake','Product description', 1.0, 0.2, 'http://image.com')
    product_null_discount = Product(2, 'Product 2', 'cake', 'Product description2', 1.0, '', 'http://image.com')
    quantity = 5
    date_added = '2021-07-29 18:17:52.829610'
    order_item = OrderItem(
        item=product,
        user=user,
        quantity=quantity,
        date_added=date_added
    )
    def test_get_total_item_price(self):
        self.assertEqual ( self.order_item.get_total_item_price() , 5 )

    def test_get_discount_item_price(self):
        self.assertEqual (self.order_item.get_discount_item_price() , 4 )

    def test_get_final_price_WhenDiscountPriceIsNotNull(self):
        self.assertEqual (self.order_item.get_final_price() , 4 )

    def test_get_final_price_WhenDiscountPriceIsNull(self):
        order_item1 = OrderItem(
            item=self.product_null_discount,
            user=self.user,
            quantity=self.quantity,
            date_added=self.date_added
        )
        self.assertEqual (order_item1.get_final_price() , 5 )

    def test_create_orderitemWhenQuantityIsNegative(self):
        quantity = -5
        order_item = OrderItem(
            item=self.product,
            user=self.user,
            quantity=quantity,
            date_added=self.date_added
        )
        with self.assertRaises(ValidationError) as context:
            order_item.full_clean()
            order_item.save()

        self.assertIsNotNone(context.exception)

class OrderTests(TestCase):
    user = CakeShopUser(email='o.yordanova@activabg.com', password='1234')
    product = Product(1, 'Product 1','cake','Product description', 1.0, 0.2, 'http://image.com')
    # product_null_discount = Product(2, 'Product 2', 'cake', 'Product description2', 1.0, '', 'http://image.com')
    quantity = 5
    date_added = '2021-07-29 18:17:52.829610'
    date_ordered = '2021-07-29 18:17:52.829610'
    complete =False
    order_item = OrderItem(
        item=product,
        user=user,
        quantity=quantity,
        date_added=date_added
    )
    # order_item.full_clean()
    # order_item.save()
    # items = order_item
    # a=5

    # def test_create_order_expectSuccess(self):
    #     order = Order(
    #         user = self.user,
    #         items = self.items,
    #         date_ordered = self.date_ordered,
    #         complete = self.complete
    #         )
    #     # order.full_clean()
    #     # order.save()


class UserModelTest(TestCase):
    def test_user_model(self):
        user = CakeShopUser.objects.create(email='o.yordanova@activabg.com', password='1234')
        self.assertEqual('o.yordanova@activabg.com', user.email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

class ProfileModelTest(TestCase):

    def test_profile_model_WhenIsValid_expectNothing(self):
        user = CakeShopUser.objects.create(email='o.yordanova@activabg.com', password='1234')
        profile = Profile(
            user=user,
        )

        profile.save ()
        user_profile = Profile.objects.get (user_id =  user)
        self.assertEqual(profile.first_name, '')
        self.assertEqual(profile.last_name, '')
        self.assertEqual(profile.age, None)
        self.assertEqual(profile.is_complete, False)


