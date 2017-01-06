
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import UserApiView



urlpatterns = [
    url(r'^$', UserApiView.as_view(), name='api-view'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
