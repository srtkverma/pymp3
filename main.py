from bs4 import BeautifulSoup as bs
import requests
import os

def download(url,song_name):
    os.system("wget -q --show-progress -O '{}' '{}'".format(song_name,url))

def find_all(string,to_find="/"):
    pos=[]
    for i in range(0,len(string)):
        if string[i]==to_find:
            pos.append(i)
    return pos

def get_response(url):
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    response=requests.get(url, headers=header)
    return bs(response.text, "html.parser")

while True:
    song_name = input("Enter a song name: ")
    search_response = get_response("https://mp3download.center/mp3/{}".format(song_name))
    song_url = search_response.findAll("li", {"class":"media"})[0].a['href']
    title = search_response.findAll("li", {"class":"media"})[0].h4.text
    print(title)
    user_input=input("Enter yes if correct song, enter no if wrong song: ")
    if user_input=="no":
        continue
    slashes = find_all(song_url)
    vid=song_url[slashes[1]+1:len(song_url)]
    downloadpage_url = "https://mp3download.center/download/{}".format(vid)
    downloadpage_response = get_response(downloadpage_url)
    quality = downloadpage_response.find("button",{"class":"download-mp3-url"})["id"][3:6]
    final_url = "https://mp3download.center/get-file?vid={}&quality={}&title={}".format(vid,quality,title)
    download(final_url,f"{title}.mp3")
    break
