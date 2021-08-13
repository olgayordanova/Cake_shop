from django.test import TestCase

from cake_shop_app.forms import ProductCreateForm
from cake_shop_auth.models import CakeShopUser
from profiles.forms import ProfileForm
from profiles.models import Profile

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class ProfileFormTest(TestCase):

    def test_ProfileCreate_expectTrue(self):
        user = CakeShopUser.objects.create(email='o.yordanova@activabg.com', password='1234')
        profile = Profile(
            user=user,
        )
        profile.save ()
        profile_form = ProfileForm(
                {'first_name': 'Olga',
                 'last_name': 'Yordanova',
                 'age': '30',
                 }
        )
        self.assertTrue(profile_form.is_valid())
        # self.assertHTMLEqual(
        #     profile_form.as_ul(),
        #     """<li><label for="id_first_name">First name:</label> <input type="text" name="first_name" value="Olga" maxlength="20" id="id_first_name"></li>
        #     <li><label for="id_last_name">Last name:</label> <input type="text" name="last_name" value="Yordanova" maxlength="20" id="id_last_name"></li>
        #     <li><label for="id_age">Age:</label> <input type="number" name="age" value="30" id="id_age"></li>"""
        # )
    def test_ProfileCreateAgeIsNegative_expectRaise(self):
        user = CakeShopUser.objects.create(email='o.yordanova@activabg.com', password='1234')
        profile = Profile(
            user=user,
        )
        profile.save ()
        profile_form = ProfileForm(
                {'first_name': 'Olga',
                 'last_name': 'Yordanova',
                 'age': '-30',
                 }
        )
        self.assertFalse(profile_form.is_valid())


class ProductCreateFormTest(TestCase):
    im = Image.new(mode='RGB', size=(200, 200))
    im_io = BytesIO()
    im.save(im_io, 'JPEG')
    im_io.seek(0)
    image = InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None)

    valid_name = 'Product 1'
    valid_type = 'cake'
    valid_description = 'Product description'
    valid_price = 1.0
    valid_discount = 0.2

    def test_CorectProductCreate_expectTrue(self):
        data = {
            'name': self.valid_name,
            'type': self.valid_type,
            'description': self.valid_description,
            'price': self.valid_price,
            'discount': self.valid_discount,
        }
        file_dict = {'product_image': self.image}

        product_create_form = ProductCreateForm(data=data, files=file_dict)
        self.assertTrue(product_create_form.is_valid(), product_create_form.errors)

    def test_ProductCreateWhenPriceIsNegative_expectRaise(self):
        price = -1.5
        data = {
            'name': self.valid_name,
            'type': self.valid_type,
            'description': self.valid_description,
            'price': price,
            'discount': self.valid_discount,
        }
        file_dict = {'product_image': self.image}

        product_create_form = ProductCreateForm(data=data, files=file_dict)
        self.assertFalse(product_create_form.is_valid())

    def test_ProductCreateWhenDiscountIsNegative_expectRaise(self):
        discount = -0.5
        data = {
            'name': self.valid_name,
            'type': self.valid_type,
            'description': self.valid_description,
            'price': self.valid_price,
            'discount': discount,
        }
        file_dict = {'product_image': self.image}

        product_create_form = ProductCreateForm(data=data, files=file_dict)
        self.assertFalse(product_create_form.is_valid())

    def test_ProductCreateWhenDiscountGreatThanOne_expectRaise(self):
        discount = 1.2
        data = {
            'name': self.valid_name,
            'type': self.valid_type,
            'description': self.valid_description,
            'price': self.valid_price,
            'discount': discount,
        }
        file_dict = {'product_image': self.image}

        product_create_form = ProductCreateForm(data=data, files=file_dict)
        self.assertFalse(product_create_form.is_valid())

    def test_ProductCreateWhenTypeNotInChoises_expectRaise(self):
        type = 'neshto'
        data = {
            'name': self.valid_name,
            'type': type,
            'description': self.valid_description,
            'price': self.valid_price,
            'discount': self.valid_discount,
        }
        file_dict = {'product_image': self.image}

        product_create_form = ProductCreateForm(data=data, files=file_dict)
        self.assertFalse(product_create_form.is_valid())