from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(),
        name='mytardis_openid_login.login'),
]
