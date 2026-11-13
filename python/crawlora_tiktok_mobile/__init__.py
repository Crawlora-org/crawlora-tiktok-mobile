"""Typed TikTok Mobile client for the Crawlora hosted API."""

from .platform import TikTokMobileClient, AsyncTikTokMobileClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokMobileClient
AsyncClient = AsyncTikTokMobileClient
__version__ = '0.1.1'
DISPLAY_NAME = 'TikTok Mobile'
PLATFORM = 'tiktok-mobile'
CONTRACT_REVISION = 'sha256:37665fe483e1520869d00ae27595b9d2f38b8eacf77cdf4923d4b21df4c1daf1'

__all__ = [
    "TikTokMobileClient", "AsyncTikTokMobileClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
