from discord_webhook import DiscordWebhook, DiscordEmbed
from config import *


class Sender:
    def __init__(self):
        self.webhook = discordWebhook

    def sendWebhook(self, imgUrl, adType, adName):
        if adType == 1:
            adTypeNew = "Banner"
        elif adType == 2:
            adTypeNew = "Skyscraper"
        elif adType == 3:
            adTypeNew = "Square"
        webhook = DiscordWebhook(url=self.webhook)
        embed = DiscordEmbed()
        embed.set_title("Ad Scraper")
        embed.set_description(f"> **Type:** `{adTypeNew}`\n> **Name:** `{adName}`")
        embed.set_image(url=imgUrl)
        embed.set_footer(text="Roblox Ad Scraper")
        embed.set_color(hex(embedColor)[2:])
        webhook.add_embed(embed)
        response = webhook.execute()
        if response.status_code == 200:
            print("\033[92mSuccessfully sent webhook.\033[0m")


