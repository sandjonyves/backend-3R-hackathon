from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Agent)