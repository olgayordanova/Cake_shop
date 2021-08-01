import os

from django import forms

from cake_shop import settings
from profiles.models import Profile


class ProfileForm( forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')

