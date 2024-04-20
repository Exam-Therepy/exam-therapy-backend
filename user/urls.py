from django.contrib import admin
from django.urls import path

from user.views import signup

urlpatterns = [
    path('/sign_up', signup)
]
