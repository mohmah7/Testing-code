import smtplib

gmail_user = 'fiversameh@gmail.com'  
gmail_password = input('PLEASE ENETET YOUR PASSWORD:')

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    print(' welcome email ')
except:  
    print('Something went wrong...')
