# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Party(models.Model):
	id = models.CharField(max_length=255, primary_key=True)
	name = models.CharField(max_length=255, blank=False)
	logo = models.CharField(max_length=255, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name+' ('+self.logo+')'

class Votebank(models.Model):
	# parties = Party.objects.all()
	# PARTY_CHOICES = []

	# for party in parties:
	# 	PARTY_CHOICES.append((party.name, party.name))

	# PARTY_CHOICES = tuple(PARTY_CHOICES)

	party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='vote')
	user = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='user')
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		unique_together = ('user', 'party')

	def __repr__(self):
		return self.user.username

	def __str__(self):
		return self.user.username