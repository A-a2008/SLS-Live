from django.contrib import admin
from .models import Story

# Register your models here.

admin.site.register(Story)

# Site names

admin.site.site_title = "SLS"
admin.site.site_header = "Students' Life Stories Administration"
admin.site.index_title = "Students' Life Stories Administration"
