package net.crawlora.tiktok_mobile;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the TikTok Mobile endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 63;
    public static final List<String> OPERATION_IDS = List.of(
            "tiktok-mobile-anchor-list",
            "tiktok-mobile-collection-detail",
            "tiktok-mobile-collection-list",
            "tiktok-mobile-collection-videos",
            "tiktok-mobile-comment-replies",
            "tiktok-mobile-comments",
            "tiktok-mobile-feed",
            "tiktok-mobile-feed-offline",
            "tiktok-mobile-feed-post",
            "tiktok-mobile-hashtag",
            "tiktok-mobile-hashtag-posts",
            "tiktok-mobile-hashtags",
            "tiktok-mobile-live-effects",
            "tiktok-mobile-live-gifts",
            "tiktok-mobile-live-hashtags",
            "tiktok-mobile-live-room",
            "tiktok-mobile-live-room-by-user",
            "tiktok-mobile-live-search",
            "tiktok-mobile-live-tabs",
            "tiktok-mobile-music-beats",
            "tiktok-mobile-music-chart",
            "tiktok-mobile-music-choices",
            "tiktok-mobile-music-collection-list",
            "tiktok-mobile-music-collections",
            "tiktok-mobile-music-detail",
            "tiktok-mobile-music-pick",
            "tiktok-mobile-music-posts",
            "tiktok-mobile-music-related",
            "tiktok-mobile-music-trending",
            "tiktok-mobile-mv-videos",
            "tiktok-mobile-place-detail",
            "tiktok-mobile-place-info",
            "tiktok-mobile-place-media",
            "tiktok-mobile-place-photos",
            "tiktok-mobile-place-reviews",
            "tiktok-mobile-place-videos",
            "tiktok-mobile-playlist-detail",
            "tiktok-mobile-playlist-list",
            "tiktok-mobile-playlist-videos",
            "tiktok-mobile-search",
            "tiktok-mobile-search-effects",
            "tiktok-mobile-search-hashtags",
            "tiktok-mobile-search-music",
            "tiktok-mobile-search-photos",
            "tiktok-mobile-search-place",
            "tiktok-mobile-search-pre-info",
            "tiktok-mobile-search-stream",
            "tiktok-mobile-search-sug",
            "tiktok-mobile-search-tabs",
            "tiktok-mobile-search-user",
            "tiktok-mobile-search-videos",
            "tiktok-mobile-translation-description",
            "tiktok-mobile-trending-categories",
            "tiktok-mobile-trending-effects",
            "tiktok-mobile-user-followers",
            "tiktok-mobile-user-following",
            "tiktok-mobile-user-original-effects",
            "tiktok-mobile-user-original-music",
            "tiktok-mobile-user-posts",
            "tiktok-mobile-user-profile",
            "tiktok-mobile-user-recommendations",
            "tiktok-mobile-video-detail",
            "tiktok-mobile-video-subtitles"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("tiktok-mobile-anchor-list", new Operation("tiktok-mobile-anchor-list", "GET", "/tiktok/mobile/anchor/list", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-collection-detail", new Operation("tiktok-mobile-collection-detail", "GET", "/tiktok/mobile/collection/detail", Map.ofEntries(Map.entry("collection_id", new Param("collection_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-collection-list", new Operation("tiktok-mobile-collection-list", "GET", "/tiktok/mobile/collection/list", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-collection-videos", new Operation("tiktok-mobile-collection-videos", "GET", "/tiktok/mobile/collection/videos", Map.ofEntries(Map.entry("collection_id", new Param("collection_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-comment-replies", new Operation("tiktok-mobile-comment-replies", "GET", "/tiktok/mobile/comment/replies", Map.ofEntries(Map.entry("aweme_id", new Param("aweme_id", "query", true, "string", List.of(), "csv")), Map.entry("comment_id", new Param("comment_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-comments", new Operation("tiktok-mobile-comments", "GET", "/tiktok/mobile/comments", Map.ofEntries(Map.entry("aweme_id", new Param("aweme_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-feed", new Operation("tiktok-mobile-feed", "GET", "/tiktok/mobile/feed", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-feed-offline", new Operation("tiktok-mobile-feed-offline", "GET", "/tiktok/mobile/feed/offline", Map.ofEntries(Map.entry("pull_type", new Param("pull_type", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-feed-post", new Operation("tiktok-mobile-feed-post", "GET", "/tiktok/mobile/feed/post", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-hashtag", new Operation("tiktok-mobile-hashtag", "GET", "/tiktok/mobile/hashtag", Map.ofEntries(Map.entry("name", new Param("name", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-hashtag-posts", new Operation("tiktok-mobile-hashtag-posts", "GET", "/tiktok/mobile/hashtag/posts", Map.ofEntries(Map.entry("name", new Param("name", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("fresh", "popular"), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-hashtags", new Operation("tiktok-mobile-hashtags", "GET", "/tiktok/mobile/hashtags", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-live-effects", new Operation("tiktok-mobile-live-effects", "GET", "/tiktok/mobile/live/effects", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-live-gifts", new Operation("tiktok-mobile-live-gifts", "GET", "/tiktok/mobile/live/gifts", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-live-hashtags", new Operation("tiktok-mobile-live-hashtags", "GET", "/tiktok/mobile/live/hashtags", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-live-room", new Operation("tiktok-mobile-live-room", "GET", "/tiktok/mobile/live/room", Map.ofEntries(Map.entry("room_id", new Param("room_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-live-room-by-user", new Operation("tiktok-mobile-live-room-by-user", "GET", "/tiktok/mobile/live/room-by-user", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-live-search", new Operation("tiktok-mobile-live-search", "GET", "/tiktok/mobile/live/search", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-live-tabs", new Operation("tiktok-mobile-live-tabs", "GET", "/tiktok/mobile/live/tabs", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-music-beats", new Operation("tiktok-mobile-music-beats", "GET", "/tiktok/mobile/music/beats", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-chart", new Operation("tiktok-mobile-music-chart", "GET", "/tiktok/mobile/music/chart", Map.ofEntries(Map.entry("chart_region", new Param("chart_region", "query", false, "string", List.of("AE", "BR", "CA", "DE", "EG", "FR", "JP", "KR", "LB", "MX", "NG", "SA", "TR", "US", "ZA"), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-choices", new Operation("tiktok-mobile-music-choices", "GET", "/tiktok/mobile/music/choices", Map.of(), List.of("application/json")));
        operations.put("tiktok-mobile-music-collection-list", new Operation("tiktok-mobile-music-collection-list", "GET", "/tiktok/mobile/music/collection-list", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-collections", new Operation("tiktok-mobile-music-collections", "GET", "/tiktok/mobile/music/collections", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-detail", new Operation("tiktok-mobile-music-detail", "GET", "/tiktok/mobile/music/detail", Map.ofEntries(Map.entry("music_id", new Param("music_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-pick", new Operation("tiktok-mobile-music-pick", "GET", "/tiktok/mobile/music/pick", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-posts", new Operation("tiktok-mobile-music-posts", "GET", "/tiktok/mobile/music/posts", Map.ofEntries(Map.entry("music_id", new Param("music_id", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("fresh", "popular"), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-related", new Operation("tiktok-mobile-music-related", "GET", "/tiktok/mobile/music/related", Map.ofEntries(Map.entry("aweme_id", new Param("aweme_id", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-music-trending", new Operation("tiktok-mobile-music-trending", "GET", "/tiktok/mobile/music/trending", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-mv-videos", new Operation("tiktok-mobile-mv-videos", "GET", "/tiktok/mobile/mv/videos", Map.ofEntries(Map.entry("mv_id", new Param("mv_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-detail", new Operation("tiktok-mobile-place-detail", "GET", "/tiktok/mobile/place/detail", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv")), Map.entry("review_count", new Param("review_count", "query", false, "integer", List.of(), "csv")), Map.entry("review_cursor", new Param("review_cursor", "query", false, "integer", List.of(), "csv")), Map.entry("merged_count", new Param("merged_count", "query", false, "integer", List.of(), "csv")), Map.entry("video_cursor", new Param("video_cursor", "query", false, "integer", List.of(), "csv")), Map.entry("enter_from", new Param("enter_from", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-info", new Operation("tiktok-mobile-place-info", "GET", "/tiktok/mobile/place/info", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-media", new Operation("tiktok-mobile-place-media", "GET", "/tiktok/mobile/place/media", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv")), Map.entry("size", new Param("size", "query", false, "integer", List.of(), "csv")), Map.entry("data_version", new Param("data_version", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-photos", new Operation("tiktok-mobile-place-photos", "GET", "/tiktok/mobile/place/photos", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-reviews", new Operation("tiktok-mobile-place-reviews", "GET", "/tiktok/mobile/place/reviews", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of("1", "2"), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-place-videos", new Operation("tiktok-mobile-place-videos", "GET", "/tiktok/mobile/place/videos", Map.ofEntries(Map.entry("poi_id", new Param("poi_id", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-playlist-detail", new Operation("tiktok-mobile-playlist-detail", "GET", "/tiktok/mobile/playlist/detail", Map.ofEntries(Map.entry("mix_id", new Param("mix_id", "query", true, "string", List.of(), "csv")), Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv")), Map.entry("sec_user_id", new Param("sec_user_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-playlist-list", new Operation("tiktok-mobile-playlist-list", "GET", "/tiktok/mobile/playlist/list", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv")), Map.entry("sec_user_id", new Param("sec_user_id", "query", false, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-playlist-videos", new Operation("tiktok-mobile-playlist-videos", "GET", "/tiktok/mobile/playlist/videos", Map.ofEntries(Map.entry("mix_id", new Param("mix_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search", new Operation("tiktok-mobile-search", "GET", "/tiktok/mobile/search", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("search_id", new Param("search_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-effects", new Operation("tiktok-mobile-search-effects", "GET", "/tiktok/mobile/search/effects", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("search_id", new Param("search_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-hashtags", new Operation("tiktok-mobile-search-hashtags", "GET", "/tiktok/mobile/search/hashtags", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-music", new Operation("tiktok-mobile-search-music", "GET", "/tiktok/mobile/search/music", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-photos", new Operation("tiktok-mobile-search-photos", "GET", "/tiktok/mobile/search/photos", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of(), "csv")), Map.entry("publish_time", new Param("publish_time", "query", false, "integer", List.of(), "csv")), Map.entry("search_source", new Param("search_source", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-place", new Operation("tiktok-mobile-search-place", "GET", "/tiktok/mobile/search/place", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-pre-info", new Operation("tiktok-mobile-search-pre-info", "GET", "/tiktok/mobile/search/pre-info", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", false, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-stream", new Operation("tiktok-mobile-search-stream", "GET", "/tiktok/mobile/search/stream", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("search_source", new Param("search_source", "query", false, "string", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of("0", "1", "3"), "csv")), Map.entry("publish_time", new Param("publish_time", "query", false, "integer", List.of(), "csv")), Map.entry("filter_selected", new Param("filter_selected", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-sug", new Operation("tiktok-mobile-search-sug", "GET", "/tiktok/mobile/search/sug", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-tabs", new Operation("tiktok-mobile-search-tabs", "GET", "/tiktok/mobile/search/tabs", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-user", new Operation("tiktok-mobile-search-user", "GET", "/tiktok/mobile/search/user", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-search-videos", new Operation("tiktok-mobile-search-videos", "GET", "/tiktok/mobile/search/videos", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of("0", "1", "3"), "csv")), Map.entry("publish_time", new Param("publish_time", "query", false, "integer", List.of(), "csv")), Map.entry("search_source", new Param("search_source", "query", false, "string", List.of(), "csv")), Map.entry("search_id", new Param("search_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-translation-description", new Operation("tiktok-mobile-translation-description", "GET", "/tiktok/mobile/translation/description", Map.ofEntries(Map.entry("item_id", new Param("item_id", "query", true, "string", List.of(), "csv")), Map.entry("target_lang", new Param("target_lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-trending-categories", new Operation("tiktok-mobile-trending-categories", "GET", "/tiktok/mobile/trending/categories", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-trending-effects", new Operation("tiktok-mobile-trending-effects", "GET", "/tiktok/mobile/trending/effects", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-followers", new Operation("tiktok-mobile-user-followers", "GET", "/tiktok/mobile/user/followers", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-following", new Operation("tiktok-mobile-user-following", "GET", "/tiktok/mobile/user/following", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-original-effects", new Operation("tiktok-mobile-user-original-effects", "GET", "/tiktok/mobile/user/original-effects", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-original-music", new Operation("tiktok-mobile-user-original-music", "GET", "/tiktok/mobile/user/original-music", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-posts", new Operation("tiktok-mobile-user-posts", "GET", "/tiktok/mobile/user/posts", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv")), Map.entry("sec_user_id", new Param("sec_user_id", "query", false, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-profile", new Operation("tiktok-mobile-user-profile", "GET", "/tiktok/mobile/user/profile", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv")), Map.entry("sec_user_id", new Param("sec_user_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-user-recommendations", new Operation("tiktok-mobile-user-recommendations", "GET", "/tiktok/mobile/user/recommendations", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-video-detail", new Operation("tiktok-mobile-video-detail", "GET", "/tiktok/mobile/video/detail", Map.ofEntries(Map.entry("aweme_id", new Param("aweme_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-mobile-video-subtitles", new Operation("tiktok-mobile-video-subtitles", "GET", "/tiktok/mobile/video/subtitles", Map.ofEntries(Map.entry("video_id", new Param("video_id", "query", true, "string", List.of(), "csv")), Map.entry("language", new Param("language", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown TikTok Mobile operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object anchorList(Map<String, ?> params) { return request("tiktok-mobile-anchor-list", params); }
    public Object collectionDetail(Map<String, ?> params) { return request("tiktok-mobile-collection-detail", params); }
    public Object collectionList(Map<String, ?> params) { return request("tiktok-mobile-collection-list", params); }
    public Object collectionVideos(Map<String, ?> params) { return request("tiktok-mobile-collection-videos", params); }
    public Object commentReplies(Map<String, ?> params) { return request("tiktok-mobile-comment-replies", params); }
    public Object comments(Map<String, ?> params) { return request("tiktok-mobile-comments", params); }
    public Object feed(Map<String, ?> params) { return request("tiktok-mobile-feed", params); }
    public Object feedOffline(Map<String, ?> params) { return request("tiktok-mobile-feed-offline", params); }
    public Object feedPost(Map<String, ?> params) { return request("tiktok-mobile-feed-post", params); }
    public Object hashtag(Map<String, ?> params) { return request("tiktok-mobile-hashtag", params); }
    public Object hashtagPosts(Map<String, ?> params) { return request("tiktok-mobile-hashtag-posts", params); }
    public Object hashtags(Map<String, ?> params) { return request("tiktok-mobile-hashtags", params); }
    public Object liveEffects(Map<String, ?> params) { return request("tiktok-mobile-live-effects", params); }
    public Object liveGifts(Map<String, ?> params) { return request("tiktok-mobile-live-gifts", params); }
    public Object liveHashtags(Map<String, ?> params) { return request("tiktok-mobile-live-hashtags", params); }
    public Object liveRoom(Map<String, ?> params) { return request("tiktok-mobile-live-room", params); }
    public Object liveRoomByUser(Map<String, ?> params) { return request("tiktok-mobile-live-room-by-user", params); }
    public Object liveSearch(Map<String, ?> params) { return request("tiktok-mobile-live-search", params); }
    public Object liveTabs(Map<String, ?> params) { return request("tiktok-mobile-live-tabs", params); }
    public Object musicBeats(Map<String, ?> params) { return request("tiktok-mobile-music-beats", params); }
    public Object musicChart(Map<String, ?> params) { return request("tiktok-mobile-music-chart", params); }
    public Object musicChoices(Map<String, ?> params) { return request("tiktok-mobile-music-choices", params); }
    public Object musicCollectionList(Map<String, ?> params) { return request("tiktok-mobile-music-collection-list", params); }
    public Object musicCollections(Map<String, ?> params) { return request("tiktok-mobile-music-collections", params); }
    public Object musicDetail(Map<String, ?> params) { return request("tiktok-mobile-music-detail", params); }
    public Object musicPick(Map<String, ?> params) { return request("tiktok-mobile-music-pick", params); }
    public Object musicPosts(Map<String, ?> params) { return request("tiktok-mobile-music-posts", params); }
    public Object musicRelated(Map<String, ?> params) { return request("tiktok-mobile-music-related", params); }
    public Object musicTrending(Map<String, ?> params) { return request("tiktok-mobile-music-trending", params); }
    public Object mvVideos(Map<String, ?> params) { return request("tiktok-mobile-mv-videos", params); }
    public Object placeDetail(Map<String, ?> params) { return request("tiktok-mobile-place-detail", params); }
    public Object placeInfo(Map<String, ?> params) { return request("tiktok-mobile-place-info", params); }
    public Object placeMedia(Map<String, ?> params) { return request("tiktok-mobile-place-media", params); }
    public Object placePhotos(Map<String, ?> params) { return request("tiktok-mobile-place-photos", params); }
    public Object placeReviews(Map<String, ?> params) { return request("tiktok-mobile-place-reviews", params); }
    public Object placeVideos(Map<String, ?> params) { return request("tiktok-mobile-place-videos", params); }
    public Object playlistDetail(Map<String, ?> params) { return request("tiktok-mobile-playlist-detail", params); }
    public Object playlistList(Map<String, ?> params) { return request("tiktok-mobile-playlist-list", params); }
    public Object playlistVideos(Map<String, ?> params) { return request("tiktok-mobile-playlist-videos", params); }
    public Object search(Map<String, ?> params) { return request("tiktok-mobile-search", params); }
    public Object searchEffects(Map<String, ?> params) { return request("tiktok-mobile-search-effects", params); }
    public Object searchHashtags(Map<String, ?> params) { return request("tiktok-mobile-search-hashtags", params); }
    public Object searchMusic(Map<String, ?> params) { return request("tiktok-mobile-search-music", params); }
    public Object searchPhotos(Map<String, ?> params) { return request("tiktok-mobile-search-photos", params); }
    public Object searchPlace(Map<String, ?> params) { return request("tiktok-mobile-search-place", params); }
    public Object searchPreInfo(Map<String, ?> params) { return request("tiktok-mobile-search-pre-info", params); }
    public Object searchStream(Map<String, ?> params) { return request("tiktok-mobile-search-stream", params); }
    public Object searchSug(Map<String, ?> params) { return request("tiktok-mobile-search-sug", params); }
    public Object searchTabs(Map<String, ?> params) { return request("tiktok-mobile-search-tabs", params); }
    public Object searchUser(Map<String, ?> params) { return request("tiktok-mobile-search-user", params); }
    public Object searchVideos(Map<String, ?> params) { return request("tiktok-mobile-search-videos", params); }
    public Object translationDescription(Map<String, ?> params) { return request("tiktok-mobile-translation-description", params); }
    public Object trendingCategories(Map<String, ?> params) { return request("tiktok-mobile-trending-categories", params); }
    public Object trendingEffects(Map<String, ?> params) { return request("tiktok-mobile-trending-effects", params); }
    public Object userFollowers(Map<String, ?> params) { return request("tiktok-mobile-user-followers", params); }
    public Object userFollowing(Map<String, ?> params) { return request("tiktok-mobile-user-following", params); }
    public Object userOriginalEffects(Map<String, ?> params) { return request("tiktok-mobile-user-original-effects", params); }
    public Object userOriginalMusic(Map<String, ?> params) { return request("tiktok-mobile-user-original-music", params); }
    public Object userPosts(Map<String, ?> params) { return request("tiktok-mobile-user-posts", params); }
    public Object userProfile(Map<String, ?> params) { return request("tiktok-mobile-user-profile", params); }
    public Object userRecommendations(Map<String, ?> params) { return request("tiktok-mobile-user-recommendations", params); }
    public Object videoDetail(Map<String, ?> params) { return request("tiktok-mobile-video-detail", params); }
    public Object videoSubtitles(Map<String, ?> params) { return request("tiktok-mobile-video-subtitles", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
