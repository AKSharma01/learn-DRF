"""voting_system URL Configuration

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
from rest_framework.urlpatterns import format_suffix_patterns
# from django.contrib import admin
from rest_framework import routers
from parties import views as parties_view
from users import views as users_view

router = routers.DefaultRouter()
router.register(r'parties', parties_view.PartyViewSet, 'party')
router.register(r'votes', parties_view.VotebankViewSet, 'votes')
router.register(r'users', users_view.UsersViewSet, 'users')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('users.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
