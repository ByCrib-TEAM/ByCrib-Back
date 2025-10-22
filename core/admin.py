from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'name', 'is_staff', 'is_active']
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Categoria)
admin.site.register(models.Produto)
admin.site.register(models.Carrinho)
admin.site.register(models.ItemCarrinho)
admin.site.register(models.Marca)
admin.site.site_header = "ByCrib Admin"