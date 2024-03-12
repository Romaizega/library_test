from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (EventsViewSet, LibraryUserViewSet, OrganisationViewSet,
                       UserOrganisationViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('users', LibraryUserViewSet, 'users')
router.register('organisations', OrganisationViewSet, 'organisations')
router.register('events', EventsViewSet, 'events')
router.register(
    'userorganisation', UserOrganisationViewSet, 'userorganisation'
)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
