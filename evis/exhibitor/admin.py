from django.contrib import admin

from evis.exhibitor.models import Exhibitor, Organizers

# Register your models here.

admin.site.register(Organizers)


@admin.register(Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "country")
    search_fields = ("name", "address", "country")
