from django.contrib import admin
from ui.models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class AuthorAdmin(admin.ModelAdmin):
    pass
