from django import urls
#from django.conf.urls import include, urls
from users.views import dashboard
from django.urls import path, include

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]