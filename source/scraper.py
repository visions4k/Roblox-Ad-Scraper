import requests
import time
import re
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
                r = requests.get(url)
                time.sleep(delay)
                adData = self.extractAd(r)
                if adData is not None:
                    imgUrl, adName, adRedirect = adData
                    self.sender.sendWebhook(imgUrl, adType, adName, adRedirect)
                    if saveAds:
                        self.writeFile(imgUrl, adType)

    def writeFile(self, imgUrl, adType):
        filePaths = {1: 'output/banner.txt', 2: 'output/skyscraper.txt', 3: 'output/square.txt'}
        with open(filePaths[adType], 'a') as f:
            f.write(imgUrl + '\n')

    def extractAd(self, r):
        if match := re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', r.text):
            imgUrl, name = match.groups()
            redirectUrl = re.search(f'<a class="ad" title="{name}" href="(.*?)"', r.text).group(1)
            return imgUrl, name, redirectUrl
        else:
            return None, None, None
