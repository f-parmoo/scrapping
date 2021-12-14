import requests
from bs4 import BeautifulSoup
import re


parameter = {'a': '2', 'b': '4', 'op': '*'}
url = 'http://www.webscrapingfordatascience.com/calchttp'
result = requests.get(url, params=parameter)
print('status_code:', result.status_code)


url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
result = requests.get(url)
content = BeautifulSoup(result.text, 'html.parser')
for item in content.findAll('h2' , limit=3):
    print(item)




print(content.find('li', {"id":"footer-copyrightico"}), end='\n\n')
print(content.find('div', class_ ="mw-indicators"))


res  = content.find('h2')
print(res.name)
print(res.content)
print(res.get_text())
print(res.attrs)
print(res.get('id')) # id is one of attributes

print( content.findAll(re.compile('^h')))

print( content.select('a'))
print('---------------p_logo------------')
print( content.select('#p-logo'))
print( content.select('a.mw-wiki-logo'))
print(content.select('a[href^="/wiki/"]'))

print(content.select('ul > li'))