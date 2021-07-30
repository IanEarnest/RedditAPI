import requests
import json

def RequestGet(url):
    # HTTPS check/ skip for URL
    httpsStr = "https://"
    if(url.startswith(httpsStr)):
        pass
    else:
        url =  httpsStr + url
        print(f"url modified to: {url}")

    # HTTPS GET request
    request = requests.get(url, headers = {'User-agent': 'IHS'})
    posts = request.json()

    postIndex = 0
    #top 5 post titles based on score
    for post in posts['data']['children']:
        postIndex += 1
        print(f"{postIndex}. {post['data']['title']}")

