from django.urls import path,re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Profile import views

urlpatterns=[
   re_path(r'^lista/$', views.ProfileList.as_view()),
   re_path(r'^editprofile/(?P<pk>\d+)/$',views.ProfileDetail.as_view()),
   re_path(r'^img/$',views.FileUploadView.as_view()),
]