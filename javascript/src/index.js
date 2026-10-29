import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class TikTokMobileClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-tiktok-mobile-js/0.1.0" });
    this["anchorList"] = (...args) => this.request("tiktok-mobile-anchor-list", ...args);
    this["collectionDetail"] = (...args) => this.request("tiktok-mobile-collection-detail", ...args);
    this["collectionList"] = (...args) => this.request("tiktok-mobile-collection-list", ...args);
    this["collectionVideos"] = (...args) => this.request("tiktok-mobile-collection-videos", ...args);
    this["commentReplies"] = (...args) => this.request("tiktok-mobile-comment-replies", ...args);
    this["comments"] = (...args) => this.request("tiktok-mobile-comments", ...args);
    this["feed"] = (...args) => this.request("tiktok-mobile-feed", ...args);
    this["feedOffline"] = (...args) => this.request("tiktok-mobile-feed-offline", ...args);
    this["feedPost"] = (...args) => this.request("tiktok-mobile-feed-post", ...args);
    this["hashtag"] = (...args) => this.request("tiktok-mobile-hashtag", ...args);
    this["hashtagPosts"] = (...args) => this.request("tiktok-mobile-hashtag-posts", ...args);
    this["hashtags"] = (...args) => this.request("tiktok-mobile-hashtags", ...args);
    this["liveEffects"] = (...args) => this.request("tiktok-mobile-live-effects", ...args);
    this["liveGifts"] = (...args) => this.request("tiktok-mobile-live-gifts", ...args);
    this["liveHashtags"] = (...args) => this.request("tiktok-mobile-live-hashtags", ...args);
    this["liveRoom"] = (...args) => this.request("tiktok-mobile-live-room", ...args);
    this["liveRoomByUser"] = (...args) => this.request("tiktok-mobile-live-room-by-user", ...args);
    this["liveSearch"] = (...args) => this.request("tiktok-mobile-live-search", ...args);
    this["liveTabs"] = (...args) => this.request("tiktok-mobile-live-tabs", ...args);
    this["musicBeats"] = (...args) => this.request("tiktok-mobile-music-beats", ...args);
    this["musicChart"] = (...args) => this.request("tiktok-mobile-music-chart", ...args);
    this["musicChoices"] = (...args) => this.request("tiktok-mobile-music-choices", ...args);
    this["musicCollectionList"] = (...args) => this.request("tiktok-mobile-music-collection-list", ...args);
    this["musicCollections"] = (...args) => this.request("tiktok-mobile-music-collections", ...args);
    this["musicDetail"] = (...args) => this.request("tiktok-mobile-music-detail", ...args);
    this["musicPick"] = (...args) => this.request("tiktok-mobile-music-pick", ...args);
    this["musicPosts"] = (...args) => this.request("tiktok-mobile-music-posts", ...args);
    this["musicRelated"] = (...args) => this.request("tiktok-mobile-music-related", ...args);
    this["musicTrending"] = (...args) => this.request("tiktok-mobile-music-trending", ...args);
    this["mvVideos"] = (...args) => this.request("tiktok-mobile-mv-videos", ...args);
    this["placeDetail"] = (...args) => this.request("tiktok-mobile-place-detail", ...args);
    this["placeInfo"] = (...args) => this.request("tiktok-mobile-place-info", ...args);
    this["placeMedia"] = (...args) => this.request("tiktok-mobile-place-media", ...args);
    this["placePhotos"] = (...args) => this.request("tiktok-mobile-place-photos", ...args);
    this["placeReviews"] = (...args) => this.request("tiktok-mobile-place-reviews", ...args);
    this["placeVideos"] = (...args) => this.request("tiktok-mobile-place-videos", ...args);
    this["playlistDetail"] = (...args) => this.request("tiktok-mobile-playlist-detail", ...args);
    this["playlistList"] = (...args) => this.request("tiktok-mobile-playlist-list", ...args);
    this["playlistVideos"] = (...args) => this.request("tiktok-mobile-playlist-videos", ...args);
    this["search"] = (...args) => this.request("tiktok-mobile-search", ...args);
    this["searchEffects"] = (...args) => this.request("tiktok-mobile-search-effects", ...args);
    this["searchHashtags"] = (...args) => this.request("tiktok-mobile-search-hashtags", ...args);
    this["searchMusic"] = (...args) => this.request("tiktok-mobile-search-music", ...args);
    this["searchPhotos"] = (...args) => this.request("tiktok-mobile-search-photos", ...args);
    this["searchPlace"] = (...args) => this.request("tiktok-mobile-search-place", ...args);
    this["searchPreInfo"] = (...args) => this.request("tiktok-mobile-search-pre-info", ...args);
    this["searchStream"] = (...args) => this.request("tiktok-mobile-search-stream", ...args);
    this["searchSug"] = (...args) => this.request("tiktok-mobile-search-sug", ...args);
    this["searchTabs"] = (...args) => this.request("tiktok-mobile-search-tabs", ...args);
    this["searchUser"] = (...args) => this.request("tiktok-mobile-search-user", ...args);
    this["searchVideos"] = (...args) => this.request("tiktok-mobile-search-videos", ...args);
    this["translationDescription"] = (...args) => this.request("tiktok-mobile-translation-description", ...args);
    this["trendingCategories"] = (...args) => this.request("tiktok-mobile-trending-categories", ...args);
    this["trendingEffects"] = (...args) => this.request("tiktok-mobile-trending-effects", ...args);
    this["userFollowers"] = (...args) => this.request("tiktok-mobile-user-followers", ...args);
    this["userFollowing"] = (...args) => this.request("tiktok-mobile-user-following", ...args);
    this["userOriginalEffects"] = (...args) => this.request("tiktok-mobile-user-original-effects", ...args);
    this["userOriginalMusic"] = (...args) => this.request("tiktok-mobile-user-original-music", ...args);
    this["userPosts"] = (...args) => this.request("tiktok-mobile-user-posts", ...args);
    this["userProfile"] = (...args) => this.request("tiktok-mobile-user-profile", ...args);
    this["userRecommendations"] = (...args) => this.request("tiktok-mobile-user-recommendations", ...args);
    this["videoDetail"] = (...args) => this.request("tiktok-mobile-video-detail", ...args);
    this["videoSubtitles"] = (...args) => this.request("tiktok-mobile-video-subtitles", ...args);
  }
}

export { TikTokMobileClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default TikTokMobileClient;
