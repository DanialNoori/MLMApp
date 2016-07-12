"""MLMApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import handler400, handler403, handler404, handler500
from errors import views

handler404 = 'errors.views.page_not_found_view'
handler500 = 'errors.views.server_error_view'
handler403 = 'errors.views.permission_denied_view'
handler400 = 'errors.views.bad_request_view'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('users.urls')),
    url(r'^accounts/', include('webuser.urls')),
]



