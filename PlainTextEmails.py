import smtplib
Sender_Email = "emailpythontest12345@gmail.com"
Reciever_Email = "codeitbro@gmail.com"
Password = input('Enter your email account password: ')

Subject = "Test Email from CodeItBro"
Body = "Hi, hope you are doing fine! Stay Home! Stay Safe!"
Message = f'Subject: {Subject}\n\n{Body}'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_Email, Password)
    smtp.sendmail(Sender_Email, Reciever_Email, Message)