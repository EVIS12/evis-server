from django.contrib import admin

from .models import RegisterInterest, Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "photo")
    list_filter = ("title", "description", "photo")
    search_fields = ("title", "description", "photo")
    ordering = ("title", "description", "photo")
    readonly_fields = ("title", "description", "photo")
    fieldsets = (("Visit", {"fields": ("title", "description", "photo")}),)


@admin.register(RegisterInterest)
class RegisterInterestAdmin(admin.ModelAdmin):
    list_display = ("email", "job_title", "company_name", "address", "city", "interested_in")
    list_filter = ("email", "job_title", "company_name", "address", "city", "interested_in")
    search_fields = ("email", "job_title", "company_name", "address", "city", "interested_in")
    ordering = ("email", "job_title", "company_name", "address", "city", "interested_in")
    readonly_fields = ("email", "job_title", "company_name", "address", "city", "interested_in")
