from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests as r

# create message object instance 
msg = MIMEMultipart()

message = f'Здравствуйте, Mav.'
 
# setup the parameters of the message 
password = ""
msg['From'] = ""
msg['To'] = ""
msg['Subject'] = ""
 
# add in the message body 
msg.attach(MIMEText(message, 'plain'))
 
#create server 
server = smtplib.SMTP('server: port')
 
server.starttls()
 
# Login Credentials for sending the mail 
server.login(msg['From'], password)
 
 
# send the message via the server. 
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print(f'Письмо успешно отправлено {msg['To']}')
