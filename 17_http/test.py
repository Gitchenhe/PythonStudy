#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib.request import  Request,urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup

def getContent(url):
    req = Request(url)

    #增加头信息
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')
    try:
        response = urlopen(req)
        buffer = response.read()
        html = buffer.decode("gbk")
        response.close()
    except HTTPError as e:
         print("reason %s",e.code)
    except URLError as e:
         print("reason %s" % e.reason)
    return html

def saveContent(content,host):
    soup = BeautifulSoup(content,"html.parser")
    for link in soup.find("tbody").find_all("tr"):
        list = []
        for td in link.find_all("td"):
            list.append(td.get_text())
        print(list)
        # title = link.get_text().strip()
        #
        # url = link.get("href")
        # if url and url.startswith("//"):
        #     url = url.replace("//",host)
        # if url and title :
        #     print("title :%s ,url %s" % (title, url))
        #
        # if url and url.startswith("http://") :
        #
        #     html = getContent(url)
        #     saveContent(html,host)
        #soup2 = BeautifulSoup(html,"html.parser")
        #print("content:%s" % content)

url = "http://q.10jqka.com.cn/"
content = getContent(url)
saveContent(content,url)
