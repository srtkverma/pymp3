print("Enter a digit from 1 to 2: ")
print("1. Download by name")
print("2. Download by Youtube Link")
user_choice = input(">")
if user_choice=="1":
    import name_downloader
    name_downloader.main()
elif user_choice=="2":
    import youtube_downloader
    youtube_downloader.main()
else:
    print("Wrong Input")
