import requests, json

response = requests.get('https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty')
ids = json.loads(response.text)
for id in ids:
  print(id)