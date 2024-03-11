from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import User


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = '__all__'
