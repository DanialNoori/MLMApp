from django.contrib import admin
from .models import AppUser, Address, ParentHood
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Address)
admin.site.register(ParentHood)