from TikTokApi import TikTokApi
import logging

class Driver:


    # comments
    # public likes

    def __init__(self):
        self.api = TikTokApi(custom_verify_fp="verify_l69g7zud_MZwI7sKz_FlUJ_4GlT_8IvL_TwcuR59aCvUs")


    def scrape_hashtag(self, hashtag, count=30, download_video=False):
        """
        Scrapes a hashtag

        hashtag: the hastag to scrape
        count: how many videos to scrape (max ~1000)
        download_video: whether or not to download the video (will increase runtime significantly)
        """
        logging.info("Scraping hashtag %s", hashtag)

        tag = self.api.hashtag(name=hashtag).videos(count)

        tiktoks = []
        for tiktok in tag:
            try:
                tiktoks.append(self.get_data(tiktok, download_video))
            except Exception as e:
                print(e)
                continue
        
        return tiktoks


    def scrape_user(self, username, count=30, download_video=False):
        """
        Scrapes a user. Needs logged in custom_verify_fp.

        username: the user to scrape
        count: how many videos to scrape
        download_video: whether or not to download the video (will increase runtime significantly)
        """
        logging.info("Scraping user %s", username)

        user = self.api.user(username=username).videos(count=count)

        tiktoks = []
        for tiktok in user:
            try:
                tiktoks.append(self.get_data(tiktok, download_video))
            except Exception as e:
                print(e)
                continue

        return tiktoks

    def scrape_url(self, url, download_video=False):
        """
        Scrapes a url
        
        url: url to scrape
        """

        logging.info("Scraping url %s", url)
        try:
            tiktok = self.api.video(url = url)
        except Exception as e:
            print(e)
            return

        return self.get_data(tiktok, download_video)
            
    def scrape_sound(self, sound_id, count=30, download_video=False):
        """
        Scrapes a sound

        sound_id: the id of the sound to scrape
        count: how many videos to scrape (max ~1500)
        download_video: whether or not to download the video (will increase runtime significantly)
        """
        logging.info("Scraping sound %s", sound_id)

        sound = self.api.sound(id=sound_id).videos(count=count)

        tiktoks = []
        for tiktok in sound:
            try:
                tiktoks.append(self.get_data(tiktok, download_video))
            except Exception as e:
                print(e)
                continue

        return tiktoks

    def scrape_search_term(self, search_term, count=30, download_video=False):
        """
        Scrapes a sound

        sound_id: the id of the sound to scrape
        count: how many videos to scrape (max ~1000)
        download_video: whether or not to download the video (will increase runtime significantly)

        currently broken.
        """
        logging.info("Scraping search term %s", search_term)

        search = self.api.search.videos(search_term, count=count)

        tiktoks = []
        for tiktok in search:
            try:
                tiktoks.append(self.get_data(tiktok, download_video))
            except Exception as e:
                print(e)
                continue

        return tiktoks


    def shutdown(self):
        """
        shuts down the api
        """
        
        self.api.shutdown()

    @staticmethod
    def get_data(tiktok, download_video):
        """
        scrapes data from a single TikTok

        tiktok: the tiktok object
        download_video: whether or not to download the video (will increase runtime significantly)
        """

        data = {"info": tiktok.info_full(),
                "video": ""}

        if download_video:
            data["video"] = tiktok.bytes()

        return data
