
import smtplib
try:  
    server = smtplib.SMTP('smtp.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    # ...send emails
except:  
    print('Something went wrong...')
