import requests
# This API key from https://newsapi.org/
API_key = 'a743b2e2fd41482b93949c707d148e03'
URL = "https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-27&to=2032-2-28&sortBy=popularity&language=en&apiKey=a743b2e2fd41482b93949c707d148e03"
content = requests.get(URL).json()
print(content['articles'][0]['title'])





