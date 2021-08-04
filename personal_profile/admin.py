from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):

    list_display = ("title", "description", "picture", "link", "source_code", "tools")

class ContentAdmin(admin.ModelAdmin):

    list_display = ("para", "para2", "resume")


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Content, ContentAdmin)