import os

from crawlora_tiktok_mobile import TikTokMobileClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with TikTokMobileClient(api_key=api_key) as client:
    feed = client.feed()
    print('feed', feed)
    search_sug = client.search_sug(keyword='science')
    print('search_sug', search_sug)
