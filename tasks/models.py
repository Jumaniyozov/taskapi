from django.db import models


class Task(models.Model):
    is_complete_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} task'


class StatusValue(models.TextChoices):
    BOSHLANMAGAN = "BOSHLANMAGAN", "Boshlanmagan"
    ARAFASIDA = "ARAFASIDA", "Yopilish arafasida"
    TOLANDI = "TOLANDI", "To'landi"


class Project(models.Model):
    customer_id = models.IntegerField()
    adress = models.CharField(max_length=255)
    project_sum = models.FloatField()
    status = models.CharField(max_length=15, choices=StatusValue.choices, default=StatusValue.BOSHLANMAGAN)
    customer_inn = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    json_body = models.JSONField(null=True)
    left_amount = models.FloatField()
    task = models.ForeignKey(Task, related_name="projects", on_delete=models.CASCADE)
