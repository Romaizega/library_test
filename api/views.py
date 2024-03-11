from djoser.views import UserViewSet

from users.models import User
from api.serializers import UserSerializer


class LibraryUserViewSet(UserViewSet):
    """ViewSet для работы с пользователями."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
