# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins, generics, viewsets, exceptions, status
from rest_framework.response import Response
from models import Users, UsersToken
import uuid, bcrypt, random
from serializer import UsersSerializer, SignupSerializer, SigninSerializer
from users.permissions import IsUserAuthenticated, IsUserOwner

class UsersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	queryset = Users.objects.all()
	serializer_class = UsersSerializer
	permission_classes = (IsUserAuthenticated, IsUserOwner, )

class UserRegisterViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Users.objects.all()
	serializer_class = SignupSerializer

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(id=str(uuid.uuid4()), password=bcrypt.hashpw(str(self.request.data['password']), bcrypt.gensalt()))

class UserLoginViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Users.objects.all()
	serializer_class = SigninSerializer

	def post(self, request, *args, **kwargs):
		username = request.data.get('username', None)
		password = request.data.get('password', None)

		if not username or not password:
			raise exceptions.AuthenticationFailed('No credentials provided.')

		user = Users.objects.filter(**{'username':username})
		data = {}
		if len(user) and bcrypt.checkpw(str(password), str(user[0].password)):
			
			token = UsersToken()
			token.user = user[0]
			token.access_token = str(bcrypt.hashpw(str(random.random()), bcrypt.gensalt()))
			token.save()
			
			data = {
				'id' : token.id,
				'user' : token.user.username,
				'acces_token' : token.access_token,
				'message' : "Successfully Logged-In"
			}

			request.session['token'] = token.access_token
			request.session['auth'] = user[0].username
		else:
			raise exceptions.AuthenticationFailed('Invalid Credentials Provided.')
		return Response(data, status=status.HTTP_200_OK)

class UserLogoutViewSet(generics.GenericAPIView):
	queryset = UsersToken.objects.all()
	serializer_class = UsersSerializer
	permission_classes = (IsUserAuthenticated, )

	def get(self, request, *args, **kwargs):
		token = UsersToken.objects.filter(**{'access_token':request.session.get('token', None)}).delete()
		data = {
			'message' : "Successfully Logged-Out"
		}
		return Response(data, status=status.HTTP_200_OK)
