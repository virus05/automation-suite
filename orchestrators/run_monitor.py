from monitoring.ping_server import is_server_up
from monitoring.email_alert import send_email_alert

def main():
    host = "Jenkins server"
    if not is_server_up(host):
        send_email_alert(
            to_email="clnup50@gmail.com",
            message=f"Server {host} appears to be DOWN."
        )

if __name__ == "__main__":
    main()
