
# -*- coding: utf-8 -*-

import json
import re
import requests
from bs4 import BeautifulSoup as bs

def get_listings(model):
    url = 'https://www.sgcarmart.com/used_cars/listing.php?MOD=' + model + '&TRN=1&AVL=2&ASL=1'
    base_url = 'https://www.sgcarmart.com/used_cars/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }

    def clean_text(text):
        return re.sub('\s+', ' ', text).strip()

    listings = set()
    items = []
    with requests.session() as s:
        s.headers.update(headers)
        resp = s.get(url)
        soup = bs(resp.content, 'html.parser')

        for div in soup.find_all('div'):
            children = div.findChildren('a')
            if len(children) > 0 :
                link = children[0].get('href')
                match = re.search('(info.php\?ID\=\d+)&', link)
                if match:
                    listings.add(match.group(1))
        
        for listing in listings:
            item_url = base_url + listing
            resp = s.get(item_url)
            soup = bs(resp.content, 'html.parser')
            title = soup.find('a', class_='link_redbanner')
            if title:
                car_info = soup.find('table', id='carInfo')
                if car_info:
                    info = [[clean_text(cell.text) for cell in row('td') if len(clean_text(cell.text)) > 0]
                                for row in car_info('tr')]

                    item = {
                        'url': item_url,
                        'title': title.text,
                        'info': info
                    }

                    items.append(item)
        
        return json.dumps({'model': model, 'listings': items})

if __name__ == '__main__':
    print(get_listings('mx-5'))