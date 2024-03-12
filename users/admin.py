from django.contrib import admin
from django.contrib.admin import display
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User, UserOrganisation

User = get_user_model()

admin.site.site_header = 'Администратор сайта "Library"'
admin.site.empty_value_display = 'Не выбрано'
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number',
    )
    filter_horizontal = ('organizations',)

    list_editable = (
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number',
    )
    search_fields = (
        'username',
        'email',
        'phone_number',)
    list_filter = (
        'username',
        'email',
        'phone_number',)


@admin.register(UserOrganisation)
class UserOrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'organisation',
    )
    list_display_links = ('user',)
    search_fields = (
        'user__username',
        'organisation__title',
    )
    list_filter = (
        'user',
        'organisation',
    )
