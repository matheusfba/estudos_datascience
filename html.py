from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.globo.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')

first_paragraph_id = soup.p.get('id')


all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

print all_paragraphs

