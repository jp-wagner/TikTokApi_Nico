from tkinter import W
from webdriver import Driver
import json

webdriver = Driver()

def download_video(video, path="test_download.mp4"):
    open(path, "wb").write(video)

# test url scraping and download
tiktok = webdriver.scrape_url("https://www.tiktok.com/@AisieArt/video/7097051858728013099", download_video=True)
print(tiktok["info"])
download_video(tiktok["video"])

# test hashtag scraping
tiktoks = webdriver.scrape_hashtag("ukraine", count=3, download_video=True)
for indx, tiktok in enumerate(tiktoks):
    download_video(tiktok["video"], path=str(indx))
    open(str(indx)+"info.txt", "w").write(str(tiktok["info"]))
    if indx == 3:
        webdriver.shutdown()
        exit()

# test sound scraping
tiktoks = webdriver.scrape_sound("6728562975734515713")
for tiktok in tiktoks:
    print(tiktok["info"])

# test user scraping
tiktoks = webdriver.scrape_user("the_rock")
for tiktok in tiktoks:
    print(tiktok["info"])

# test search term scraping
tiktoks = webdriver.scrape_search_term("funny animals")
for tiktok in tiktoks:
    print(tiktok["info"])

webdriver.shutdown()
