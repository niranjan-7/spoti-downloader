from bs4 import BeautifulSoup
import requests

# Define the URL and the request parameters
url = 'https://masstamilan.dev/search'
params = {'keyword': 'Maamadura'}
cookies = {
    'prefetchAd_6115795': 'true',
    'cf_clearance': 'RoDGFb1aJhUy2edY4jILzDDfWAySyEeTBOxDi2Glb8U-1722940129-1.0.1.1-azPY1Vgc2YRD2tOQ8J39Yh7e_hCUAq0gw7ZtEmBvfg3_ZIulpsr3rbmSPIxbcAgJfJEnPzkAQPJWkWhzauRpxA',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://masstamilan.dev/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

# Make the HTTP request
response = requests.get(url, params=params, cookies=cookies, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <div> elements with class "a-i"
divs = soup.find_all('div', class_='a-i')


albums = []
# Check if divs are found and extract href attributes
if divs:
    for div in divs:
        a_tag = div.find('a')
        if a_tag and 'href' in a_tag.attrs:
            print(a_tag['href'])
            albums.append("https://masstamilan.dev"+a_tag['href'])
else:
    print("No divs with class 'a-i' found.")


print(albums)