# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt'#Go to the default page.
try:
    r = requests.get(url)
except:
    print 'Some errors happened, check your network or something else.'
else:
    r.encoding = 'utf-8'
    t = r.text
    soup = BeautifulSoup(t, 'lxml')
    for tr in soup.find_all('tbody'):
        latest = tr.find('td').string#Get the latest number from the default page.
    url_a = 'http://www.lottery.gov.cn/historykj/history.jspx?page=false&_ltype=dlt&termNum=0&startTerm=07001&endTerm=' + latest#Inquiry all the past numbers.
try:
    r_a = requests.get(url_a)
except:
    print 'Some errors happened, check your network or something else.'
else:
    r_a.encoding = 'utf-8'
    t_a = r_a.text
    soup_a = BeautifulSoup(t_a, 'lxml')
    for tr_a in soup_a.find_all('tr'):
        i = 1
        for td in tr_a.find_all('td'):
            if i % 20 == 0:#Every 20 attribute a new line.
                str_a = str(td.string) + '\n'
                print str_a
                i += 1
            else:
                str_a = str(td.string) + '\t'
                print str_a
                i += 1
            with open('Chinese_dlt.txt', 'a') as f:#Write into file.
                f.write(str_a)
