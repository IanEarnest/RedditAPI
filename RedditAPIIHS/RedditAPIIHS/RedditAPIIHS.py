import requests

x = requests.get('https://reddit.com/r/redditdev/')

print(x.text)