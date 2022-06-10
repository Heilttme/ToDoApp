from django.contrib import admin
from django.urls import path, include

from .views import RegisterUser, logout_user, login_user

urlpatterns = [
    path('sign_up', RegisterUser.as_view(), name='sign_up'),
    path('sign_in', login_user, name='sign_in'),
    path('logout/', logout_user, name='logout'),
]
