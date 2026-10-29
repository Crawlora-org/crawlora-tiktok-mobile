"""Typed TikTok Mobile client for the Crawlora hosted API."""

from .platform import TikTokMobileClient, AsyncTikTokMobileClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokMobileClient
AsyncClient = AsyncTikTokMobileClient
__version__ = '0.1.0'
DISPLAY_NAME = 'TikTok Mobile'
PLATFORM = 'tiktok-mobile'
CONTRACT_REVISION = 'sha256:e5c9adbb39f7461654081ba911e31925e6d1a5450715a23c0e51f392ecf6da7d'

__all__ = [
    "TikTokMobileClient", "AsyncTikTokMobileClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
