from django.contrib import admin
from .models import Profile, ProfileSetting

# Register your models here.
@admin.register(ProfileSetting)
class ProfileSettingAdmin(admin.ModelAdmin):
    list_display = ('actor', 'role')
    list_filter = ('actor',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name", "phone")
