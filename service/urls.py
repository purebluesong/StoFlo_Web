import views
from django.conf.urls import include, url

urlpatterns = [
	url(r'^index/$', views.index),
	url(r'^$', views.index),
]

urlpatterns += [
	url(r'^login$', views.login),
	url(r'^regeister',views.regeister),	
]