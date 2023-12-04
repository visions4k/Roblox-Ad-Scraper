import aiohttp
import asyncio
import re
from config import *
from source.sender import Sender

class AdScraper:
    def __init__(self):
        self.sender = Sender()

    async def scrapeAds(self):
        async with aiohttp.ClientSession() as session:
            while True:
                adTypes = [1, 2, 3]
                for adType in adTypes:
                    url = f"https://www.roblox.com/user-sponsorship/{adType}"
                    r = await session.get(url)
                    await asyncio.sleep(delay)
                    adData = await self.extractAd(r)
                    if adData is not None:
                        imgUrl, adName, adRedirect = adData
                        self.sender.sendWebhook(imgUrl, adType, adName, adRedirect)
                        if saveAds:
                            self.writeFile(imgUrl, adType)

    def writeFile(self, imgUrl, adType):
        filePaths = {1: 'output/banner.txt', 2: 'output/skyscraper.txt', 3: 'output/square.txt'}
        with open(filePaths[adType], 'a') as f:
            f.write(imgUrl + '\n')

    async def extractAd(self, r):
        text = await r.text()
        if match := re.search('<img src=\"(.*?)\" alt=\"(.*?)\"', text):
            imgUrl, name = match.groups()
            redirect_match = re.search(f'<a class="ad" title="{name}" href="(.*?)"', text)
            redirectUrl = redirect_match.group(1) if redirect_match else None
            return imgUrl, name, redirectUrl
        else:
            return None, None, None
