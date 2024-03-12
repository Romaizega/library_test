from django.contrib import admin
from django.contrib.admin import display
from django.utils.html import format_html

from .models import Events, Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_display_links = ('title',)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'get_organizations_display',
        'date',
        'get_image',
    )
    filter_horizontal = ('organizations',)
    readonly_fields = ('get_image',)

    @display(description='Изображение')
    def get_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" height="50px" />')
        return 'Нет фото'

    @display(description='Организаторы')
    def get_organizations_display(self, obj):
        return ', '.join(
            str(organization) for organization in obj.organizations.all())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('organizations')
