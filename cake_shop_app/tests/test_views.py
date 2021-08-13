from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from cake_shop_app.models import Product, OrderItem, Order
from cake_shop_app.tests.test_base import create_product
from cake_shop_app.views import add_to_cart
from cake_shop_auth.models import CakeShopUser
from profiles.models import Profile
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

UserModel = get_user_model()

class IndexTests(TestCase):
    @patch('cake_shop_app.models.Product.objects')
    def test_index_page(self,orders_mock):
        orders_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('index'), )
        self.assertTemplateUsed(response, 'index.html')
        posts = response.context['cakes']


class CakeShopTestCase(TestCase):
    logged_in_user_email = 'o.yordanova@activabg.com'
    logged_in_user_password = '1234'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        profile = Profile(
            user=self.user,
        )
        profile.save ()


class ProfileDetailsTest(CakeShopTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        profile = Profile(
            user=self.user,
        )
        profile.save ()

    def test_getPrfileDetails_whenLoggedInUser(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))
        self.assertEqual(self.user.id, response.context['profile'].user_id)




class ProductCreateViewTests(TestCase):
    logged_in_user_email = 'irina@dir.bg'
    logged_in_user_password = '1234'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        self.super_user = UserModel.objects.create_superuser(
            email='o.yordanova@activabg.com',
            password='1234',
        )
        profile = Profile(
            user=self.user,
        )
        profile.save ()
        profile = Profile(
            user=self.super_user,
        )
        profile.save ()

    def test_createProductIfSuperUser_WhenUserLoggedIn(self):
        self.client.force_login(self.super_user)
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed ( response, 'create.html' )
        self.assertTrue(self.super_user.is_authenticated)


    def test_createProductIfNotSuperUser_WhenUserLoggedIn(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.user.is_authenticated)

class EditProductTests(TestCase):

    im = Image.new(mode='RGB', size=(200, 200))
    im_io = BytesIO()
    im.save(im_io, 'JPEG')
    im_io.seek(0)
    image = InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None)

    logged_in_user_email = 'irina@dir.bg'
    logged_in_user_password = '1234'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        self.super_user = UserModel.objects.create_superuser(
            email='o.yordanova@activabg.com',
            password='1234',
        )
        profile = Profile(
            user=self.user,
        )
        profile.save ()
        profile_su = Profile(
            user=self.super_user,
        )
        profile_su.save ()

    def test_edit_product_WhenSuperUser_expectSuccses(self):
        self.client.force_login(self.super_user)
        product = create_product(
            id = 1,
            name='Product 1',
            type = 'cake',
            description = 'Product description',
            price = 1.0,
            discount = 0.2,
            product_image = 'http://image.com')

        response = self.client.post(reverse('edit', kwargs={
            'pk': product.id,
        }))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed ( response, 'edit.html' )
        self.assertTrue ( self.super_user.is_authenticated )



    def test_delete_product_WhenSuperUser_expectSuccses(self):
        self.client.force_login(self.super_user)
        product = create_product(
            id = 1,
            name='Product 1',
            type = 'cake',
            description = 'Product description',
            price = 1.0,
            discount = 0.2,
            product_image = 'http://image.com')

        response = self.client.post(reverse('delete', kwargs={
            'pk': product.id,
        }))

        self.assertEqual(302, response.status_code)
        self.assertTrue ( self.super_user.is_authenticated )

    def test_delete_product_WhenUser_expectRaise(self):
        self.client.force_login ( self.user )
        product = create_product (
            id=1,
            name='Product 1',
            type='cake',
            description='Product description',
            price=1.0,
            discount=0.2,
            product_image='http://image.com' )

        response = self.client.post ( reverse ( 'delete', kwargs={
            'pk': product.id,
        } ) )
        self.assertEqual ( 403, response.status_code )
        self.assertTrue ( self.user.is_authenticated )

#------------------------------------

class AddToCardTest(TestCase):
    logged_in_user_email = 'irina@dir.bg'
    logged_in_user_password = '1234'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        self.super_user = UserModel.objects.create_superuser(
            email='o.yordanova@activabg.com',
            password='1234',
        )
        profile = Profile(
            user=self.user,
        )
        profile.save ()
        profile = Profile(
            user=self.super_user,
        )
        profile.save ()

    # product = create_product (
    #     id=1,
    #     name='Product 1',
    #     type='cake',
    #     description='Product description',
    #     price=1.0,
    #     discount=0.2,
    #     product_image='http://image.com' )


    def test_add_to_cart(self):
        pass
        # self.client.force_login ( self.super_user )
        # product = Product ( 1, 'Product 1', 'cake', 'Product description', 1.0, 0.2, 'http://image.com' )
        # quantity = 5
        # date_added = '2021-07-29 18:17:52.829610'

        # order_item = OrderItem (
        #     item=product,
        #     user=self.super_user,
        #     quantity=quantity,
        #     date_added=date_added
        # )


        # response = self.client.post(reverse('cart', kwargs={
        #     'pk': product.id,
        # }))
        #
        # order_exist = Order.objects.filter(
        #     user_id=self.super_user.id,
        #     complete=True,
        # ) \
        #     .exists()
        #
        # self.assertTrue(order_exist)
        # response = self.client.post ( reverse ( 'cart', kwargs={
        #     'pk': product.pk,
        # } ) )

        # response = self.client.post ( reverse ( 'like pet', kwargs={
        #     'pk': pet.id,
        # } ) )

        # self.assertEqual ( 302, response.status_code )

        # self.assertTemplateUsed ( response, 'index.html' )
        # self.assertEqual ( 302, response.status_code )


# ------------------------------------