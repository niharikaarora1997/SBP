# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User_Info(models.Model):
	username=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
# Create your models here.
