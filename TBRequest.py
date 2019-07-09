import re
import requests
#need to login

def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(';'))
			title = eval(tlt[i].split(';'))
			ilt.append(price, title)
	except:
		print("")

def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号", "价格", "名称"))
	count = 0
	for g in ilt:
		count += 1
		print(tplt.format(count, g[0], g[1]))

def main():
	goods = '键盘'
	depth =2
	start_url = 'http://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range (depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList)

main()