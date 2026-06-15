import smtplib
from email.message import EmailMessage

email = EmailMessage()

email["Subject"] = "Server Alert"
email["From"] = "yourmail@gmail.com"
email["To"] = "receiver@gmail.com"

email.set_content("Server CPU usage is high!")

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(
    "yourmail@gmail.com",
    "your-app-password"
)

server.send_message(email)

server.quit()

print("Alert email sent!")