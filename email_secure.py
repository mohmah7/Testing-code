import ssl, smtplib
smtp = smtplib.SMTP("mail.yahoo.com", port=587)
context = ssl.create_default_context()
smtp.starttls(context=context)
