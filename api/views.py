from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from api import models, serializers


class TileBaseViewSet(viewsets.GenericViewSet):
    """Tile base view set with basic attributes"""
    queryset = models.Tile.objects.all()
    serializer_class = serializers.TileSerializer


class TileRetrieveUpdateDestroyViewSet(TileBaseViewSet,
                                        mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        mixins.DestroyModelMixin):
    """
    Tile retrieve, update, destroy view sets
    """
    pass


class TileCreateListViewSet(TileBaseViewSet,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin):
    """
    Tile create, list view sets.
    """
    pass


class TaskBaseViewSet(viewsets.GenericViewSet):
    """Task base view set with basic attributes"""
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskRetrieveUpdateDestroyViewSet(TaskBaseViewSet,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin):
    """
    Task retrieve, update, destroy view sets
    """
    pass


class TaskCreateListViewSet(TaskBaseViewSet, 
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin):
    """
    Task create, list view sets.
    """
    pass
