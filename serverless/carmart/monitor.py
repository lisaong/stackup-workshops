# -*- coding: utf-8 -*-

import json
import re
import requests
import os
from bs4 import BeautifulSoup as bs

def get_listings(model, pricing_only=True):
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

                    if pricing_only:
                        # pricing is the first entry
                        info = info[0]

                    item = {
                        'url': item_url,
                        'title': title.text,
                        'info': info
                    }

                    items.append(item)

        # sort by price
        if pricing_only:
            sorter = lambda item: item['info']
        else:
            sorter = lambda item: item['info'][0]
        items = sorted(items, key=sorter)

        return {'model': model, 'items': items}

def post_webhook(payload):
    msg = json.dumps({'text': json.dumps(payload, sort_keys=True)})

    # https://api.slack.com/apps/ATDMP46KT/incoming-webhooks
    url = os.environ.get('SLACK_WEBHOOK_URL')
    if url is not None:
        headers = {'Content-type': 'application/json'}
        res = requests.post(url, data=msg, headers=headers)
        if res.status_code == 200:
            print(f'Posted to webhook: {msg}')
        else:
            print(f'Webhook Error {res}')

if __name__ == '__main__':
    queries = os.environ.get('CARMART_QUERIES')
    if queries is None:
        queries = 'mx-5;brz;suzuki+swift'

    [post_webhook(get_listings(query)) for query in queries.split(';')]
