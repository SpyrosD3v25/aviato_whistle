"""
This file is responsible for sending mms to the number phone_num parameter passed in here. 
"""

import os
from twilio.rest import Client

class Send:
    def __init__(self, category, img_path, phone_num):
        self.category = category
        self.img_path = img_path
        self.phone_num = phone_num

    def send_mms(self):
        account_sid = os.environ['AC206912c5dae838a7d663beacaa59058d']
        auth_token = os.environ['2f992eb4ee9daad8ea1c45a9ae53cee0']
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=self.category,
                media_url=self.img_path,
                from_='+8596597987',
                to=self.phone_num
            )

        print(message.sid)

    if __name__ == '__main__':
        send_mms()
