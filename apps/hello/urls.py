from django.conf.urls import patterns, url
from apps.hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	
	urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	)
	urlpatterns += staticfiles_urlpatterns()