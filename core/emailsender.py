import os
import smtplib

from config import Config

EMAIL_USERNAME = os.environ.get("EMAIL_ADDR", "myarea51acc@gmail.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS", "Abcd1234!")


class EmailSender:

    __Instance = None

    @staticmethod
    def Instance():
        if EmailSender.__Instance is None:
            EmailSender.__Instance = EmailSender()

        return EmailSender.__Instance

    def __init__(self):
        smtp_options = Config.Instance().get("smtp")
        smtp_server = smtp_options["server"]
        smtp_port = smtp_options["port"]

        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        self._smtp = smtp

    def __del__(self):
        self._smtp.close()

    def send_email(self, subject: str, body: str):
        msg = f"Subject: {subject}\n\n{body}"

        self._smtp.sendmail(EMAIL_USERNAME, EMAIL_USERNAME, msg)
