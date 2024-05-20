import os
import smtplib
import ssl

HOST = "smtp.gmail.com"
CONTEXT = ssl.create_default_context()
password = os.getenv("PASSWORD")
PORT = 465


def send_email():
    message = ("""\
Subject: Some object caught\n
There is some object front of me!
""")
    username = "emailexperimental70@gmail.com"
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(username, password=password)
        server.sendmail(username, username, message)
