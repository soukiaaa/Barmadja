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

    list_display = ['title','photo', 'description', 'services']
    list_filter = ('title', 'services', )
    search_fields = ('title', )
admin.site.register(project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'isregistred', 'project', 'datec')
    list_filter = ('isregistred', 'project', 'datec' )
    search_fields = ('name', )
admin.site.register(client, ClientAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service','type', 'datec', 'description')
    list_filter = ('name', 'service', 'datec', 'type')
    search_fields = ('name', 'phone')
admin.site.register(customer, CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):

    def photo(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['designation','photo', 'description']
    search_fields = ('designation', )
admin.site.register(category, CategoryAdmin)

class ProjectsAdmin(admin.ModelAdmin):

    def photo(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['title','photo', 'description', 'price']
    list_filter = ('price', 'title', )
    search_fields = ('title', )
admin.site.register(projects, ProjectsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('datec', 'proj', 'content')
    list_filter = ('proj', 'datec' )
admin.site.register(comment, CommentAdmin)

class CustomerPrjAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'datec', 'prj', 'description')
    list_filter = ('prj', 'datec' )
admin.site.register(customerPrj, CustomerPrjAdmin)

