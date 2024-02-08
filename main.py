import requests
from send_email import send_email

topic = "tesla"

api_key = "2734e88e531f48e485e9ce9162ff1832"

url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2024-01-08&sortBy=publishedAt" \
    "&apiKey=2734e88e531f48e485e9ce9162ff1832&" \
    "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

body = body.encode("utf-8")
send_email(message=body)
