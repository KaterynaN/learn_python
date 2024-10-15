import os
from twilio.rest import Client
import smtplib


#This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self._mail = os.environ["MY_MAIL"]
        self._password = os.environ["MY_PASSWORD"]
        self._connection = smtplib.SMTP("smtp.gmail.com", port=587)

    def send_message(self, message_body):
        message = self.client.messages.create(
            from_=os.environ.get('FROM_TWILIO_WHATSAPP_NUMBER'),
            body=message_body,
            to=os.environ.get('TO_TWILIO_WHATSAPP_NUMBER')
        )
        print(message.status)
        print(message.sid)

    def send_email(self, email, message):
        with self._connection.starttls():
            self._connection.login(self._mail, self._password)
            self._connection.sendmail(from_addr=self._mail, to_addrs=email, msg=message)
