from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Website urls
    url(r'^2013/', include('website.urls', namespace='website')),
    url(r'^', include('website.urls', namespace='website')),
    # Accounts urls
    url(r'accounts/login/$', 'scipy.views.user_login'),
    url(r'accounts/logout/$', 'scipy.views.user_logout'),
    url(r'accounts/register/$', 'scipy.views.user_register'),
    url(r'accounts/profile/$', 'scipy.views.user_profile'),
    url(r'accounts/upload-document/$', 'scipy.views.upload_document', name='upload-document'),
    # Reusing the admin password reset
    url(r'accounts/password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'accounts/password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
