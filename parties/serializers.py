from rest_framework import serializers
from models import Party, Votebank

class VotebankSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	class Meta:
		model = Votebank
		fields = ('id', 'party', 'user', 'created_at')

class PartySerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	vote = serializers.HyperlinkedRelatedField(many=True, view_name='votes-detail', read_only=True)
	
	class Meta:
		model = Party
		fields = ('id', 'name', 'logo', 'vote', 'created_at')
		read_only_fields = ('vote',)