from django.conf.urls import url

from . import views
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views

from .views import PostViewSet

app_name = 'mediahub'
router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post', views.add_post, name='add_post'),
    path('search', views.search, name='search'),
    path('api/', include(router.urls)),
    path('accounts/login/', auth_views.LoginView.as_view()),

]
