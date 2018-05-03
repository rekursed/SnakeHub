# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Message(models.Model):
    # From Django 2.0 on_delete is required
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
