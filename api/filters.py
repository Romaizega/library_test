from django_filters import rest_framework as filters
from community.models import Events


class EventsFilter(filters.FilterSet):
    """Фильтр для мероприятий."""

    title = filters.CharFilter(
        field_name='title',
        lookup_expr='istartswith')

    class Meta:
        model = Events
        fields = (
            'date',
            'title',
        )
