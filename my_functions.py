import requests
from bs4 import BeautifulSoup as bs

def download_response(url,vid):
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

def downloader(vid,quality,title):
    url = "https://mp3download.center/get-file?vid={}&quality={}&title={}".format(vid,quality,title)
    print("Creating file for download....")
    requests.post("https://mp3download.center/trigger-download",data={"vid":vid, "quality":quality})
    while True:
        response = download_response(url,vid)
        if response.headers['content-type']=='audio/mpeg':
            break
        else:
            continue
    handle = open(f"{title}.mp3", "wb")
    total_bytes=0
    for chunk in response.iter_content(chunk_size=512):
        total_bytes+=512
        if chunk:
            handle.write(chunk)
        print(f"{round((total_bytes/1000)/1000,1)}MB", end='\r')
    print(f"Downloaded Complete({((total_bytes)/1000)/1000} MB)")
