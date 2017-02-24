from django.contrib import admin

from collection.models import Tool

class ToolAdmin(admin.ModelAdmin):
   model = Tool
   list_display = ('name', 'description',)
   prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Tool, ToolAdmin)
