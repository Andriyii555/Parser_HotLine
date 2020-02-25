import requests
from bs4 import BeautifulSoup
import re
import random
import time
from model import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Float

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
ref_list = []
proxy = {'HTTPS': '163.172.182.164:3128'}
url = 'https://hotline.ua/ax/bosch_'
Session = sessionmaker(bind=db_engine)
session = Session()

def read_ref():
    with open('input.csv', 'r') as file:
        for line in file:
            ref_list.append(line.strip('\n'))
    return ref_list


def get_html(url):
    while True:
        #time.sleep(random.randint(random.randint(6, 10), random.randint(12, 27)))
        time.sleep(5)
        html = requests.get(url, headers=HEADERS, proxies=proxy)
        if html.status_code == 200:
            print(html.status_code)
            return html
        elif html.status_code == 403:
            print(html.status_code)
            print('weit to 100-180 sec')
            time.sleep(random.randint(100,280))
        elif html.status_code == 404:
            print(html.status_code)
            break
        else:
            time.sleep(random.randint(14, 27))
            print(html.status_code)
            print(html.url)
            continue



def parse(html, ref):
    try:
        soup = BeautifulSoup(html.content, 'html.parser')
        offer_count = soup.find('li', {'data-id': 'prices'}).find('i').text
    except:
        offer_count = None

    try:
        new_element = HotLine(ref, offer_count)
        session.add(new_element)
        session.commit()
    except:
        pass


def main():
    count = 1
    ref_list = read_ref()
    for ref in ref_list:
        card_exist = session.query(HotLine.ref).filter(HotLine.ref == ref).count
        if not card_exist:
            html = get_html(url + str(ref))
            parse(html, ref)
            print(f'All ref: {len(ref_list)} parsed: {count}')
            count += 1
        else:
            print(f'All ref: {len(ref_list)} parsed: {count}')
            count += 1

if __name__ == '__main__':
    main()




