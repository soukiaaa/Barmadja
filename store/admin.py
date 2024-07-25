from django.contrib import admin
from . models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(service, ServiceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(client, ClientAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(category, CategoryAdmin)


