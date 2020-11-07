from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('tile', views.TileRetrieveUpdateDestroyViewSet)
router.register('tile', views.TileCreateListViewSet)
router.register('task', views.TaskRetrieveUpdateDestroyViewSet)
router.register('task', views.TaskCreateListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]