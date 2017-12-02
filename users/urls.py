from django.conf.urls import url
from users import views

urlpatterns = [
	url(r'^register$', views.UserRegisterViewSet.as_view()),
	url(r'^login$', views.UserLoginViewSet.as_view()),
	url(r'^logout$', views.UserLogoutViewSet.as_view())
]