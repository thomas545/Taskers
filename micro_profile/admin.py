from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)

admin.site.register(Address)
admin.site.register(Profile)