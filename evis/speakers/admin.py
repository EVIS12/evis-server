from django.contrib import admin

from .models import Advisors, Speakers, SpeakersVersion


@admin.register(Speakers)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ["name", "job_title", "created_at"]


@admin.register(SpeakersVersion)
class SpeakerVersionAdmin(admin.ModelAdmin):
    list_display = ["name", "year"]


@admin.register(Advisors)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ["name", "job_title", "created_at"]
