# Sending EMails

> Python has built in libraries to send and receive simple and complex emails.

> Python supports sending email through an smtp server

> Receiving E-Mails can be done via Pop3 or IMAP protocal, both supported by Python

> The smtplib library can be used to send out E-Mails

> Plain Text, HTML, E-Mail with attachments etc.. Can be sent

> Free smtp servers from gmail and yahoo  e-mail accounts can be used for sending E-Mails

**Example**

```Python

# Import smtplib and MIME libraries

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Create the smtp connection to gmail's smtp server
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


#The from and to addresses
from_email = 'from@gmail.com'
to_email = 'to@gmail.com'

#Create the EMail MIME object
msg = MIMEMultipart()
msg['Subject'] = 'EMail from Python'
msg['From'] = from_email

msg['To'] = to_email
body = 'E-Mail Body'
msg.attach(MIMEText(body, 'plain'))


#log in to the server using gmail username and password
smtpserver.login('username', 'password')

#Send the E mail
text = msg.as_string()
smtpserver.sendmail(from_email, to_email, text)


#E-Mail should be in the inbox


```


# Exercise

**Use Case**

> Tom will be visiting New York City from 9/22/2018 to 9/25/2018
> Tom visits expedia.com everyday to check the hotel prices for the date range
> Tom would like someone to automate this for him

**Requirements**

> Get NYC hotel prices from expedia.com for the date range 9/22/2017 to 9/25/2017
> Store them in a DB with the date they were extracted
> The DB should include Hotel Name, Hotel Price and Search Date
> E-Mail the list of hotels to Tom after the search is complete as a CSV file

**Project Structure**

> As part of the solution we will create modules to send Email and Write results to DB
> Gmail will be used for E-Mail, Sqlite as the DB and Selenium for automation
