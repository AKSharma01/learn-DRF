# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENDER = (
		('male', 'male'),
		('female', 'female'),
		('other', 'other')
	)

class Users(models.Model):
	id = models.CharField(max_length=100, primary_key=True, blank=False)
	username = models.CharField(max_length=100, unique=True, blank=False)
	email = models.CharField(max_length=200, unique=True, blank=False)
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	gender = models.CharField(choices=GENDER, default='other', max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created_at',)
		db_table = 'users'
		app_label = 'users'

	def __str__(self):
		return self.username

class UsersToken(models.Model):
	user = models.ForeignKey(
		'Users',
		on_delete=models.CASCADE,
		related_name='users'
		)
	access_token = models.CharField(max_length=255, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
