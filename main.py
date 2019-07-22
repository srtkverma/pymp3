from bs4 import BeautifulSoup as bs
import requests

def download(url,vid):
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    result = requests.get(url, stream=True, headers=header)
    return result

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
    downloadpage_response = get_response("https://mp3download.center/download/{}".format(vid))
    quality = downloadpage_response.find("button",{"class":"download-mp3-url"})["id"][3:6]
    final_url = "https://mp3download.center/get-file?vid={}&quality={}&title={}".format(vid,quality,title)
    print("Creating file for download....")
    requests.post("https://mp3download.center/trigger-download",data={"vid":vid, "quality":"320"})
    while True:
        response = download(final_url,vid)
        if response.headers['content-type']=='audio/mpeg':
            break
        else:
            continue
    file_name = title
    handle = open(file_name, "wb")
    total_bytes=0
    for chunk in response.iter_content(chunk_size=512):
        total_bytes+=512
        if chunk:
            handle.write(chunk)
        print(f"{round((total_bytes/1000)/1000,1)}MB", end='\r')
    print(f"Downloaded Complete({((total_bytes)/1000)/1000} MB)")
    break
