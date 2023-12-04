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
                time.sleep(delay)
                response = requests.get(url)
                if response.status_code == 200:
                    imgUrl = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', response.text).group(1)
                    name = re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', response.text).group(2)
                    redirectUrl = re.search(f'<a class="ad" title="{name}" href="(.*?)"', response.text).group(1)

                    self.sender.sendWebhook(imgUrl, adType, name, redirectUrl)
                    
                    if saveAds:
                        self.writeFile(imgUrl, adType)

    def writeFile(self, imgUrl, adType):
        filePaths = {1: 'output/banner.txt', 2: 'output/skyscraper.txt', 3: 'output/square.txt'}
        with open(filePaths[adType], 'a') as f:
            f.write(imgUrl + '\n')
