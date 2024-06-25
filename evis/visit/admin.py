from django.contrib import admin

from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "photo")
    list_filter = ("title", "description", "photo")
    search_fields = ("title", "description", "photo")
    ordering = ("title", "description", "photo")
    readonly_fields = ("title", "description", "photo")
    fieldsets = (("Visit", {"fields": ("title", "description", "photo")}),)
