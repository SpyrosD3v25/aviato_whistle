"""
This file is responsible for sending emails to email record. 
"""

import smtplib
from email.message import EmailMessage

class Send:
    def __init__(self):pass

    def send_email(self, subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "dhmosxyzpyrosbestikh@gmail.com"
        msg['from'] = user
        password = "dxvyciqaenrbmdnq"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        print(msg)
        server.send_message(msg)

        server.quit()

