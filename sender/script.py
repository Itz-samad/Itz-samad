import pandas as pd
import smtplib

SenderAddress = "<olabodealbert205@gmail.com>"
password = "@Olabode205"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values 
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()