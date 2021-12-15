import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Normal Website ---------------------------------------------
print('1: Normal Website')
url = 'http://www.webscrapingfordatascience.com/postform2/'
form_data = {'name': 'David',
             'gender': 'M',
             'pizza': 'like',
             'salad': 'like',
             'haircolor': 'black',
             'comments': 'this is a test'}
result = requests.post(url, data=form_data)
print(result.text)
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------- Scrap from Website with Protection -----------------------------------

print('2: Scrap from Website with Protection')
url = 'http://www.webscrapingfordatascience.com/postform3/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
protection = soup.find('input', {'name': 'protection'}).get('value')

form_data = {'name': 'David',
             'gender': 'M',
             'pizza': 'like',
             'salad': 'like',
             'haircolor': 'black',
             'comments': 'this is a test',
             'protection': protection}
result = requests.post(url, data=form_data)
print(result.text)

# ------------------------------------------------------------------------------------------------------------
# --------------------------- solving problems of websites which ignore Scrapping ----------------------------
print('3: solving problems of websites which ignore Scrapping')
url = 'http://www.webscrapingfordatascience.com/usercheck'
result = requests.get(url)
print(result.text)
print(result.request.headers)
# ---------------------------------------
print('4: solving problems of websites which ignore Scrapping')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
url = 'http://www.webscrapingfordatascience.com/usercheck'
result = requests.get(url, headers=header)
print(result.text)
print(result.request.headers)

print('5: solving problems of websites which ignore Scrapping')
url = 'http://www.webscrapingfordatascience.com/referercheck/secret.php'
header = {'Referer': 'http://www.webscrapingfordatascience.com/referercheck/'}
result = requests.get(url, headers=header)
print(result.text)
print(result.request.headers)

# -------------------------------------------------- Cookie --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
print('6: Cookie')
url = 'http://www.webscrapingfordatascience.com/cookielogin/secret.php'
cookie = {'PHPSESSID': 'csvon8r7k0tufd4qsmpvqer32k'}
result = requests.get(url, cookies=cookie)
print(result.text)

# ---------------------
print('7: Cookie')
url = 'http://www.webscrapingfordatascience.com/cookielogin/'
data = {'username': 'david', 'password': 'david'}
r = requests.post(url, data=data)

url = 'http://www.webscrapingfordatascience.com/cookielogin/secret.php'
cookie = {'PHPSESSID': r.cookies['PHPSESSID']}
result = requests.get(url, cookies=cookie)
print(result.text)

# ---------------------
print('8: Cookie')
url = 'http://www.webscrapingfordatascience.com/redirlogin/'
r = requests.post(url, data={'username': 'david', 'password': 'david'}, allow_redirects=False)

cookie = {'PHPSESSID': r.cookies['PHPSESSID']}
r = requests.get(url + 'secret.php', cookies=cookie)
print(r.text)

# ------------------------------
print('9: Cookie')
url = 'http://www.webscrapingfordatascience.com/trickylogin/'
r1 = requests.get(url)
cookie = {'PHPSESSID': r1.cookies['PHPSESSID']}
r2 = requests.post(url, data={'username': 'david', 'password': 'david'}, params={'p': 'login'}, cookies=cookie,
                   allow_redirects=False)
cookie = {'PHPSESSID': r2.cookies['PHPSESSID']}
r1 = requests.get(url + 'index.php')
r = requests.get(url, params={'p': 'protected'}, cookies=cookie)
print(r.text)
# -------------------------------------------------- Session -------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
print('10: Session')
url = 'http://www.webscrapingfordatascience.com/trickylogin/'
mysession = requests.Session()
r1 = mysession.post(url)
r2 = mysession.post(url, params={'p':'login'}, data={'username':'david', 'password':'david'})
r3 = mysession.get(url, params={'p':'protected'})
print(r3.text)
# ------------------------------------------------- Json Ajax ------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
print('11: Json Ajax')
url = 'http://www.webscrapingfordatascience.com/jsonajax/results.php'
result = requests.post(url , data ={'api_code': 'C123456'})
print(result.json())