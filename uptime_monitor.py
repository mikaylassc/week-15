"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3
Week 15
Chat Gpt Assistance 
"""
import requests
import time
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

URL = "https://thiswebsitedoesnotexist123456.com"
LOG_FILE = "uptime_log.txt"

last_state = "UNKNOWN"


def send_email(url, status_code, error=None):
    print("\nEMAIL ALERT (SIMULATED)")
    print("Subject: Website Down Alert")
    print(f"URL: {url}")
    print(f"Time: {datetime.now()}")
    print(f"Status Code / Error: {status_code or error}\n")


def log(status, code_or_error):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {URL} - {status} - {code_or_error}\n")


def check_site():
    global last_state

    try:
        r = requests.get(URL, timeout=5)
        status_code = r.status_code

        if 200 <= status_code < 400:
            print(f"ONLINE - {datetime.now()} - {URL}")
            log("ONLINE", status_code)
            last_state = "ONLINE"

        else:
            print(f"DOWN - {datetime.now()} - {URL}")
            log("DOWN", status_code)

            if last_state != "DOWN":
                send_email(URL, status_code)
            last_state = "DOWN"

    except Exception as e:
        print(f"DOWN - {datetime.now()} - {URL}")
        log("DOWN", str(e))

        if last_state != "DOWN":
            send_email(URL, None, str(e))

        last_state = "DOWN"


def main():
    while True:
        check_site()
        time.sleep(300)


if __name__ == "__main__":
    main()
