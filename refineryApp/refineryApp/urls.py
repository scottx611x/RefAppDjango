from django.contrib import admin
from django.conf.urls import patterns, include, url

from .api import CategoryResource, WorkflowResource

category_resource = CategoryResource()
workflow_resource = WorkflowResource()

urlpatterns = patterns('',
    url(r'^v1/', include(category_resource.urls)),
    url(r'^v1/', include(workflow_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
                       )

