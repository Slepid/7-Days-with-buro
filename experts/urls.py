from django.urls import path
from django.urls import re_path
from .import views
urlpatterns = [

	path('index1', views.index1),
	path('expert', views.expert),
	path('expert_about', views.expert_about),
	path('meropriatia', views.meropriatia),
	path('expert_mean',views.expert_mean),
	path('projects', views.projects),
	path('donate', views.donate),
	path('profile', views.profile),
	
]

