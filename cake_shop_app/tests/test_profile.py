from cake_shop_auth.models import CakeShopUser
from profiles.forms import ProfileForm
from django.test import TestCase

from profiles.models import Profile


class ProfileTest(TestCase):

    def test_whenGreateUserGreateProfile_expectNoting(self):
        user = CakeShopUser.objects.create ( email='o.yordanova@activabg.com', password='1234' )
        registered_user = CakeShopUser.objects.get ( email=user.email )
        profile = Profile.objects.get(user_id = registered_user)
        self.assertTrue (profile is not None)

        # profile = Profile(
        #     user=user,
        # )
        # profile.save ()
        # user_profile = Profile.objects.get (user_id =  user)
        # self.assertTrue(Profile.objects.exists (user_id =  user))
        # profile_form = ProfileForm (
        #     {'first_name': 'Olga',
        #      'last_name': 'Yordanova',
        #      'age': '50',
        #      'user_id': user,
        #      'is_complete': False,
        #      }
        # )
        # self.assertTrue(profile_form.is_valid())
        # profile_form.save()
        # registered_user_profile = Profile.objects.get(user=user)
        #
        # self.assertEqual(user_profile.user_id, user.id)

