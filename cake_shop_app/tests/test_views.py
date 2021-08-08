from unittest.mock import patch

from django.http import request
from django.test import TestCase, Client
from django.urls import reverse

class IndexTests(TestCase):
    @patch('cake_shop_app.models.Product.objects')
    def test_index_page(self,orders_mock):
        orders_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('index'), )
        self.assertTemplateUsed(response, 'index.html')
        posts = response.context['cakes']


# class ProductDeleteViewTests(TestCase):
#     @patch('cake_shop_app.models.Product.objects')
#     def test_delete_product(self,delete_mock):
#         delete_mock.all.return_value = [1]
#         client = Client()
#         response = client.get(reverse('delete'), )
#         self.assertTemplateUsed(response, 'delete.html')
#         posts = response.context['cakes']


# class AddToCardTest(TestCase):
#     product = Product(1, 'Product 1','cake','Product description', 1.0, 0.2, 'http://image.com')
#     user = CakeShopUser(email='o.yordanova@activabg.com', password='1234')
#
#     def test_add_to_cart(self):
#         pk = self.product.pk
#         add_to_cart(request, pk)

