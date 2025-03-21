import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import schedule
import time

# === CONFIG ===
URL = "/"  # Replace with your target URL
HEADERS = {"User-Agent": "Mozilla/5.0"}
KEYWORDS = ["python", "remote", "developer"]
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"


def fetch_jobs():
    print("Checking for new job listings...")
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = soup.find_all("div", class_="job-listing")  
    matched = []

    for job in listings:
        title = job.find("h2").get_text()
        link = job.find("a")["href"]
        if any(kw.lower() in title.lower() for kw in KEYWORDS):
            matched.append(f"{title}\n{link}\n")

    if matched:
        send_email("New Job Matches Found", "\n".join(matched))
    else:
        print("No matches found.")


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent!")
    except Exception as e:
        print("Failed to send email:", e)

# === Scheduler ===
schedule.every(1).hour.do(fetch_jobs)

print("Scraper running... (Ctrl+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(10)