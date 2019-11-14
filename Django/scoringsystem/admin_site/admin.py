from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Session, Student

admin.site.site_header = 'Senior Design Conference Admin Site'

class sessionAdmin(admin.ModelAdmin):
	list_display = ('addJudge')

admin.site.register(Session)
admin.site.register(Student)
admin.site.unregister(Group)