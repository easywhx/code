import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title><p>The Dormouse's story</p></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,'lxml')
print(soup.head.parent)  #获取head标签
print(soup.find_all('p',class_='title')) #获取p节点下的b节点
print(soup.find_all("a",id='link1')) #获取a标签下的文本，只获取第一个
print(soup.find_all(text=re.compile('Tillie')))  #文本过滤
print(soup.find_all('a',limit=2))  #限制输出数量