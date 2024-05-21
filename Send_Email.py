import os
from email.message import EmailMessage
import smtplib
import imghdr

HOST = "smtp.gmail.com"
PASSWORD = os.getenv("PASSWORD")
PORT = 587
SENDER = "emailexperimental70@gmail.com"
RECEIVER = "emailexperimental70@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "New Client appeared!"
    email_message.set_content("There is a new client chief!")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(HOST, PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(RECEIVER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())


if __name__ == "__main__":
    send_email("images/10.png")