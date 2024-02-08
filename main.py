import requests
api_key = "2734e88e531f48e485e9ce9162ff1832"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-08&sortBy=publishedAt&apiKey=" \
       "2734e88e531f48e485e9ce9162ff1832"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
