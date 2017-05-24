import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

for p in range(1,5):
	url = "http://www.zhihu.com/collection/27109279?page=" + str(p)
	page = urlopen(url)
	soup = BeautifulSoup(page,"html5lib")

	allp = soup.findAll(class_ = 'zm-item')
	for each in allp:
		answer = each.findNext(class_ = 'zh-summary summary clearfix')
		if len(answer.text) > 100:
			continue    # 答案太长了，有可能出现“显示全部”情况，直接跳过
		problem = each.findNext(class_ = 'zm-item-title')
		print(problem)
		print(answer)