from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns

from projectmanager.views import ProjectList, ProjectDetail

urlpatterns = []

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += format_suffix_patterns(
    patterns('projectmanager.views',
        url(r'^$', 'home'),
        url(r'^browse/$', 'api_root'),
        url(r'^projects/$', ProjectList.as_view(), name="project-list"),
        url(r'^project/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name="project-detail")
    )
)