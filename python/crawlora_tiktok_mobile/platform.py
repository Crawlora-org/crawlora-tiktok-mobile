"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class TikTokMobileClient(CrawloraClient):
    """Synchronous TikTok Mobile API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-tiktok-mobile-python/0.1.0')
        super().__init__(*args, **kwargs)

    def anchor_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-anchor-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def collection_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-collection-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def collection_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-collection-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def collection_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-collection-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def comment_replies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-comment-replies', params, response_type=response_type, timeout=timeout, headers=headers)

    def comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    def feed_offline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-feed-offline', params, response_type=response_type, timeout=timeout, headers=headers)

    def feed_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-feed-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    def hashtag_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtag-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_room(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-room', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_room_by_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-room-by-user', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_beats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-beats', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_choices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-choices', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_collection_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-collection-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_pick(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-pick', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-related', params, response_type=response_type, timeout=timeout, headers=headers)

    def music_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    def mv_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-mv-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_media(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-media', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def place_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-place-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def playlist_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-playlist-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def playlist_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-playlist-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def playlist_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-playlist-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-music', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-place', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_pre_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-pre-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_stream(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-stream', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_sug(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-sug', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def translation_description(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-translation-description', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-trending-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-trending-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_followers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-followers', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_following(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-following', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_original_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-original-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_original_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-original-music', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-user-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    def video_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-video-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def video_subtitles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-video-subtitles', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncTikTokMobileClient(AsyncCrawloraClient):
    """Asynchronous TikTok Mobile API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-tiktok-mobile-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def anchor_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-anchor-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def collection_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-collection-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def collection_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-collection-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def collection_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-collection-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def comment_replies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-comment-replies', params, response_type=response_type, timeout=timeout, headers=headers)

    async def comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    async def feed_offline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-feed-offline', params, response_type=response_type, timeout=timeout, headers=headers)

    async def feed_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-feed-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hashtag_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtag-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_room(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-room', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_room_by_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-room-by-user', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_beats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-beats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_choices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-choices', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_collection_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-collection-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_pick(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-pick', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-related', params, response_type=response_type, timeout=timeout, headers=headers)

    async def music_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mv_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-mv-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_media(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-media', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def place_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-place-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playlist_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-playlist-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playlist_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-playlist-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playlist_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-playlist-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-music', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-place', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_pre_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-pre-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_stream(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-stream', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_sug(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-sug', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def translation_description(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-translation-description', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-trending-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-trending-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_followers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-followers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_following(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-following', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_original_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-original-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_original_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-original-music', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-user-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-video-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video_subtitles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-video-subtitles', params, response_type=response_type, timeout=timeout, headers=headers)
