from djoser.serializers import UserSerializer
from rest_framework import serializers

from api.fields import Base64ImageField
from community.models import Events, Organisation
from users.models import User, UserOrganisation


class LibraryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = '__all__'


class UserOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrganisation
        fields = '__all__'


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Events
        fields = '__all__'
