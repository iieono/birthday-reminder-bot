from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import schedule
import time

from birthdays.views import send_birthday_reminders, send_messages 
from birthdays.management.commands.schedule_tasks import Command as ScheduleTasksCommand


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', send_messages, name='send_messages'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

ScheduleTasksCommand().handle()