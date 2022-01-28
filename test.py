import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()


from_email = 'gavnuq321@gmail.com'
password = 'onnh vnzs giwp tiwy'

recipient = 'lakidaki228@gmail.com'
message = 'registration completed successfully'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, recipient, msg.as_string())
server.quit()
