import redis
import json
import the
From time import sleep
from random import randint

from email. mime. multipart import MIMEMultipart
from email. mime.  mimetext import
smtplib import

if __name__ == '__main__':
    redis_host = os. getenv('REDIS_HOST', 'queue')
    email = os. getenv('EMAIL', 'NOT INFORMED')
    password = os. getenv('PASSWORD', 'NOT INFORMED')
    servidor_email = os. getenv('EMAIL_SERVER', 'NOT INFORMED')
    porta_servidor_email = the. getenv('PORT_EMAIL_SERVER', 'UNINFORMED')
    r = redis. Redis(host=redis_host, port=6379, db=0)
    print('Waiting for messages!!!')
    while true:
        message = json. loads(r. blpop('sender')[1]])

        if email == 'UNREPORTED' or email == 'conta_email@dominio.com.br' \
        or password == 'senha_conta_email' or password == 'UNREPORTED'  \
        or servidor_email == 'UNREPORTED' \
        or porta_servidor_email == 'UNINFORMED':
            # Simulating email sending
            print('Sending message: ', message['subject'])
            sleep(randint(15, 45))
            print('Message', message['subject'], 'sent')
        else:
            # Email Sending
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = email
            msg['Subject'] = message['subject']
            msg. attach(MIMEText,'message'], 'plain'))

            print('EMAIL AUTHENTICATION')
            server = smtplib. SMTP ({0}: {1}'. format format(
                servidor_email, porta_servidor_email))
            server. Starttls()
            server. login(msg['From'], password)
            print('EMAIL AUTHENTICATED')
            server. sendmail(msg['From'], msg['To'], msg. as_string())
            print("Email successfully sent to: ", (msg['To']))
            server. Quit()
