import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.http import HttpResponse

from celery import shared_task

@shared_task
def sum(x,y):
    return x+y

