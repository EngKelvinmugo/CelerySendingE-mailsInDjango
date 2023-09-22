from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryproject.settings")
app = Celery("celeryproject")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Africa/Nairobi')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")#celery beat settings
#celery beat settings
app.conf.beat_schedule={
    'send-mail-everyday-at-7':{
        'task':'mailfireapp.tasks.send_mail_func',
        'schedule': crontab(hour=00,minute=10),
        # we can pass arguments here and we can use those in
        # firemailapp/tasks.py send_mail_func function for 
        # that you need one extra argument in your function
        # currently we are not doing that
        # 'args': (1000,)  
    }
}