from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Contact, Statistic, Timer

admin.site.register(Contact)


@admin.register(Timer)
class TimerAdmin(SingletonModelAdmin):
    list_display = ("time",)


@admin.register(Statistic)
class HomeAdmin(SingletonModelAdmin):
    list_display = ("delegates", "speakers", "square_meters", "exhibitors", "country")
