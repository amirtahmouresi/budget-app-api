from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budget import views


router = DefaultRouter()
router.register('tag', views.TagViewSet)

app_name = 'budget'

urlpatterns = [
    path('', include(router.urls))
]
