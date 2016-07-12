from django.conf.urls import url, include
from .import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^register/complete', views.fullRegistration),
    url(r'^validate/' , views.validate_registration),
    url(r'^validate-email/' ,views.validateEmail),
    url(r'^upline-proposal/', views.parentObject),
    url(r'^logout/', views.logout)
]