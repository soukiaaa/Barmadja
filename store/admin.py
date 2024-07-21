from django.contrib import admin
from . models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(service, ServiceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(project, ProjectAdmin)


