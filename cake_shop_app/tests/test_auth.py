from django.test import TestCase

from cake_shop_auth.forms import SignUpForm, SignInForm
from cake_shop_auth.models import CakeShopUser

class SighUpTest(TestCase):

    def test_whenPasswordsDoesMatch_expectNoting(self):
        user_form = SignUpForm(
            {'email': 'o.yordanova@activabg.com',
             'password1': '1234',
             'password2': '1234'
             }
        )
        self.assertTrue(user_form.is_valid())

    def test_whenPasswordsDoesNotMatch_expectRaiseValidationError(self):
        user_form = SignUpForm(
            {'email': 'o.yordanova@activabg.com',
             'password1': '1234',
             'password2': '1111'
             }
        )
        self.assertFalse(user_form.is_valid())

    def test_whenEmailIsValid_expectNoting(self):
        user_form = SignUpForm(
            {'email': 'o.yordanova@activabg.com',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertTrue(user_form.is_valid())

    def test_whenEmailIsNotValid_expectRaiseValidationError(self):
        user_form = SignUpForm(
            {'email': 'o.yordanova.activabg.com',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertFalse(user_form.is_valid())



    def test_whenUserEmailAlreadyExists_expectRaiseValidationError(self):
        CakeShopUser.objects.create ( email='o.yordanova@activabg.com', password='1234' )

        user_form = SignUpForm(
            {'email': 'o.yordanova@activabg.com',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertFalse ( user_form.is_valid () )

    def test_whenUser_withValidEmailAndPasswords(self):
        user_form = SignUpForm(
            {'email': 'o.yordanova@activabg.com',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertTrue(user_form.is_valid())
        user_form.save()
        registered_user = CakeShopUser.objects.get(email='o.yordanova@activabg.com')
        self.assertIsNotNone(registered_user)

class SighInTest(TestCase):

    def test_whenUserExistAndPasswordsDoesMatch_expectNoting(self):
        user = CakeShopUser.objects.create ( email='o.yordanova@activabg.com', password='1234' )
        registered_user = CakeShopUser.objects.get ( email='o.yordanova@activabg.com' )
        self.assertTrue((registered_user is not None) and user.is_authenticated)

    def test_whenUserNot_expectRaise(self):
        user = None
        self.assertTrue((user is None) )


