from django.conf.urls import patterns, include, url
from rest_framework import routers
from person import views

router = routers.DefaultRouter()
router.register(r'person', views.FacebookUserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
