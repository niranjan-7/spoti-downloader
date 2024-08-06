import os
import requests
import re


# urls = [
#     "https://masstamilan.dev/downloader/gfl4NID3KTKGjbrbbPfBZA/1722942147/d128_cdn/24963/MjQwNToyMDE6ZTAxODo2MDJiOjI1YzA6MTYyMDo1ZTY4OmEzYQ==",
#     "https://masstamilan.dev/downloader/hNM9bDxZTacjhO7YZ9_tTQ/1722944694/d320_cdn/28780/MjQwNToyMDE6ZTAxODo2MDJiOjI1YzA6MTYyMDo1ZTY4OmEzYQ==",
#     "https://masstamilan.dev/downloader/hNM9bDxZTacjhO7YZ9_tTQ/1722944694/d320_cdn/29625/MjQwNToyMDE6ZTAxODo2MDJiOjI1YzA6MTYyMDo1ZTY4OmEzYQ==",
#     "https://masstamilan.dev/downloader/hNM9bDxZTacjhO7YZ9_tTQ/1722944694/d320_cdn/27627/MjQwNToyMDE6ZTAxODo2MDJiOjI1YzA6MTYyMDo1ZTY4OmEzYQ=="
# ]


# save_dir = "D:\\github\\spoti-downloader\\downloads"
# os.makedirs(save_dir, exist_ok=True)


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }


# for url in urls:
    
#     match = re.search(r'/(\d+)/[^/]+$', url)
#     if match:
#         unique_id = match.group(1)
#         save_path = os.path.join(save_dir, f"{unique_id}.mp3")
        
        
#         response = requests.get(url, headers=headers, stream=True)
#         if response.status_code == 200:
#             with open(save_path, "wb") as file:
#                 for chunk in response.iter_content(chunk_size=8192):
#                     file.write(chunk)
#             print(f"File downloaded successfully and saved as '{save_path}'.")
#         else:
#             print(f"Failed to download file from {url}. Status code:", response.status_code)
#     else:
#         print(f"Failed to extract unique ID from URL: {url}")




def spotiDownloader(save_dir, songs):
    os.makedirs(save_dir, exist_ok=True)

    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    
    for song in songs:
        unique_id = song["title"] 
        save_path = os.path.join(save_dir, f"{unique_id}.mp3")
        
        response = requests.get(song["href"], headers=headers, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File downloaded successfully and saved as '{save_path}'.")
        else:
            print(f"Failed to download file "+song["title"] +". Status code:", response.status_code)
    

def searchResult(songname):
    from bs4 import BeautifulSoup
    import requests

    url = 'https://masstamilan.dev/search'
    params = {'keyword': songname}
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

    
    response = requests.get(url, params=params, cookies=cookies, headers=headers)

    
    soup = BeautifulSoup(response.text, 'html.parser')

    
    divs = soup.find_all('div', class_='a-i')
    # print(divs)

    albums = []
    
    if divs:
        for div in divs:
            a_tag = div.find('a')
            if a_tag and 'href' in a_tag.attrs:
                # print(a_tag['href'])
                albums.append("https://masstamilan.dev"+a_tag['href'])
                return "https://masstamilan.dev"+a_tag['href']                
    else:
        albums.append("")
        print("No divs with class 'a-i' found.")
    # return albums[0] 


def getSongList(client_id,client_secret,playlist_id):
    import requests
    from requests.auth import HTTPBasicAuth

    # CLIENT_ID = '8b621303212d4f51a2f82741ab80bd6a'
    # CLIENT_SECRET = 'e70739656af543cdbe54de2671ebff02'
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    # playlist_id = '37i9dQZF1DX4Im4BTs2WMg'
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(playlist_url, headers=headers)
    playlist_data = response.json()
    song_list=[]
    tracks = playlist_data['tracks']['items']
    for track in tracks:
        track_name = track['track']['name']
        song_list.append(track_name)  
        # print(track_name)

    return song_list

def getSongLinks(urlLink,songName):
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

    response = requests.get(urlLink, params=params, cookies=cookies, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', class_='dlink anim')

    result = []
    for link in links:
        title = link.get('title')
        if songName.lower() in title.lower():
            href = link.get('href')
            result.append({'title': title, 'href':'https://masstamilan.dev'+ href})
    return result

def remove_enclosed_text(strings):
    patterns = [r'".*?"', r'\(.*?\)', r'\[.*?\]']
    def clean_string(s):
        for pattern in patterns:
            s = re.sub(pattern, '', s)
        return s
    cleaned_strings = [clean_string(s) for s in strings]
    return cleaned_strings

def get_href_for_titles(titles, objects):
    result = []
    for title in titles:
        matched_object = next((obj for obj in objects if title in obj["desc"]), None)
        if matched_object:
            result.append({"title": title, "href": matched_object["href"]})
        else:
            result.append({"title": title, "href": None})
    return result

def runMain():
    songListFromSpotify = getSongList('8b621303212d4f51a2f82741ab80bd6a','e70739656af543cdbe54de2671ebff02','37i9dQZF1DX4Im4BTs2WMg')
    songsList = remove_enclosed_text(songListFromSpotify)
    
    urls = []
    for song in songsList:
        albumLink = searchResult(song)
    
        if albumLink != "":
            urls.append({"songName":song,"albumLink":albumLink})
        

    songsCollection = []
    for url in urls:
        songs = getSongLinks(url["albumLink"],url["songName"])
        songsCollection.extend(songs)

    print(songsCollection)
    spotiDownloader(songsCollection)

    # haveToDownload = get_href_for_titles(songsList,songsCollection)
    # print(haveToDownload)



runMain()