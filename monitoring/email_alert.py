import smtplib
from email.mime.text import MIMEText

def send_email_alert(
    to_email,
    message,
    smtp_server="smtp.gmail.com",
    from_email="clnup50@gmail.com"
):
    """Send a simple email alert."""
    
    msg = MIMEText(message)
    msg["Subject"] = "Server is DOWN ALERT!!!"
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(from_email, "utyo kiiy mfwr urcz")  # required for Gmail unless using an app password
        server.send_message(msg)
