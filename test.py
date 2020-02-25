import requests
from bs4 import BeautifulSoup


API_URL = 'https://www.freeproxy-list.ru/api/proxy?anonymity=false&token=demo'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
url = 'https://hotline.ua/'

def get_proxy(api_url):
    proxy_list = requests.get(api_url)
    return proxy_list.text.split('\n')


proxy_list = get_proxy(API_URL)
print(len(proxy_list))

for ip in proxy_list:
    proxy = {'HTTPS': ip}
    html = requests.get(url, headers=HEADERS, proxies=proxy)
    if html.status_code == 200:
        print(html.status_code)
    elif html.status_code == 403:
        print(html.status_code)
        print('weit to 100-180 sec')
        time.sleep(random.randint(100, 280))
    elif html.status_code == 404:
        print(html.status_code)
        break
    else:
        time.sleep(random.randint(14, 27))
        print(html.status_code)
        print(html.url)
        continue




