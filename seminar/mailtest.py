#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

presenter1="1"
presenter2="2"
date="3"
conf1="4"
conf2="5"
title1="6"
title2="7"

fm = open('mail.personal')
for line in fm.readlines():
	line = line.strip('\n')
	if "[mailhost]" in line:
		tmp = line.split(':')
		mailhost = tmp[1]
	if "[mailuser]" in line:
		tmp = line.split(':')
		mailuser = tmp[1]
	if "[mailpass]" in line:
		tmp = line.split(':')
		mailpass = tmp[1]
	if "[mailport]" in line:
		tmp = line.split(':')
		mailport = tmp[1]
	if "[from]" in line:
		tmp = line.split(':')
		sender = tmp[1]
	if "[to]" in line:
		tmp = line.split(':')
		receiver = tmp[1]
fm.close()
mainmsg = """
	<p>Dear all, 
	<br/>
	%s and %s will present two research works as follows on %s.
	<br/>
	1. %s, %s
	<br/>
	2. %s, %s
	<br/>
	Please find the details and download the papers at
	<a href="http://mobinets.org/seminar">http://mobinets.org/seminar</a>
	<br/>
	<br/>
	Best regards, 
	<br/>
	MobiNets
	</p>
	"""%(presenter1,presenter2,date,conf1,title1,conf2,title2)

message = MIMEText(mainmsg, 'html', 'utf-8')
message['From'] = Header("组会from", 'utf-8')
message['To'] =  Header("组会to", 'utf-8')

subject = '%s组会通知'%(date)
message['Subject'] = Header(subject, 'utf-8')

try:
    smtp = smtplib.SMTP_SSL()
    # smtp.ehlo()
    smtp.connect(mailhost,mailport)
    smtp.login(mailuser,mailpass)
    smtp.sendmail(sender, receiver, message.as_string())
    print "邮件发送成功"
except Exception as e:  
    print e
