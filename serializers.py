from rest_framework import serializers
from .models import Task
from .models import Tasklist
from .models import Tag
from .models import Owner

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed', 'date_created', 'date_modified', 'due_date', 'priority','tasklist','Tag','User')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):

        return Task.objects.create(**validated_data)




class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tasklist
        fields = ('name', 'tasks')


class TagSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = ('name', 'tasks')

class OwnerSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = ('name', 'tasks')