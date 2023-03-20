import os
import smtplib
from email.message import EmailMessage
import mimetypes
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

current_dir = Path(__file__).resolve().parent if '__file__' in locals() else Path.cwd()
envars = current_dir / 'cred.env'
sender_email = os.getenv('email')
sender_password = os.getenv('password')

def File_attachment(fileToSend,msg):
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()

    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)


def send_mail():
    fileToSend = r'Images/steam_data.csv'
    htmAttach = r'Images/discount_graph.png'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Hello there!Check out the cool steam sales this week!'
    msg['From'] = sender_email
    msg['To'] = sender_password

    csv_file = r'Images/steam_data.csv'
    htm = r'Images/discount_graph.png'
    File_attachment(csv_file,msg)
    File_attachment(htm,msg)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email,sender_password)

        smtp.send_message(msg)

send_mail()