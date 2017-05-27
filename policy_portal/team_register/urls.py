from django.conf.urls import url

from . import views

urlpatterns = [

	 url(r'^$', views.team_registration, name='team_registration'),
	 # url(r'^team/create/$', views.TeamCreate.as_view(), name='team_create'),
	 # url(r'^member/create/$', views.MemberCreate.as_view(), name='member_create'),
	 

	 

]