import os
import time

from dotenv import load_dotenv

import requests

from twilio.rest import Client

load_dotenv()


def get_status(user_id):
    url = 'https://api.vk.com/method/users.get'
    token = os.getenv('VK_TOKEN')
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'v': '5.92',
        'access_token': token
    }
    is_online = (requests.post(url, data=None, params=params).json()[
        'response'][0]['online'])
    return is_online


def sms_sender(sms_text):
    print('online!')
    account_sid = os.getenv('twilio_account_sid')
    auth_token = os.getenv('twilio_auth_token')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_text,
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO')
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
