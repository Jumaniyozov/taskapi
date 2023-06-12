import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from .models import Project, Task, StatusValue
from .serializer import TaskSerializer, ProjectSerializer


@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    projects = []

    for task in tasks:
        project = Project.objects.filter(task_id=task.id)[0]
        proj_temp = project.__dict__
        proj_temp.pop("_state")
        tas_temp = task.__dict__
        tas_temp.pop("_state")

        projects.append({
            "task": tas_temp,
            "project": proj_temp,
        })

    return Response(projects)


@api_view(["POST"])
def make_payment(request):
    try:
        json_data = json.loads(request.body)

        project = Project.objects.get(pk=json_data["project_id"])
        task = Task.objects.get(id=project.task_id)

        if task.is_complete_status:
            return Response({"message": f"Ushbu proyekt yopilgan va to'lov to'liq amalga oshirilgan"})

        left_amount = project.left_amount - json_data["amount"]
        if left_amount < 0:
            return Response({"message": f"siz keradigan ortiqcha {abs(left_amount)} summaga to'lov amalga oshiryapsiz"})

        project.left_amount = left_amount

        if project.json_body is None:
            project.json_body = [{"order": 1, "amount": json_data["amount"]}]
        else:
            project.json_body = [*project.json_body, {"order": len(project.json_body) + 1, "amount": json_data["amount"]}]

        percentage = 100 - (project.left_amount * 100 / project.project_sum)
        # print(percentage)

        if percentage == 100:
            project.status = StatusValue.TOLANDI
            task.is_complete_status = True
        elif percentage < 50.0:
            project.status = StatusValue.BOSHLANMAGAN
        elif percentage > 50.0:
            project.status = StatusValue.ARAFASIDA

        project.save()
        task.save()

        data = project.__dict__
        data.pop("_state")
        temp_task = task.__dict__
        temp_task.pop("_state")
        # data = serializers.serialize("json", project)
        # print(data)

        return Response({"project": data, "task": temp_task})
    except Exception as e:
        print(e)
        return Response({"message": "bad request. try again"}, status=400)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created')
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
