from django.contrib import admin
from plants import models


class SpecieAdmin(admin.ModelAdmin):
    list_display = [
                    'name',
                    'common_name',
                    'family',
                    'iucn_level',
                    ]

admin.site.register(models.Family)
admin.site.register(models.Specie, SpecieAdmin)
