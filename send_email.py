# import necessary py modules
import smtplib, ssl

# function send email
def send_email(message):
    port = 465  # For SSL
    #port = 587 # For TSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "your_password"
    
    # login & send the mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('Email has been successfully sent!')
        except:
            print("Error! Could not login or send the mail... Try again!")