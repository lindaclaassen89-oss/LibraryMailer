import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date, datetime

START_DATE = datetime.strptime("2025-08-12", "%Y-%m-%d").date()
TODAY = date.today()

with open("date_log.txt", "r") as file:
    dates = file.readlines()
    dates = [line.strip() for line in dates]

if (TODAY.strftime("%Y-%m-%d") not in dates # not yet run today
    and (TODAY - START_DATE).days % 14 == 0 and (TODAY - START_DATE).days % (3*14) != 0): # every 2nd week except every 6th week

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "linda.claassen.89@gmail.com"
    receiver_email = sender_email
    password = "isap rioe okdl xzwa"

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Please renew"

    # Email body
    body = "Good morning<br><br>Can you please renew the books on these two cards for two more weeks?<br><br>400591012<br>400591014<br><br>Thanks, <br>Linda"
    message.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        with open("date_log.txt", "a") as file:
            file.write(f"{TODAY}\n")
    except Exception as e:
        with open("date_log.txt", "a") as file:
            file.write(f"{TODAY} failed\n")

