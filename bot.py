import smtplib, ssl
import json

smtp_server = "smtp.gmail.com"
port = 587

with open('creds.json') as json_file:
    data = json.load(json_file)
    sender_email = data['from']['address']
    password = data['from']['password']
    destination_email = data['to']['address']
    message = data["message"]

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, destination_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()