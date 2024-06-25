from django.contrib import admin

from .models import FloorPlan, RegisterLink, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_active", "is_superuser"]
    list_editable = ["is_active"]
    list_display_links = ["name", "email"]


admin.site.register(RegisterLink)
admin.site.register(FloorPlan)
