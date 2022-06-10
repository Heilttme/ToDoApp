from datetime import datetime

from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    additional_information = models.CharField(max_length=1000)
    time_expiration = models.DateTimeField(default=datetime.now(), null=True)
    user = models.ForeignKey('authentication.UserToDo', on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
