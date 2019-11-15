from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
#from .forms import UserAdminCreationForm, UserAdminChangeForm

"""
# Register your models here.
class CustomUserAdmin(UserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm
"""
admin.site.register(User, UserAdmin)