#!/usr/bin/env python
from source.scraper import AdScraper
from source.sender import Sender

def main():
    print(f"\033[92mStarting Scraper\033[0m")
    scraper = AdScraper()
    scraper.scrapeAds()


if __name__ == "__main__":
    main()
