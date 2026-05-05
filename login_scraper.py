"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4
Week 15
Chat Gpt Assistance 
"""
import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://the-internet.herokuapp.com/login"
POST_URL = "https://the-internet.herokuapp.com/authenticate"

def login_and_scrape():
    session = requests.Session()

    # Step 1: Load login page
    try:
        session.get(LOGIN_URL)
    except:
        print("Failed to load login page.")
        return

    # Step 2: Login data
    payload = {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    }

    # Step 3: Submit login form
    try:
        response = session.post(POST_URL, data=payload)
    except:
        print("Login failed.")
        return

    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    message = soup.find(id="flash")

    if message:
        clean_text = message.get_text(strip=True)
        print("Welcome message:", clean_text)
    else:
        print("Login failed.")


if __name__ == "__main__":
    login_and_scrape()