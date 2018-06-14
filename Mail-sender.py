#!/usr/bin/env python3.6

import smtplib
import getpass


Rec_Mail = input("Please enter the recipient's mail: ")
Msg_Subject = input("Please enter the subject: ")
Msg_Content = input("Please enter your message: ")

Server_Mail = smptlib.SMTP("smpt.gmail.com",587)

Server_Mail.starttls()

User_Mail = input("Please enter your email: ")
while not User_Name.isalnum():
    print("You must enter only alphanumeric characters, try again...")
    User_Name = input("Please enter your email: ")


Passwd_Mail = getpass.getpass("Please enter your password: ")

Server_Mail.login(User_Mail, Passwd_Mail)

Server_Mail.sendmail(Rec_Mail, Msg_Content)

Server_Mail.quit()
