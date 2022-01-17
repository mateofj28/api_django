from posixpath import basename
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

# instantiate the route
router = DefaultRouter()

# register the route
router.register('hello_viewSet', views.HelloViewSet, basename='hello_viewSet')
router.register('profile', views.UserProfileViewSet)

# configurations patterns

# as_view() to load function http, not class

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)), # add the route
]