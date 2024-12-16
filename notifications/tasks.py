from celery import shared_task
import requests

@shared_task
def send_sms(recipient, message):
 
    api_url = ""
    payload = {
        'recipient': recipient,
        'message': message
    }
    headers = {
        'Authorization': '', 
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return f"SMS sent to {recipient}"
    else:
        return f"Failed to send SMS to {recipient}. Status: {response.status_code}, Response: {response.text}"
