import pymongo
import os
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import dns

clientmos = os.getenv("clientm")
clientm = pymongo.MongoClient(clientmos)
newslettersdb = clientm.Newsletters
emaillistcol = newslettersdb.EmailList

count = 0
# for emaildoc in emaillistcol.find():
#   email = emaildoc['Email']
for email in ['[insert test email]']:
  print(email)
  context = ssl.create_default_context()
  MAILPASS = os.getenv("MAIL_PASS")
  MAIL = os.getenv("MAIL")
  f = open("newsletter.txt", "r")
  html = f.read()
  """
    <p><i>If you don't like this newsletter, then click <a href='https://vulcanwm.is-a.dev/unsubscribe/{str(emaildoc['_id'])}'>here</a> to unsubscribe to this newsletter!</i></p>
  </div>
  """
  message = MIMEMultipart("alternative")
  message["Subject"] = "VulcanWM's Newsletter"
  part2 = MIMEText(html, "html")
  message.attach(part2)
  sendermail = MAIL
  password = MAILPASS
  gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
  gmail_server.starttls(context=context)
  gmail_server.login(sendermail, password)
  message["From"] = sendermail
  message["To"] = email
  gmail_server.sendmail(sendermail, email, message.as_string())
  count = count + 1
print(count)