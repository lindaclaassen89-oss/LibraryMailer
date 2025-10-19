import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date, datetime
import logging

START_DATE = datetime.strptime("2025-10-01", "%Y-%m-%d").date()
TODAY = date.today()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if  ((TODAY - START_DATE).days % (2*7) != 0 
    or (TODAY - START_DATE).days % (6*7) == 0
    ): # every 2nd week except every 6th week
    logger.info(f"\n\nCriteria not met: {datetime.now()}\n\n")

else:
    logger.info(f"\n\nCriteria met: {datetime.now()}\n\n")

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "linda.claassen.89@gmail.com"
    receiver_email = "linda.claassen.89@gmail.com " #brooklyn@tshwane.gov.za"
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
    except Exception as e:
        with open("date_log.txt", "a") as file:
            logger.error(f"{TODAY} failed: {e}\n")


