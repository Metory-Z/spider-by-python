import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "Error"

url = "https://item.jd.com/584773.html"
print(getHTMLText(url))