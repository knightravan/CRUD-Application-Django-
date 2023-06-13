from django.contrib import admin
from .models import regi

# Register your models here.
@admin.register(regi)
class regiadmin(admin.ModelAdmin):
	list_display=('id','name','email','password')
