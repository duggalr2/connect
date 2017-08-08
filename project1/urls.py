"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from connect import views as core_views
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^connect/', core_views.landing_page, name='landing_page'),
    url(r'^create/', core_views.profile_creation, name='profile_creation'),
    url(r'^finish/', core_views.creation_finish, name='creation_finish'),
    url(r'^main/', core_views.main_page, name='main_page'),
    url(r'^profile/', core_views.edit_profile, name='main_profile'),
    url(r'^feature/', core_views.feature_request, name='feature_request'),
    url(r'^logout/$', views.logout, {'next_page': '/connect/'}, name='logout'),
    url(r'password_change/$', core_views.change_password, name='password_change')
    # url(r'^login/$', views.login, {'template_name': 'landing_page.html'}, name='login'),
]

