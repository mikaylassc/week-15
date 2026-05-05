# Login Scraper Automation

## Overview for login_scraper.py
This project is a Python script that logs into a practice website and extracts the welcome message shown after a successful login. It demonstrates basic web automation using sessions and HTML parsing.

## Website Used
https://the-internet.herokuapp.com/login

This is a safe practice site used for learning and testing login automation.

## Features
- Uses `requests.Session()` to maintain login state
- Sends a POST request to submit login credentials
- Parses HTML using BeautifulSoup
- Extracts text from the `#flash` element
- Handles login success and failure cases

## Credentials Used
Username: tomsmith  
Password: SuperSecretPassword!

## How to Install Dependencies
Run the following command in your terminal:

pip install requests beautifulsoup4

## How to Run the Script
Run the program using:

python3 login_scraper.py

## What the Program Does
The script logs into the website, keeps the session active, and extracts the welcome message that appears after a successful login. If login fails or the page cannot be accessed, it prints an error message.

## Output Example
Welcome message: You logged into a secure area!

## Notes
This project is for educational purposes only and uses a demo website designed for practicing web automation and testing.
