# @crawlora-org/tiktok-mobile — TikTok Mobile API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted TikTok Mobile API.
It exposes 63 API endpoints for mobile feed, search, video, creator, music, LIVE, and place endpoints through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-mobile-javascript-homepage). It does not run a browser or scrape TikTok Mobile locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by TikTok Mobile or its owners.

## Install

```sh
npm install @crawlora-org/tiktok-mobile
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-mobile-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-mobile-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { TikTokMobileClient } from "@crawlora-org/tiktok-mobile";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new TikTokMobileClient({ apiKey });
const result1 = await client.feed({});
console.log(result1);
const result2 = await client.searchSug({ keyword: "science" });
console.log(result2);
```

The client also exports `Client` as an alias for `TikTokMobileClient`. Operation
methods are available directly in camelCase and through the `tiktok-mobile`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-tiktok-mobile/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-tiktok-mobile/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported TikTok Mobile API endpoints

This package exposes each route below as a direct method and through the `tiktok-mobile` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-tiktok-mobile/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/tiktok/mobile/anchor/list` | `tiktok-mobile-anchor-list` | Anchor catalogue used by the video composer |
| `GET` | `/tiktok/mobile/collection/detail` | `tiktok-mobile-collection-detail` | Get TikTok collection detail on the mobile API |
| `GET` | `/tiktok/mobile/collection/list` | `tiktok-mobile-collection-list` | List TikTok collections on the mobile API |
| `GET` | `/tiktok/mobile/collection/videos` | `tiktok-mobile-collection-videos` | Get videos in a TikTok collection on the mobile API |
| `GET` | `/tiktok/mobile/comment/replies` | `tiktok-mobile-comment-replies` | Retrieve replies to a TikTok comment |
| `GET` | `/tiktok/mobile/comments` | `tiktok-mobile-comments` | Retrieve comments for a TikTok video |
| `GET` | `/tiktok/mobile/feed` | `tiktok-mobile-feed` | Retrieve the TikTok mobile For You feed |
| `GET` | `/tiktok/mobile/feed/offline` | `tiktok-mobile-feed-offline` | Fetch the app's cached-pull offline feed (protobuf) decoded without a schema |
| `GET` | `/tiktok/mobile/feed/post` | `tiktok-mobile-feed-post` | Fetch the app's primary feed call (POST, protobuf) decoded without a schema |
| `GET` | `/tiktok/mobile/hashtag` | `tiktok-mobile-hashtag` | Retrieve a TikTok hashtag |
| `GET` | `/tiktok/mobile/hashtag/posts` | `tiktok-mobile-hashtag-posts` | Retrieve videos for a TikTok hashtag |
| `GET` | `/tiktok/mobile/hashtags` | `tiktok-mobile-hashtags` | Search TikTok hashtags |
| `GET` | `/tiktok/mobile/live/effects` | `tiktok-mobile-live-effects` | Retrieve TikTok LIVE effects |
| `GET` | `/tiktok/mobile/live/gifts` | `tiktok-mobile-live-gifts` | Retrieve TikTok LIVE gifts |
| `GET` | `/tiktok/mobile/live/hashtags` | `tiktok-mobile-live-hashtags` | LIVE category/game reference catalogue (hashtags, live-studio/voice/third-party tags, game tags) |
| `GET` | `/tiktok/mobile/live/room` | `tiktok-mobile-live-room` | LIVE room detail: status, viewers, owner, stream URLs, cover |
| `GET` | `/tiktok/mobile/live/room-by-user` | `tiktok-mobile-live-room-by-user` | LIVE room by user: the room a user is currently streaming |
| `GET` | `/tiktok/mobile/live/search` | `tiktok-mobile-live-search` | Search TikTok LIVE streams |
| `GET` | `/tiktok/mobile/live/tabs` | `tiktok-mobile-live-tabs` | Fetch the LIVE tab catalogue |
| `GET` | `/tiktok/mobile/music/beats` | `tiktok-mobile-music-beats` | Retrieve TikTok music beats |
| `GET` | `/tiktok/mobile/music/chart` | `tiktok-mobile-music-chart` | List a regional TikTok sound chart |
| `GET` | `/tiktok/mobile/music/choices` | `tiktok-mobile-music-choices` | Recommended sounds for video creation |
| `GET` | `/tiktok/mobile/music/collection-list` | `tiktok-mobile-music-collection-list` | Music collection list (paged browse) |
| `GET` | `/tiktok/mobile/music/collections` | `tiktok-mobile-music-collections` | Retrieve TikTok music collections |
| `GET` | `/tiktok/mobile/music/detail` | `tiktok-mobile-music-detail` | Retrieve one TikTok sound |
| `GET` | `/tiktok/mobile/music/pick` | `tiktok-mobile-music-pick` | Retrieve TikTok sound chart picks |
| `GET` | `/tiktok/mobile/music/posts` | `tiktok-mobile-music-posts` | Retrieve videos for a TikTok sound |
| `GET` | `/tiktok/mobile/music/related` | `tiktok-mobile-music-related` | Retrieve sounds related to a TikTok video |
| `GET` | `/tiktok/mobile/music/trending` | `tiktok-mobile-music-trending` | Retrieve TikTok trending sounds |
| `GET` | `/tiktok/mobile/mv/videos` | `tiktok-mobile-mv-videos` | MV channel feed: the app's music-video tab, paged |
| `GET` | `/tiktok/mobile/place/detail` | `tiktok-mobile-place-detail` | Place (POI) detail from the mobile app's Places surface |
| `GET` | `/tiktok/mobile/place/info` | `tiktok-mobile-place-info` | Compact place (POI) record: address, coordinates, rating, hours, counters |
| `GET` | `/tiktok/mobile/place/media` | `tiktok-mobile-place-media` | List a TikTok place's mixed media |
| `GET` | `/tiktok/mobile/place/photos` | `tiktok-mobile-place-photos` | Place photo album with per-photo attribution |
| `GET` | `/tiktok/mobile/place/reviews` | `tiktok-mobile-place-reviews` | List a TikTok place's reviews |
| `GET` | `/tiktok/mobile/place/videos` | `tiktok-mobile-place-videos` | Videos posted at one place (paged) |
| `GET` | `/tiktok/mobile/playlist/detail` | `tiktok-mobile-playlist-detail` | Retrieve one TikTok playlist |
| `GET` | `/tiktok/mobile/playlist/list` | `tiktok-mobile-playlist-list` | List a creator's TikTok playlists |
| `GET` | `/tiktok/mobile/playlist/videos` | `tiktok-mobile-playlist-videos` | List a playlist's videos |
| `GET` | `/tiktok/mobile/search` | `tiktok-mobile-search` | Search TikTok videos on the mobile API |
| `GET` | `/tiktok/mobile/search/effects` | `tiktok-mobile-search-effects` | Search TikTok effects/stickers by keyword |
| `GET` | `/tiktok/mobile/search/hashtags` | `tiktok-mobile-search-hashtags` | Hashtag suggestions for a keyword (hashtag typeahead) |
| `GET` | `/tiktok/mobile/search/music` | `tiktok-mobile-search-music` | Search TikTok sounds on the mobile API |
| `GET` | `/tiktok/mobile/search/photos` | `tiktok-mobile-search-photos` | Search the mobile app's photo-post tab |
| `GET` | `/tiktok/mobile/search/place` | `tiktok-mobile-search-place` | Search TikTok places |
| `GET` | `/tiktok/mobile/search/pre-info` | `tiktok-mobile-search-pre-info` | Pre-search info token for a search session |
| `GET` | `/tiktok/mobile/search/stream` | `tiktok-mobile-search-stream` | Run the app's primary (streaming) general search |
| `GET` | `/tiktok/mobile/search/sug` | `tiktok-mobile-search-sug` | Retrieve TikTok search suggestions |
| `GET` | `/tiktok/mobile/search/tabs` | `tiktok-mobile-search-tabs` | Search tabs available for a keyword |
| `GET` | `/tiktok/mobile/search/user` | `tiktok-mobile-search-user` | Search TikTok users on the mobile API |
| `GET` | `/tiktok/mobile/search/videos` | `tiktok-mobile-search-videos` | Search TikTok videos on the mobile API (video tab) |
| `GET` | `/tiktok/mobile/translation/description` | `tiktok-mobile-translation-description` | Translate one TikTok video caption |
| `GET` | `/tiktok/mobile/trending/categories` | `tiktok-mobile-trending-categories` | Retrieve TikTok trending categories |
| `GET` | `/tiktok/mobile/trending/effects` | `tiktok-mobile-trending-effects` | Retrieve TikTok trending effects |
| `GET` | `/tiktok/mobile/user/followers` | `tiktok-mobile-user-followers` | Retrieve the followers of a TikTok creator |
| `GET` | `/tiktok/mobile/user/following` | `tiktok-mobile-user-following` | Retrieve the accounts a TikTok creator follows |
| `GET` | `/tiktok/mobile/user/original-effects` | `tiktok-mobile-user-original-effects` | List a creator's original TikTok effects |
| `GET` | `/tiktok/mobile/user/original-music` | `tiktok-mobile-user-original-music` | List a creator's original TikTok sounds |
| `GET` | `/tiktok/mobile/user/posts` | `tiktok-mobile-user-posts` | Retrieve the videos posted by a TikTok creator |
| `GET` | `/tiktok/mobile/user/profile` | `tiktok-mobile-user-profile` | Retrieve a TikTok creator profile |
| `GET` | `/tiktok/mobile/user/recommendations` | `tiktok-mobile-user-recommendations` | Recommended creators on the mobile app's Following page |
| `GET` | `/tiktok/mobile/video/detail` | `tiktok-mobile-video-detail` | Retrieve one TikTok video |
| `GET` | `/tiktok/mobile/video/subtitles` | `tiktok-mobile-video-subtitles` | Video captions translated into a target language |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
