"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # Con estos comando cambio lo que se muestra,
    # Lo que es link al Profile
    # Lo que es editable
    list_display = ('pk', 'user', 'phone', 'website', 'created')
    list_display_links = ('pk', 'user')
    list_editable = ('phone', 'website')

    # Para aparecer barra de busqueda solo debo definir
    # los campos por los que quiero buscar
    # Con esto agrego los campos por los cuales quiero buscar
    search_fields = ('user__email', 'user__username', 'user__first_name',
                     'user__last_name', 'phone')

    # Para agregar filtros solo debemos definir
    # los campos que queremos poder filtrar
    # Aparecen en el orden en el que son escritos
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
