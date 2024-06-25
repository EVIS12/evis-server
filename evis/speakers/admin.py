from django.contrib import admin

from .models import Advisors, Speakers, SpeakersVersion


@admin.register(Speakers)
class SpeakerAdmin(admin.ModelAdmin):
    @admin.action(description="Make conference_page equal false")
    def make_conference_page_false(self, request, queryset):
        queryset.update(conference_page=False)

    @admin.action(description="Make home_page equal false")
    def make_home_page_false(self, request, queryset):
        queryset.update(home_page=False)

    actions = ["make_conference_page_false", "make_home_page_false"]
    list_display = ["name", "job_title", "created_at"]


@admin.register(SpeakersVersion)
class SpeakerVersionAdmin(admin.ModelAdmin):
    list_display = ["name", "year"]


@admin.register(Advisors)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ["name", "job_title", "created_at"]
