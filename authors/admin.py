from django.contrib import admin
from authors.models import Profile


@admin.register(Profile)
class PprofileAdmin(admin.ModelAdmin):
    pass
