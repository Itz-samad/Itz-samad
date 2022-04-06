from cgitb import html
from numpy import append
import pandas as pd
import csv
from fileinput import filename
import smtplib
import random
import imghdr
from email.message import EmailMessage
m = random.randint(000000, 999999)

def send_mail(to_rec, verification_otp):
    
    msg = EmailMessage()
    
    gmail_user = 'tzsamad17@gmail.com'
    gmail_password = 'Ayinkus12#'
    
    b = str('Please use this for your one time password: \n\t {}'.format(verification_otp))
    # b = 'hey'
    msg['Subject'] = 'OTP from naija baba'
    msg['From'] = gmail_user
    msg['to'] = to_rec
    msg.set_content(b)


    try:

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit
        print ("Email sent successfully!")
    except Exception as ex:  
        print ("Something went wrong….",ex)



# with open('email.csv', 'r')as f:
#     file = f.readline()
#     # print(file)
#     for i in file:
#         print(i)
#         # print(n)
#         # v = str(n)
#         # print(file)
#         # print(v)

e = pd.read_excel("Book1.xlsx")

print(e)
for i in e:
    print(i)
    m = random.randint(000000, 999999)
    send_mail(i, m)
    print(i)
    

