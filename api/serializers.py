from rest_framework import serializers

from api import models


class CustomTaskSerializer(serializers.ModelSerializer):
    """Custom serializer for task object in tile serializer"""
    task_type = serializers.CharField(source='get_task_type_display')

    class Meta:
        model = models.Task
        exclude = ('tile', )


class CustomTileSerializer(serializers.ModelSerializer):
    """Custom serializer for tile object in task serializer"""
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = models.Tile
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for task objects"""

    class Meta:
        model = models.Task
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['tile'] = CustomTileSerializer(instance.tile).data
        ret['task_type'] = instance.get_task_type_display()
        return ret


class TileSerializer(serializers.ModelSerializer):
    """Serializer for tile objects"""
    
    class Meta:
        model = models.Tile
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        tasks = models.Task.objects.filter(tile=instance)
        ret['tasks'] = CustomTaskSerializer(tasks, many=True).data
        ret['status'] = instance.get_status_display()
        return ret
