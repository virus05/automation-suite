import smtplib
from email.mime.text import MIMEText

def send_email_alert(to_email, message,
                     smtp_server="smtp.example.com",
                     from_email="monitor@example.com"):
    """Send a simple email alert."""
    
    msg = MIMEText(message)
    msg["Subject"] = "Server is DOWN ALLEERRTT!!!"
    msg["From"] = from_email
    msg["To"] = to_email
    
    with smtplib.SMTP(smtp_server) as server:
        server.send_message(msg)