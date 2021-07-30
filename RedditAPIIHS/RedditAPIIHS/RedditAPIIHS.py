import requests

def RequestGet(url):
    # HTTPS check/ skip for URL
    httpsStr = "https://"
    if(url.startswith(httpsStr)):
        pass
    else:
        url =  httpsStr + url
        print(f"url modified to: {url}")

    # HTTPS GET request
    request = requests.get(url)
    print(request.text)
