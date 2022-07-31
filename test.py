from webdriver import Driver
import json

webdriver = Driver()

def download_video(video, path="test_download.mp4"):
    print("bruh")
    open(path, "wb").write(video)
    print("breh")

# test url scraping
tiktok = webdriver.scrape_url("https://www.tiktok.com/@AisieArt/video/7097051858728013099", download_video=True)
print(tiktok[0])
download_video(tiktok[1])

# test hashtag scraping
tiktoks = webdriver.scrape_hashtag("funny")
for tiktok in tiktoks:
    print(tiktok[0])

# test sound scraping
tiktoks = webdriver.scrape_sound("6728562975734515713", count=1000)
for tiktok in tiktoks:
    print(tiktok[0])

# test user scraping
tiktoks = webdriver.scrape_user("the_rock")
for tiktok in tiktoks:
    print(tiktok[0])

# test search term scraping
tiktoks = webdriver.scrape_search_term("funny animals")
for tiktok in tiktoks:
    print(tiktok[0])

webdriver.shutdown()
