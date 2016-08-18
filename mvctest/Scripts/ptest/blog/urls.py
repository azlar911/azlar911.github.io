from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^hello_world$', views.hello_world),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
]
