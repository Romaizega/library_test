from djoser.serializers import UserSerializer
from rest_framework import serializers

from api.fields import Base64ImageField
from community.models import Events, Organisation
from users.models import User, UserOrganisation


class LibraryUserSerializer(UserSerializer):
    """Сериализатор для модели LibraryUser"""

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class OrganisationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Organisation"""

    class Meta:
        model = Organisation
        fields = '__all__'


class UserOrganisationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели UserOrganisation"""

    user = LibraryUserSerializer(read_only=True)
    organisation = OrganisationSerializer(read_only=True)

    class Meta:
        model = UserOrganisation
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Event"""

    organizations = OrganisationSerializer(
        many=True,
        read_only=True)

    class Meta:
        model = Events
        fields = '__all__'
