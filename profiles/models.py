from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    # profile_image = models.ImageField(upload_to='profiles', blank=True,)

    is_complete = models.BooleanField(
        default=False,
    )

    # discount = models.FloatField(
    #     default=0,
    # )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )