from django.contrib import admin
from django.urls import path, include

from .views import TasksToDo, CompletedTasks, delete_task, finish_task

urlpatterns = [
    path('to_do_tasks/', TasksToDo.as_view(), name='to_do_tasks'),
    path('completed_tasks/', CompletedTasks.as_view(), name='completed_tasks'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('finish/<int:id>/', finish_task, name='finish_task'),
]