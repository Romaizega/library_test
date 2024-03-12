from djoser.views import UserViewSet
from rest_framework import viewsets

from api.pagination import LimitPagination
from api.serializers import (EventSerializer, OrganisationSerializer,
                             UserOrganisationSerializer, UserSerializer)
from community.models import Events, Organisation
from users.models import User, UserOrganisation


class LibraryUserViewSet(UserViewSet):
    """ViewSet для работы с пользователями."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserOrganisationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserOrganisation.objects.all().order_by('id')
    serializer_class = UserOrganisationSerializer
    pagination_class = LimitPagination


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
