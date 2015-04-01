from django.conf.urls import patterns, url
from apps.hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	
	urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^requests/', 'views.requests'),
	urlpatterns += staticfiles_urlpatterns()