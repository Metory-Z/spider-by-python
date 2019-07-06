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
	print("{:<10}\t{:<20}\t{:<10}--length".format("排名","学校名称","总分"))
	for i in range(num):
		u=ulist[i]
		fpath = 'D:/UnivRankingInfo.txt'
		#print(isinstance("{:<10}\t{:<66}\t{:<10}".format(u[0][0],u[1][0],u[2][0]),str))
		print("{:^10}{:^26}{:<10}--len{}".format(u[0][0],u[1][0],u[2][0],len(u[2][0])))
	with open(fpath, 'a', encoding='utf-8') as f:
		f.write(str(ulist) + '\n')
	f.close()

def main():
	uinfo = []
	url = "http://zuihaodaxue.com/subject-ranking/mathematics.html"
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 50)

main()