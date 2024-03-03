import datetime
from django.http import HttpResponse

from django.shortcuts import render
from .models import Employee
from django.conf import settings
import base64
from django.views.decorators.csrf import csrf_exempt
from .utils import send_telegram_message

def send_birthday_reminders():
    print("call reminder")
    # Get today's date
    today = datetime.date.today()
    # Find employees whose birthday is today
    employees = Employee.objects.filter(
        birth_date__month=today.month,
        birth_date__day=today.day
    )
    # Find admin users
    admin_users = Employee.objects.filter(roles__role_name='admin')  # Assuming 'admin' is the name of the admin role
    if employees.exists() and admin_users.exists():
        for employee in employees:
            for admin in admin_users:
                # Get employee image
                image_data = None
                if employee.image:
                    # Read image data and encode it in base64
                    with open(employee.image.path, "rb") as img_file:
                        image_data = base64.b64encode(img_file.read())
                else:
                    image_data = None
                # Compose message with image
                current_date = datetime.datetime.now().strftime("%B %d").replace(" 0", " ").replace(" 1", " 1st").replace(" 2", " 2nd").replace(" 3", " 3rd") + "th"
                birth_year = employee.birth_date.strftime("%Y")
                age = datetime.datetime.now().year - employee.birth_date.year
                suffix = "th" if 11 <= age <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(age % 10, "th")
                message = f"🎉 Today {current_date} is {employee.first_name} {employee.last_name}'s {age}{suffix} birthday! 🎂🥳 He was born in {birth_year}. "
                message += f"Let's celebrate this special day together. Wishing {employee.first_name} all the happiness and success in the year ahead!\n"
                message += f"Don't forget to congratulate {employee.first_name} on this joyous occasion! 🎈🎉"
                send_telegram_message(token=settings.TELEGRAM_BOT_TOKEN, chat_username=admin.telegram_chat_id, text=message, image_data=image_data)

def send_messages(request):
    if request.method == 'POST':
        employees = Employee.objects.all()
        table = "+--------------------------------------------------+----------------+\n"
        table += "| Full Name                                        | Birthday       |\n"
        table += "+--------------------------------------------------+----------------+\n"

        for employee in employees:
            full_name = employee.get_full_name()
            birthday = employee.birth_date.strftime("%Y-%m-%d") if employee.birth_date else ""
            table += "| {:<50} | {:<15} |\n".format(full_name, birthday)

        table += "+--------------------------------------------------+----------------+"

        admin_users = Employee.objects.filter(roles__role_name='admin')
        for admin in admin_users:
            send_telegram_message(token=settings.TELEGRAM_BOT_TOKEN, chat_username=admin.telegram_chat_id, text=table)


        # Send the message to the Telegram channel

        return HttpResponse('Message sent successfully!')
    else:
        return render(request, 'send_requests_page.html', {})       
        
        
        
# return render(request, 'send_requests_page.html', {})
    