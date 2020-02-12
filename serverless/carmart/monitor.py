# -*- coding: utf-8 -*-

import json
import re
import requests
import os
from bs4 import BeautifulSoup as bs
import boto3
from botocore.exceptions import ClientError

def get_listings(model, pricing_only=True):
    url = 'https://www.sgcarmart.com/used_cars/listing.php?MOD=' + model + '&TRN=1&AVL=2&ASL=1'
    base_url = 'https://www.sgcarmart.com/used_cars/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }

    def clean_text(text):
        return re.sub('\s+', ' ', text).strip()

    listings = dict()
    items = []
    with requests.session() as s:
        s.headers.update(headers)
        resp = s.get(url)
        soup = bs(resp.content, 'html.parser')

        for div in soup.find_all('div', id='Frame'):
            children = div.findChildren('a')
            if len(children) > 0 :
                link = children[0].get('href')
                match = re.search('(info.php\?ID\=\d+)&', link)
                if match:
                    # find the thumbnail
                    listings[match.group(1)] = div.find_next_sibling('img', 
                                                                     attrs={'title': 'more details'})['src']

        for listing, thumbnail_url in listings.items():
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
                        'info': info,
                        'img_url': thumbnail_url
                    }

                    items.append(item)

        # sort by price
        if pricing_only:
            sorter = lambda item: item['info']
        else:
            sorter = lambda item: item['info'][0]
        items = sorted(items, key=sorter)

        return {'model': model, 'items': items}

def post_webhook(listings, history):
    # https://api.slack.com/messaging/webhooks#advanced_message_formatting
    """{
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://www.sgcarmart.com/used_cars/info.php?ID=876320|MINI Cooper S Cabriolet 1.6M (COE till 11/2025)>\n \n Price: $63,888"
            },
            "accessory": {
                "type": "image",
                "image_url": "https://i.i-sgcm.com/cars_used/201911/870928_small.jpg",
                "alt_text": "car image"
            }
        }
    ]}
    """

    blocks = []

    for item in listings['items']:

        # mark new items so that they stand out
        # an item is new if it has not been seen in the last time this code was run
        flag = ''
        if history and item["url"] not in history:
            # list of emoji: https://unicodey.com/emoji-data/table.htm
            flag = ':new'

        markdown = f'<{item["url"]}|{item["title"]}> {flag} \n Price: {item["info"][1]}'

        blocks.append(
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': markdown
                },
                'accessory': {
                    'type': 'image',
                    'image_url': item["img_url"],
                    'alt_text': 'thumbnail'
                }
            }
        )

    msg = json.dumps({'text': listings['model'], 'blocks': blocks})

    # https://api.slack.com/apps/ATDMP46KT/incoming-webhooks
    url = os.environ.get('SLACK_WEBHOOK_URL')
    if url is not None:
        headers = {'Content-type': 'application/json'}
        res = requests.post(url, data=msg, headers=headers)
        if res.status_code == 200:
            print(f'Posted to webhook: {msg}')
        else:
            print(f'Webhook Error {res}')

def get_history(client, bucket, key):
    try:
        obj = client.get_object(Bucket=bucket, Key=key)
    except ClientError as e:
        # no history
        return None
    return json.loads(obj['Body'].read().decode('utf-8'))

def save_history(client, bucket, key, history):
    obj = json.dumps(history)
    client.put_object(Body=obj, Bucket=bucket, Key=key)

if __name__ == '__main__':
    queries = os.environ.get('CARMART_QUERIES')
    if queries is None:
        queries = 'mx-5;brz;suzuki+swift'

    bucket_name = os.environ.get('S3_BUCKET_NAME')

    for query in queries.split(';'):
        listing = get_listings(query)

        if len(listing) > 0:
            history = None
            if bucket_name:
                s3 = boto3.client('s3')
                history = get_history(s3, bucket_name, query)
                save_history(s3, bucket_name, listing, query)

            post_webhook(listing, history)