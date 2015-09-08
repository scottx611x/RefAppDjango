__author__ = 'scott'

from tastypie.resources import ModelResource
from tastypie import fields
from .models import Category, Workflow

class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all().order_by('id')
        resource_name = 'category'



class WorkflowResource(ModelResource):

    category = fields.ToOneField(CategoryResource, 'category',full=True)

    class Meta:
        queryset = Workflow.objects.all().order_by('id')
        field_order = ('category', 'id', 'workflow_name', 'workflow_Description', 'workflow_Steps', 'date_Created', 'last_Modified')
        resource_name = 'workflow'

    def build_schema(self):
        schema = super(WorkflowResource, self).build_schema()
        schema['field_order'] = self._meta.field_order
        return schema