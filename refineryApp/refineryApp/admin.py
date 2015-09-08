from django.contrib import admin
from .models import Category, Workflow


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_Description', 'date_Created', 'last_Modified')
    ordering = ('id','category_name')

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'workflow_name', 'category', 'workflow_Description', 'workflow_Steps','date_Created', 'last_Modified')
    ordering = ('id','workflow_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)