import requests
from bs4 import BeautifulSoup

cookies = {
    'cf_clearance': 'RoDGFb1aJhUy2edY4jILzDDfWAySyEeTBOxDi2Glb8U-1722940129-1.0.1.1-azPY1Vgc2YRD2tOQ8J39Yh7e_hCUAq0gw7ZtEmBvfg3_ZIulpsr3rbmSPIxbcAgJfJEnPzkAQPJWkWhzauRpxA',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'cf_clearance=RoDGFb1aJhUy2edY4jILzDDfWAySyEeTBOxDi2Glb8U-1722940129-1.0.1.1-azPY1Vgc2YRD2tOQ8J39Yh7e_hCUAq0gw7ZtEmBvfg3_ZIulpsr3rbmSPIxbcAgJfJEnPzkAQPJWkWhzauRpxA',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'ref': 'search',
}

response = requests.get('https://masstamilan.dev/jigarthanda-doublex-songs', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', class_='dlink anim')

result = []
for link in links:
    title = link.get('title')
    href = link.get('href')
    result.append({'title': title, 'href': href})

print(result)
