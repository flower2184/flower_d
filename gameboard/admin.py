from django.contrib import admin
from .models import Games

class GamesAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Games, GamesAdmin)
