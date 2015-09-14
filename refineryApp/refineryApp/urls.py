from django.contrib import admin
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from .api import CategoryResource, WorkflowResource
import views

v1_api = Api(api_name='v1')

v1_api.register(CategoryResource())
v1_api.register(WorkflowResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
                    url(r'^categorys$', views.categorys, name='categorys'),
                    url(r'^workflows$', views.workflows, name='workflows'),

    )

