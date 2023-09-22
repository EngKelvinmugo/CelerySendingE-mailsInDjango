
from django.shortcuts import render
from .tasks import fun
from django.http import HttpResponse
from mailfireapp.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json
# Create your views here.

def testView(request):
    fun.delay()
    return HttpResponse("Done")


def send_mail_to_all_users(request):
    send_mail_func.delay()
    return HttpResponse("Email has beed Sent Successfully")

def sendmailattime(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=20,minute=45)
    #we need to give name dynamically. now i am manually adding like mail_task_1
    task=PeriodicTask.objects.create(crontab=schedule,
    name="mail_task_"+"6",task='mailfireapp.tasks.send_mail_func')
    return HttpResponse("succcess")