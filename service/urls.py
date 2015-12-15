import views
from django.conf.urls import include, url

urlpatterns = [
	url(r'^index/$', views.index),
	url(r'^$', views.index),
]

urlpatterns += [
	
]