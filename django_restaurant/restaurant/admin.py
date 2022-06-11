from django.contrib import admin

from restaurant.models import User, Item


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'date_joined', 'is_staff')
    list_filter = ('is_staff', 'date_joined')
    fields = (
        'id',
        'username',
        ('first_name', 'last_name'),
        'date_joined',
        'mobile_number',
        'email',
        (
            'is_staff',
            'is_active',
        ),
    )
    ordering = ('username', 'date_joined')
    readonly_fields = ('id',)

    empty_value_display = '-empty-'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    fields = (
        'id',
        'name',
        'description',
        'price'
    )

    empty_value_display = '-empty-'
