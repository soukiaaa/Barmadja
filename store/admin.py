from django.contrib import admin
from . models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    
    def photo(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['designation','description','photo',]
    list_filter = ('designation', )
    search_fields = ('designation', )
admin.site.register(service, ServiceAdmin)

class ProjectAdmin(admin.ModelAdmin):

    def photo(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['title','photo', 'description', 'service']
    list_filter = ('title', 'service', )
    search_fields = ('title', )
admin.site.register(project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'isregistred', 'project', 'datec')
    list_filter = ('isregistred', 'project', 'datec' )
    search_fields = ('name', )
admin.site.register(client, ClientAdmin)

class CategoryAdmin(admin.ModelAdmin):

    def photo(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['designation','photo', 'description']
    search_fields = ('designation', )
admin.site.register(category, CategoryAdmin)


