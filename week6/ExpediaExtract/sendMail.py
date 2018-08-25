import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Create the E-Mail connection variables
smpt_server = 'smtp.gmail.com'
smpt_port = 587

#GMail username and password
username = 'iacc.python'
password = '1@ccpython'

#Create the smtp server connection
smtpserver = smtplib.SMTP(smpt_server, smpt_port)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()


#Define a function accept the from and to addresses, subject of the E-Mail and the file name to send as arguments and send an E-Mail
def sendMail(from_email, to_email, subject, fileName):

    #Create a new MultiPart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    #Open the csv file and add the contents to the message MIME type
    fp = open(fileName)
    msg_body = MIMEText(fp.read())
    fp.close()

    #Create a attachment header and attach the content to the E-Mail
    msg_body.add_header("Content-Disposition", "attachment", filename=fileName)
    msg.attach(msg_body)

    #Next, log in to the server
    smtpserver.login(username, password)

    #Send the mail
    text = msg.as_string()
    smtpserver.sendmail(from_email, to_email, text)
