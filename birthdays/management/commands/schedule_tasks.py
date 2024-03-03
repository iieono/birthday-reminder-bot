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
                time.sleep(1)  # Check every second

        # Create a thread for running the scheduler loop
        scheduler_thread = threading.Thread(target=job)
        scheduler_thread.daemon = True  # Daemonize the thread to stop it when the main thread exits
        scheduler_thread.start()

        # Schedule the task to run every 30 seconds
        schedule.every(10).seconds.do(send_birthday_reminders)
        # schedule.every().day.at("08:00").do(send_birthday_reminders)

        # Continue with runserver
        try:
            from django.core.management import call_command
            call_command('runserver', *args, **options)
        except KeyboardInterrupt:
            pass  # Allow clean exit on KeyboardInterrupt
