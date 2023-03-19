import smtplib, ssl
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import path

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "xxxxxxxxxx@gmail.com"
receiver_email = "xxxxxxxxxcv@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there
Im sending an email through python code."""
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)