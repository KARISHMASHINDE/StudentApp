from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Admin, Courses, Students

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Courses)
admin.site.register(Students)
