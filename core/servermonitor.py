from time import sleep

from config import Config
import requests
import urllib3

from core.emailsender import EmailSender

email_sender = EmailSender.Instance()


def background_process():
    servers = Config.Instance().get("servers")

    while True:
        for server in servers:
            server = server["server"]
            name = server["display_name"]
            url = server["healthcheck_url"]
            timeout = server["timeout_duration"]
            status_req = server["healthy_status"]

            print(f"Polling {name} @ {url}")

            try:
                _r = requests.get(url=url, timeout=timeout)

                if _r.status_code != status_req:
                    print(f"Server {name} is down! Status code: {_r.status_code}")
                    email_sender.send_email(
                        f"Server {name} is down", f"{name} @ {url} is down"
                    )
            except urllib3.exceptions.ReadTimeoutError:
                print(f"Timed out {name} after {timeout}s")
                email_sender.send_email(
                    f"Server {name} is down", f"{name} @ {url} is down"
                )
            except Exception as err:
                print(f"Unknown connection error: {err}")
                email_sender.send_email(
                    f"Server {name} is down", f"{name} @ {url} is down"
                )

        sleep(30)
