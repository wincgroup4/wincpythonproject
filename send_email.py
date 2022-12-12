# Send EMAIL functionality
# '''
# @author: WinC Python project Group4
# """
from email.message import EmailMessage
import smtplib
from vardata import *
from utilities import catch_exception

@catch_exception
def sendEmail(msg_body):
    response = 0
    server = smtplib.SMTP(smtp_domain, smtp_port)
    server.starttls()
    server.login(mail_from_addr, mail_app_password)
    message = EmailMessage()
    message['Subject'] = str(mail_subject)
    message['From'] = str(mail_to_addr)
    message.set_content(str(msg_body))
    message['To'] = mail_to_addr
    response = server.send_message(message)
    server.quit()
    return response
