from django.contrib import admin
from .models import Category, Workflow


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_Description', 'date_Created', 'last_Modified')

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('workflow_name', 'category', 'workflow_Description', 'workflow_Steps','date_Created', 'last_Modified')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)