from django_filters import rest_framework as filters
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import LimitPagination
from api.serializers import (EventSerializer, OrganisationSerializer,
                             UserOrganisationSerializer, UserSerializer)
from community.models import Events, Organisation
from community.tasks import create_event_with_delay
from users.models import User, UserOrganisation
from api.filters import EventsFilter


class LibraryUserViewSet(UserViewSet):
    """ViewSet для работы с пользователями."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserOrganisationViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для доступа только на чтение к модели UserOrganisation."""

    queryset = UserOrganisation.objects.all().order_by('id')
    serializer_class = UserOrganisationSerializer
    pagination_class = LimitPagination


class OrganisationViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с организациями."""

    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def create_organizations(self, request, *args, **kwargs):
        """Создает организацию."""
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventsViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с мероприятиями."""

    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventsFilter

    @action(detail=False, methods=('post',),
            permission_classes=[IsAuthenticated])
    def create_event_view(self, request):
        """Создает мероприятие."""
        title = request.data.get('title')
        description = request.data.get('description')
        organizations = request.data.get('organizations')
        image = request.data.get('image')
        date = request.data.get('date')
        create_event_with_delay.delay(
            title, description, organizations, image, date)
        return Response(status=status.HTTP_201_CREATED)
