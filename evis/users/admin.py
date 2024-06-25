from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import RegisterLink, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_active", "is_superuser"]
    list_editable = ["is_active"]
    list_display_links = ["name", "email"]

    def save_model(self, request, obj, form, change):
        if obj.password:
            obj.password = make_password(obj.password)
        else:
            obj.password = User.objects.get(pk=obj.pk).password
        obj.save()


admin.site.register(RegisterLink)
