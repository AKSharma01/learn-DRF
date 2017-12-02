# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from models import Party, Votebank
from serializers import PartySerializer, VotebankSerializer
from users.permissions import IsUserAuthenticated
import uuid, json

# Create your views here.
class PartyViewSet(viewsets.ModelViewSet):

	serializer_class = PartySerializer
	queryset = Party.objects.all()
	permission_classes = (IsUserAuthenticated, )
	
	def perform_create(self, serializer):
		serializer.save(id=str(uuid.uuid4()))

class VotebankViewSet(viewsets.ModelViewSet):

	serializer_class = VotebankSerializer
	queryset = Votebank.objects.all()
	permission_classes = (IsUserAuthenticated, )

	def perform_create(self, serializer):
		from users.models import UsersToken
		access_token = serializer.context['request'].session.get('token')
		token = UsersToken.objects.filter(**{'access_token':access_token})
		serializer.save(user=token[0].user)