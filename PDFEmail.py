import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "emailpythontest12345@gmail.com"
Reciever_Email = "codeitbro@gmail.com"
Password = input('Enter your email account password: ')

newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new program PDF" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Let me know what you think. Image attached!') 

files = ['LargeElementArray.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)                   