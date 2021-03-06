from django.contrib.auth.models import User
from django.db import models


class Person(User):
    balance = models.FloatField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    ruc = models.CharField(max_length=11, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=70, null=True, blank=True)


User.person = property(lambda e: Person.objects.get(pk=e.pk))
