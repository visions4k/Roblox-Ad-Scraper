import requests
import time
from bs4 import BeautifulSoup
from config import *
from source.sender import Sender

class AdScraper:
    def __init__(self):
        self.sender = Sender()

    def scrapeAds(self):
        while True:
            adTypes = [1, 2, 3]
            for adType in adTypes:
                url = f"https://www.roblox.com/user-sponsorship/{adType}"
                time.sleep(delay)
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                adData = self.extractAd(soup)
                if adData is not None:
                    imgUrl, adName = adData
                    self.sender.sendWebhook(imgUrl, adType, adName)
                    if saveAds:
                        self.writeFile(imgUrl, adType)

    def writeFile(self, imgUrl, adType):
        filePaths = {1: 'output/banner.txt', 2: 'output/skyscraper.txt', 3: 'output/square.txt'}
        with open(filePaths[adType], 'a') as f:
            f.write(imgUrl + '\n')

    def extractAd(self, soup):
        imgTag = soup.find('img')
        if imgTag and 'src' in imgTag.attrs and 'alt' in imgTag.attrs:
            return imgTag['src'], imgTag['alt']
        return None, None
