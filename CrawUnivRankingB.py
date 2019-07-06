import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html ,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([[tds[0].string], [tds[1].string], [tds[3].string]])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^15}\t{2:^10}" # {3} Fill with the third char in format
    print(tplt.format("排名","学校名称","总分", chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0][0],u[1][0],u[2][0],chr(12288)))

def main():
    uinfo = []
    url = "http://zuihaodaxue.com/subject-ranking/mathematics.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)

main()