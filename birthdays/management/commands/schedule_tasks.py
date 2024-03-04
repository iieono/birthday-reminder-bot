import schedule
import time
import threading
from django.core.management.base import BaseCommand
from birthdays.views import send_birthday_reminders

class Command(BaseCommand):
    help = 'Schedules tasks'

    def handle(self, *args, **options):
        def job():
            while True:
                schedule.run_pending()
                time.sleep(1)  

        scheduler_thread = threading.Thread(target=job)
        scheduler_thread.daemon = True  
        scheduler_thread.start()

        schedule.every().day.at("08:00").do(send_birthday_reminders)


        try:
            from django.core.management import call_command
            call_command('runserver', *args, **options)
        except KeyboardInterrupt:
            pass 
