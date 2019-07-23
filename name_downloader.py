import my_functions as my
def main():
    while True:
        song_name = input("Enter a song name: ")
        print("Searching for song....")
        search_response = my.get_response("https://mp3download.center/mp3/{}".format(song_name))
        song_url = search_response.findAll("li", {"class":"media"})[0].a['href']
        title = search_response.findAll("li", {"class":"media"})[0].h4.text
        print(title)
        user_input=input("Enter yes if correct song, enter no if wrong song: ")
        if user_input=="no":
            continue
        vid=song_url[my.find_all(song_url)[1]+1:len(song_url)]
        quality = my.get_response("https://mp3download.center/download/{}".format(vid)).find("button",{"class":"download-mp3-url"})["id"][3:6]
        my.downloader(vid,quality,title)
        break
