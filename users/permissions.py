from rest_framework import permissions
from users.models import UsersToken

class IsUserAuthenticated(permissions.BasePermission):
	def has_permission(self, request, view):
		token = UsersToken.objects.filter(**{'access_token':request.session.get('token')})
		if len(token):
			return True
		return False

class IsUserOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj.username == request.session.get('auth'):
			return True
		return False