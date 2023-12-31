import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender= ""
receiver = ""

message = MIMEMultipart()

message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello Again"

body = """
<h2> Hi There </h2>
There are only 2 cats flying today!
Lets hope more!
"""
mimetext = MIMEText(body,"html")
message.attach(mimetext)

attachpart = '/config/workspace/vinay2.txt'
attachment_file = open(attachpart,'rb')
payload = MIMEBase('application','octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition','attachment',filename = attachpart)
message.attach(payload)


server = smtplib.SMTP('smtp.office365.com',587)
server.startls()
server.login(sender,password)

message_text = message.as_string()
server.sendmail(sender,receiver,message_text)
server.quit()