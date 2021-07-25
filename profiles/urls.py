from django.urls import path

from profiles.views import profile_details

urlpatterns = (
    path('', profile_details, name='profile details'),
)

import profiles.signals
