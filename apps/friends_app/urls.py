from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^add_friend/(?P<id>\d+)$', views.add_friend, name='add_friend'),
    url(r'^remove_friend/(?P<id>\d+)$', views.remove_friend, name='remove_friend'),
	url(r'^view_profile/(?P<id>\d+)$', views.view_profile, name='view_profile'),
]
