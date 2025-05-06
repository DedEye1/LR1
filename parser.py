from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omsk.drom.ru/auto/new/all/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    block = soup.find_all('div', limit=20, attrs={'data-ftid': 'bulls-list_bull'})

    return block