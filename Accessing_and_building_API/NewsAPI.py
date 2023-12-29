#api key = 30e77af403684922aae9b1eec84f9d36
import requests

r = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-11-29&sortBy=publishedAt&apiKey=30e77af403684922aae9b1eec84f9d36")

content = r.json()
articles = (content['articles'])

print(type(articles))

for article in articles:
    print('title : ',article['title'])
    print('description : ',article['description'])
