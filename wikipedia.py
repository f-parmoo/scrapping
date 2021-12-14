import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

tags = ['wikitable plainrowheaders wikiepisodetable']
episodes = []
for table in soup.findAll('table', class_='wikiepisodetable'):
    headers = []
    first_row = table.find('tr')
    for th in first_row.findAll(['th']):
        headers.append(th.text)
    for tr in table.findAll('tr')[1:]:
        sublist = []
        for th in tr.findAll(['th', 'td']):
            sublist.append(th.text)
        episodes.append({headers[item]: sublist[item] for item in range(len(sublist))})

print(episodes)
