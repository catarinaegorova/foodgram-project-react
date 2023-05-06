from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Subscription, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'username')
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)
