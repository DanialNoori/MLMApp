from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^validate/', views.validate_registration),
    url(r'^register/complete/', views.fullRegistration),
    url(r'^register/upline/', views.parentObject),
    url(r'^main/info/', views.mainPage),
    url(r'^main/profile/', views.profilepage),
    url(r'^main/notifs/', views.notifications),
    url(r'^parentvalidation/', views.parentValidation),
    url(r'^tasks/$', views.tasklist),
    url(r'^tasks/accomplished/', views.taskaccomplished)
]