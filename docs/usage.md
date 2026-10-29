# TikTok Mobile API endpoint reference and client usage

This reference lists all 63 public TikTok Mobile API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/tiktok-mobile`, `crawlora-tiktok-mobile`, and `crawlora-tiktok-mobile` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape TikTok Mobile locally; Crawlora is independent from and not endorsed by TikTok Mobile or its owners.

The package tracks the public API contract revision `sha256:e5c9adbb39f7461654081ba911e31925e6d1a5450715a23c0e51f392ecf6da7d` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `tiktok-mobile`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `anchorList` | `anchor_list` | `tiktok_mobile.anchor_list` | `GET /tiktok/mobile/anchor/list` | — | Anchor catalogue used by the video composer |
| `collectionDetail` | `collection_detail` | `tiktok_mobile.collection_detail` | `GET /tiktok/mobile/collection/detail` | `collection_id` (query, required) | Get TikTok collection detail on the mobile API |
| `collectionList` | `collection_list` | `tiktok_mobile.collection_list` | `GET /tiktok/mobile/collection/list` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List TikTok collections on the mobile API |
| `collectionVideos` | `collection_videos` | `tiktok_mobile.collection_videos` | `GET /tiktok/mobile/collection/videos` | `collection_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Get videos in a TikTok collection on the mobile API |
| `commentReplies` | `comment_replies` | `tiktok_mobile.comment_replies` | `GET /tiktok/mobile/comment/replies` | `aweme_id` (query, required), `comment_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve replies to a TikTok comment |
| `comments` | `comments` | `tiktok_mobile.comments` | `GET /tiktok/mobile/comments` | `aweme_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve comments for a TikTok video |
| `feed` | `feed` | `tiktok_mobile.feed` | `GET /tiktok/mobile/feed` | `count` (query, optional), `cursor` (query, optional) | Retrieve the TikTok mobile For You feed |
| `feedOffline` | `feed_offline` | `tiktok_mobile.feed_offline` | `GET /tiktok/mobile/feed/offline` | `pull_type` (query, optional), `count` (query, optional) | Fetch the app's cached-pull offline feed (protobuf) decoded without a schema |
| `feedPost` | `feed_post` | `tiktok_mobile.feed_post` | `GET /tiktok/mobile/feed/post` | — | Fetch the app's primary feed call (POST, protobuf) decoded without a schema |
| `hashtag` | `hashtag` | `tiktok_mobile.hashtag` | `GET /tiktok/mobile/hashtag` | `name` (query, required) | Retrieve a TikTok hashtag |
| `hashtagPosts` | `hashtag_posts` | `tiktok_mobile.hashtag_posts` | `GET /tiktok/mobile/hashtag/posts` | `name` (query, required), `sort` (query, optional; values: `fresh`, `popular`), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok hashtag |
| `hashtags` | `hashtags` | `tiktok_mobile.hashtags` | `GET /tiktok/mobile/hashtags` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok hashtags |
| `liveEffects` | `live_effects` | `tiktok_mobile.live_effects` | `GET /tiktok/mobile/live/effects` | — | Retrieve TikTok LIVE effects |
| `liveGifts` | `live_gifts` | `tiktok_mobile.live_gifts` | `GET /tiktok/mobile/live/gifts` | — | Retrieve TikTok LIVE gifts |
| `liveHashtags` | `live_hashtags` | `tiktok_mobile.live_hashtags` | `GET /tiktok/mobile/live/hashtags` | — | LIVE category/game reference catalogue (hashtags, live-studio/voice/third-party tags, game tags) |
| `liveRoom` | `live_room` | `tiktok_mobile.live_room` | `GET /tiktok/mobile/live/room` | `room_id` (query, required) | LIVE room detail: status, viewers, owner, stream URLs, cover |
| `liveRoomByUser` | `live_room_by_user` | `tiktok_mobile.live_room_by_user` | `GET /tiktok/mobile/live/room-by-user` | `user_id` (query, required) | LIVE room by user: the room a user is currently streaming |
| `liveSearch` | `live_search` | `tiktok_mobile.live_search` | `GET /tiktok/mobile/live/search` | `keyword` (query, required), `count` (query, optional) | Search TikTok LIVE streams |
| `liveTabs` | `live_tabs` | `tiktok_mobile.live_tabs` | `GET /tiktok/mobile/live/tabs` | — | Fetch the LIVE tab catalogue |
| `musicBeats` | `music_beats` | `tiktok_mobile.music_beats` | `GET /tiktok/mobile/music/beats` | `count` (query, optional) | Retrieve TikTok music beats |
| `musicChart` | `music_chart` | `tiktok_mobile.music_chart` | `GET /tiktok/mobile/music/chart` | `chart_region` (query, optional; values: `AE`, `BR`, `CA`, `DE`, `EG`, `FR`, `JP`, `KR`, `LB`, `MX`, `NG`, `SA`, `TR`, `US`, `ZA`), `cursor` (query, optional), `count` (query, optional) | List a regional TikTok sound chart |
| `musicChoices` | `music_choices` | `tiktok_mobile.music_choices` | `GET /tiktok/mobile/music/choices` | — | Recommended sounds for video creation |
| `musicCollectionList` | `music_collection_list` | `tiktok_mobile.music_collection_list` | `GET /tiktok/mobile/music/collection-list` | `count` (query, optional), `cursor` (query, optional) | Music collection list (paged browse) |
| `musicCollections` | `music_collections` | `tiktok_mobile.music_collections` | `GET /tiktok/mobile/music/collections` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok music collections |
| `musicDetail` | `music_detail` | `tiktok_mobile.music_detail` | `GET /tiktok/mobile/music/detail` | `music_id` (query, required) | Retrieve one TikTok sound |
| `musicPick` | `music_pick` | `tiktok_mobile.music_pick` | `GET /tiktok/mobile/music/pick` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok sound chart picks |
| `musicPosts` | `music_posts` | `tiktok_mobile.music_posts` | `GET /tiktok/mobile/music/posts` | `music_id` (query, required), `sort` (query, optional; values: `fresh`, `popular`), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok sound |
| `musicRelated` | `music_related` | `tiktok_mobile.music_related` | `GET /tiktok/mobile/music/related` | `aweme_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve sounds related to a TikTok video |
| `musicTrending` | `music_trending` | `tiktok_mobile.music_trending` | `GET /tiktok/mobile/music/trending` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending sounds |
| `mvVideos` | `mv_videos` | `tiktok_mobile.mv_videos` | `GET /tiktok/mobile/mv/videos` | `mv_id` (query, required), `cursor` (query, optional) | MV channel feed: the app's music-video tab, paged |
| `placeDetail` | `place_detail` | `tiktok_mobile.place_detail` | `GET /tiktok/mobile/place/detail` | `poi_id` (query, required), `review_count` (query, optional), `review_cursor` (query, optional), `merged_count` (query, optional), `video_cursor` (query, optional), `enter_from` (query, optional) | Place (POI) detail from the mobile app's Places surface |
| `placeInfo` | `place_info` | `tiktok_mobile.place_info` | `GET /tiktok/mobile/place/info` | `poi_id` (query, required) | Compact place (POI) record: address, coordinates, rating, hours, counters |
| `placeMedia` | `place_media` | `tiktok_mobile.place_media` | `GET /tiktok/mobile/place/media` | `poi_id` (query, required), `cursor` (query, optional), `size` (query, optional), `data_version` (query, optional) | List a TikTok place's mixed media |
| `placePhotos` | `place_photos` | `tiktok_mobile.place_photos` | `GET /tiktok/mobile/place/photos` | `poi_id` (query, required) | Place photo album with per-photo attribution |
| `placeReviews` | `place_reviews` | `tiktok_mobile.place_reviews` | `GET /tiktok/mobile/place/reviews` | `poi_id` (query, required), `cursor` (query, optional), `count` (query, optional), `sort_type` (query, optional; values: `1`, `2`) | List a TikTok place's reviews |
| `placeVideos` | `place_videos` | `tiktok_mobile.place_videos` | `GET /tiktok/mobile/place/videos` | `poi_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Videos posted at one place (paged) |
| `playlistDetail` | `playlist_detail` | `tiktok_mobile.playlist_detail` | `GET /tiktok/mobile/playlist/detail` | `mix_id` (query, required), `user_id` (query, optional), `sec_user_id` (query, optional) | Retrieve one TikTok playlist |
| `playlistList` | `playlist_list` | `tiktok_mobile.playlist_list` | `GET /tiktok/mobile/playlist/list` | `user_id` (query, optional), `sec_user_id` (query, optional), `cursor` (query, optional) | List a creator's TikTok playlists |
| `playlistVideos` | `playlist_videos` | `tiktok_mobile.playlist_videos` | `GET /tiktok/mobile/playlist/videos` | `mix_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a playlist's videos |
| `search` | `search` | `tiktok_mobile.search` | `GET /tiktok/mobile/search` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `search_id` (query, optional) | Search TikTok videos on the mobile API |
| `searchEffects` | `search_effects` | `tiktok_mobile.search_effects` | `GET /tiktok/mobile/search/effects` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional), `search_id` (query, optional) | Search TikTok effects/stickers by keyword |
| `searchHashtags` | `search_hashtags` | `tiktok_mobile.search_hashtags` | `GET /tiktok/mobile/search/hashtags` | `keyword` (query, required), `count` (query, optional) | Hashtag suggestions for a keyword (hashtag typeahead) |
| `searchMusic` | `search_music` | `tiktok_mobile.search_music` | `GET /tiktok/mobile/search/music` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional) | Search TikTok sounds on the mobile API |
| `searchPhotos` | `search_photos` | `tiktok_mobile.search_photos` | `GET /tiktok/mobile/search/photos` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `sort_type` (query, optional), `publish_time` (query, optional), `search_source` (query, optional) | Search the mobile app's photo-post tab |
| `searchPlace` | `search_place` | `tiktok_mobile.search_place` | `GET /tiktok/mobile/search/place` | `keyword` (query, required), `count` (query, optional) | Search TikTok places |
| `searchPreInfo` | `search_pre_info` | `tiktok_mobile.search_pre_info` | `GET /tiktok/mobile/search/pre-info` | `keyword` (query, optional), `count` (query, optional) | Pre-search info token for a search session |
| `searchStream` | `search_stream` | `tiktok_mobile.search_stream` | `GET /tiktok/mobile/search/stream` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `search_source` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `3`), `publish_time` (query, optional), `filter_selected` (query, optional) | Run the app's primary (streaming) general search |
| `searchSug` | `search_sug` | `tiktok_mobile.search_sug` | `GET /tiktok/mobile/search/sug` | `keyword` (query, required), `count` (query, optional) | Retrieve TikTok search suggestions |
| `searchTabs` | `search_tabs` | `tiktok_mobile.search_tabs` | `GET /tiktok/mobile/search/tabs` | `keyword` (query, required) | Search tabs available for a keyword |
| `searchUser` | `search_user` | `tiktok_mobile.search_user` | `GET /tiktok/mobile/search/user` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok users on the mobile API |
| `searchVideos` | `search_videos` | `tiktok_mobile.search_videos` | `GET /tiktok/mobile/search/videos` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `3`), `publish_time` (query, optional), `search_source` (query, optional), `search_id` (query, optional) | Search TikTok videos on the mobile API (video tab) |
| `translationDescription` | `translation_description` | `tiktok_mobile.translation_description` | `GET /tiktok/mobile/translation/description` | `item_id` (query, required), `target_lang` (query, optional) | Translate one TikTok video caption |
| `trendingCategories` | `trending_categories` | `tiktok_mobile.trending_categories` | `GET /tiktok/mobile/trending/categories` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending categories |
| `trendingEffects` | `trending_effects` | `tiktok_mobile.trending_effects` | `GET /tiktok/mobile/trending/effects` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending effects |
| `userFollowers` | `user_followers` | `tiktok_mobile.user_followers` | `GET /tiktok/mobile/user/followers` | `user_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve the followers of a TikTok creator |
| `userFollowing` | `user_following` | `tiktok_mobile.user_following` | `GET /tiktok/mobile/user/following` | `user_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve the accounts a TikTok creator follows |
| `userOriginalEffects` | `user_original_effects` | `tiktok_mobile.user_original_effects` | `GET /tiktok/mobile/user/original-effects` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a creator's original TikTok effects |
| `userOriginalMusic` | `user_original_music` | `tiktok_mobile.user_original_music` | `GET /tiktok/mobile/user/original-music` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a creator's original TikTok sounds |
| `userPosts` | `user_posts` | `tiktok_mobile.user_posts` | `GET /tiktok/mobile/user/posts` | `user_id` (query, optional), `sec_user_id` (query, optional), `count` (query, optional), `cursor` (query, optional), `sort_type` (query, optional) | Retrieve the videos posted by a TikTok creator |
| `userProfile` | `user_profile` | `tiktok_mobile.user_profile` | `GET /tiktok/mobile/user/profile` | `user_id` (query, optional), `sec_user_id` (query, optional) | Retrieve a TikTok creator profile |
| `userRecommendations` | `user_recommendations` | `tiktok_mobile.user_recommendations` | `GET /tiktok/mobile/user/recommendations` | `count` (query, optional) | Recommended creators on the mobile app's Following page |
| `videoDetail` | `video_detail` | `tiktok_mobile.video_detail` | `GET /tiktok/mobile/video/detail` | `aweme_id` (query, required) | Retrieve one TikTok video |
| `videoSubtitles` | `video_subtitles` | `tiktok_mobile.video_subtitles` | `GET /tiktok/mobile/video/subtitles` | `video_id` (query, required), `language` (query, required) | Video captions translated into a target language |

## Client forms

- JavaScript: import `TikTokMobileClient` (also exported as `Client`) from `@crawlora-org/tiktok-mobile`; use `new TikTokMobileClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `TikTokMobileClient` (also exported as `Client`) from `crawlora_tiktok_mobile`; use `with TikTokMobileClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncTikTokMobileClient`, used with `async with` and `await`.
- Rust: add `crawlora-tiktok-mobile` with Cargo; import `Client` and the generated operation parameter struct, then call `client.tiktok-mobile.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-tiktok-mobile/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
