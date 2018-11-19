import smtplib

gmail_user = 'fiversameh@gmail.com'  
gmail_password = input('PLEASE ENETET YOUR PASSWORD:')

#try:  
server = smtplib.LMTP('smtp.gmail.com', 465)
server.ehlo()
server.set_debuglevel(1)
server.ehlo()
server.login(gmail_user, gmail_password)
print(' welcome email , the  password is :%s'% gmail_password)
#except:  
print('Something went wrong...The password is%s' %  gmail_password )

