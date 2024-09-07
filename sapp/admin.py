from django.contrib import admin
from .models import Enroll,Notice, Routine

# Register your models here.
admin.site.register(Enroll)
admin.site.register(Notice)
admin.site.register(Routine)