import requests
from send_email import send_email

api_key = "2734e88e531f48e485e9ce9162ff1832"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-08&sortBy=publishedAt&apiKey=" \
       "2734e88e531f48e485e9ce9162ff1832"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    title = article.get("title", "")
    description = article.get("description", "")
    if title and description:  # Check if both title and description exist
        body += title + "\n" + description + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
