import os
import smtplib


#This class is responsible for sending notifications with the deal.
class NotificationManager:
    def __init__(self):
        self._mail = os.environ['MY_MAIL']
        self._password = os.environ["MY_PASSWORD"]
        self._connection = smtplib.SMTP("smtp.gmail.com", port=587)

    def send_email(self, message):
        with self._connection as connection:
            connection.starttls()
            connection.login(self._mail, self._password)
            connection.sendmail(from_addr=self._mail, to_addrs=self._mail, msg=message)
