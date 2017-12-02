from rest_framework import serializers
from models import Users, UsersToken

class UsersSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()

	class Meta:
		model = Users
		fields = ('id', 'username', 'email', 'name', 'gender', 'created_at')

class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('id', 'username', 'password', 'email', 'name', 'gender')
		read_only_fields = ('id',)

class SigninSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('username', 'password')

class UsersTokenSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	user = serializers.ReadOnlyField(source='user.username')
	
	class Meta:
		model = UsersToken
		fields = ('id', 'user', 'access_token')