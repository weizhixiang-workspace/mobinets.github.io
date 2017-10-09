# HTML code generation and mail notification

Files needed: 
1. gen.py -- the main script
2. mail.personal -- the information required for email

##Prepare mail.personal

Before using the script, you need to create a file named ``mail.personal``, containing the necessary information for sending emails. 
The template for creating ``mail.personal`` is given as follows:

``
[mailhost]:smtp.exmail.qq.com
[mailport]:465
[mailuser]:USERNAME@mobinets.org
[mailpass]:PASSWORD
[from]:USERNAME@mobinets.org
[to]:notice@mobinets.org
``

Please fill the username and password only.
DO NOT change the above format.
Note: This file will not be uploaded to github and is available only to yourself.

##Usage

1. python gen.py
2. Input the required information.
3. Confirm the information and update/notify by input ``y''.

Required information and input format: 
1. date (e.g., 17/10/13)
2. address (e.g., B1-501)
3. conf name (e.g., INFOCOM'17, TOSN'17, TechRep)
4. paper title
5. download link (remember to add http:// in the url)
6. presenter name 