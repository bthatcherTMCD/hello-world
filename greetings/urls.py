#greetings/urls.py
from django.conf.urls import url

from .view import index

urlpatterns = [
    url(r'^$', index),
]
