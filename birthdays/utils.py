import requests
from django.conf import settings
import base64

def send_telegram_message(token, chat_username, text, image_data=None):
    

    if image_data:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendPhoto"
        files = {"photo": ("image.jpg", base64.b64decode(image_data), "image/jpeg")}
        data = {"chat_id": chat_username, "caption": text}
        response = requests.post(url, data=data, files=files)
    else:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": chat_username, "text": text}
        response = requests.post(url, data=data)

    if response.status_code != 200:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging
    else:
        print("Message sent successfully.")

