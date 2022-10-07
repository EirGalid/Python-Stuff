import smtplib
import ssl
# import csv

port = 465  # ssl port
smtp_server = "smtp.gmail.com"

sender = 'youremail@mail.com'
password = input("Your password: ")  # sender's password
receiver = "receiver'semail@mail.com"

subject = 'email subject'
body = "Email's message"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body)

# ---------- send multiple emails using csv files ---------------------
# with open("file.csv") as file:
#    reader = csv.reader(file)
#    next(reader)
#    for name, email in reader:
#        print("Send email to {name}")
#        server.sendmail(sender, email, body)
# ---------------------------------------------------------------------
