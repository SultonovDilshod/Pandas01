import requests as rq
import json

url = 'https://api.languagetoolplus.com/v2/check'
data = {
    'text': 'Cak me tell me your full name please?',
    'language': 'en',
}

response = rq.post(url=url, data=data)
result = json.loads(response.text)
print(result)

