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
for emaildoc in emaillistcol.find():
  email = emaildoc['Email']
# for email in ['[insert test email]']:
  print(email)
  context = ssl.create_default_context()
  MAILPASS = os.getenv("MAIL_PASS")
  MAIL = os.getenv("MAIL")
  html = f"""
  <div style='font-family: 'Cairo', sans-serif;'>
    <h1>VulcanWM's Newsletter - 15/05/23</h1>
    <p>I haven't used this newsletter in a while now. But I'm just sending a new newsletter to update you on all the projects I've been working on this year!</p>
    <ul>
      <li><a href="https://vulcanwm.vercel.app/">Portfolio - Next.js</a>: February 2023</li>
      <li><a href="https://github.com/VulcanWM/login-signup-nextjs">Login Signup Next.js</a>: April 2023</li>
      <li><a href="https://discipulis.vercel.app/">Discipulis - v1.0.0</a>: January - April 2023</li>
      <li><a href="https://github.com/VulcanWM/random-app">First React Native App</a>: April 2023</li>
      <li><a href="https://global-css-art.vercel.app/">Global CSS Art</a>: April 2023</li>
      <li><a href="https://github.com/VulcanWM/github-actions-mongodb">GitHub Actions MongoDB</a>: May 2023</li>
      <li><a href="https://vulcanwm-guestbook.vercel.app/">VulcanWM GuestBook</a>: May 2023</li>
    </ul>
    <p>I'm working on a project called <a href="https://github.com/VulcanWM/github-readme-todolist">GitHub Readme TodoList</a> that will enable users to show a todolist on their GitHub readme and control all the tasks they want their profile viewers to see through a dashboard.</p>
    <p>I will also be redoing my portfolio soon to add some slight changes.</p>
    <p><strong>Thanks for reading this newsletter!</strong></p>
    <br>
  """
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