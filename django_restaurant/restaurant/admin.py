from django.contrib import admin

# Register your models here.
from restaurant.models import User

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
