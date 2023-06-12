from rest_framework import serializers

from tasks.models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


# class MyTasksSerializer(serializers.ModelSerializer):
#     projects = serializers.SerializerMethodField()
#     # etc..
#     class Meta:
#         model = Task
#         fields = "__all__"
#
#     def get_projects(self, obj):
#         tasks = Task.objects.filter(pk=self.context['request'].,quiz=obj)
#         return QuizTakerSerializer(quiztakers, many=True).data
