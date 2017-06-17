from django.conf.urls import url

from . import views

urlpatterns = [

	 url(r'^phase_1_upload/$',views.phase_1_upload, name='phase_1_upload'),
	 url(r'^$',views.dashboard, name='dashboard'),

	 

]