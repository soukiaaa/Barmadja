from django.contrib import admin
from . models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('designation', 'description', 'admin_photo')
    list_filter = ('designation', )
    search_fields = ('designation', )
admin.site.register(service, ServiceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'service')
    list_filter = ('title', 'service', )
    search_fields = ('title', )
admin.site.register(project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'isregistred', 'project', 'datec')
    list_filter = ('isregistred', 'project', 'datec' )
    search_fields = ('name', )
admin.site.register(client, ClientAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('designation', 'image', 'description')
    search_fields = ('designation', )
admin.site.register(category, CategoryAdmin)


