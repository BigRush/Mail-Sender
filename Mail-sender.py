#!/usr/bin/env python3.6

import smtplib
import getpass

User_Mail = input("Please enter your email: ")
Rec_Mail = input("Please enter the recipient's mail: ")
Msg_Subject = input("Please enter the subject: ")



Passwd_Mail = getpass.getpass("Please enter your password: ")
Server_Mail = smtplib.SMTP('smtp.gmail.com',587)

Server_Mail.starttls()

Server_Mail.login(User_Mail, Passwd_Mail)

Msg_Content = input("Please enter your message: ")
Server_Mail.sendmail(User_Mail, Rec_Mail, Msg_Content)

Server_Mail.quit()
