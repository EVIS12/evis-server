from django.contrib import admin

from .models import AboutConferenceImage, ContractFile, ContractForm

admin.site.register(ContractFile)
admin.site.register(AboutConferenceImage)
admin.site.register(ContractForm)
