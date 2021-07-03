from django.contrib import admin
from .models import User, Admin, Owner, Client, ClientInfo


@admin.register(User, Admin, Owner, Client, ClientInfo)
class UserAdmin(admin.ModelAdmin):
    pass

