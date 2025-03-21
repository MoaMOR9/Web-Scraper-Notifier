# Automated Web Scraper & Notifier

This script scrapes a webpage for new job listings (or products/news) and sends email alerts when matches are found.

##  Setup
1. Install dependencies:
```bash
pip install beautifulsoup4 requests schedule
```

2. Update the following in the script:
- `URL`: Target webpage
- `KEYWORDS`: Search terms
- `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECEIVER`

3. Enable **"Less secure app access"** on your Gmail account or use App Passwords.

## 🚀 Run
```bash
python scraper.py
```

It checks hourly. You can change the schedule with the `schedule.every()` function.

##  Docker (Optional)
```Dockerfile
FROM python:3.10
WORKDIR /app
COPY scraper.py .
RUN pip install beautifulsoup4 requests schedule
CMD ["python", "scraper.py"]
```

Build and run:
```bash
docker build -t scraper .
docker run -d scraper
```

## 🕒 CRON Job (Optional)
Instead of `schedule`, run via cron:
```cron
0 * * * * /usr/bin/python3 /path/to/scraper.py
```

## ✅ Features
- Scrapes based on keyword match
- Sends email notifications
- Easy to extend for Telegram, product prices, or news feeds

"""
