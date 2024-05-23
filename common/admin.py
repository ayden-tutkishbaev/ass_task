from django.contrib import admin
from common.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['file', 'file_type']
    search_fields = ['file']
    list_filter = ['file_type']


@admin.register(BackgroundImage1)
class BackgroundImage1(admin.ModelAdmin):
    list_display = ['text', 'bottom_text']


@admin.register(AboutUs1)
class AboutUs1Admin(admin.ModelAdmin):
    list_display = ['headline', 'text']


@admin.register(AboutUs2)
class AboutUs2Admin(admin.ModelAdmin):
    list_display = ['headline', 'text']


@admin.register(Promo)
class AboutUs2Admin(admin.ModelAdmin):
    list_display = ['headline', 'text']


@admin.register(StandardSettings)
class StandardSettingsAdmin(admin.ModelAdmin):
    list_display = ['main_phone_number', 'main_email', 'instagram', 'vkontakte']


