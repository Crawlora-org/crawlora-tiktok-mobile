<?php

declare(strict_types=1);

namespace Crawlora\TiktokMobile;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'tiktok-mobile';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 63;
    public const OPERATION_IDS = ["tiktok-mobile-anchor-list", "tiktok-mobile-collection-detail", "tiktok-mobile-collection-list", "tiktok-mobile-collection-videos", "tiktok-mobile-comment-replies", "tiktok-mobile-comments", "tiktok-mobile-feed", "tiktok-mobile-feed-offline", "tiktok-mobile-feed-post", "tiktok-mobile-hashtag", "tiktok-mobile-hashtag-posts", "tiktok-mobile-hashtags", "tiktok-mobile-live-effects", "tiktok-mobile-live-gifts", "tiktok-mobile-live-hashtags", "tiktok-mobile-live-room", "tiktok-mobile-live-room-by-user", "tiktok-mobile-live-search", "tiktok-mobile-live-tabs", "tiktok-mobile-music-beats", "tiktok-mobile-music-chart", "tiktok-mobile-music-choices", "tiktok-mobile-music-collection-list", "tiktok-mobile-music-collections", "tiktok-mobile-music-detail", "tiktok-mobile-music-pick", "tiktok-mobile-music-posts", "tiktok-mobile-music-related", "tiktok-mobile-music-trending", "tiktok-mobile-mv-videos", "tiktok-mobile-place-detail", "tiktok-mobile-place-info", "tiktok-mobile-place-media", "tiktok-mobile-place-photos", "tiktok-mobile-place-reviews", "tiktok-mobile-place-videos", "tiktok-mobile-playlist-detail", "tiktok-mobile-playlist-list", "tiktok-mobile-playlist-videos", "tiktok-mobile-search", "tiktok-mobile-search-effects", "tiktok-mobile-search-hashtags", "tiktok-mobile-search-music", "tiktok-mobile-search-photos", "tiktok-mobile-search-place", "tiktok-mobile-search-pre-info", "tiktok-mobile-search-stream", "tiktok-mobile-search-sug", "tiktok-mobile-search-tabs", "tiktok-mobile-search-user", "tiktok-mobile-search-videos", "tiktok-mobile-translation-description", "tiktok-mobile-trending-categories", "tiktok-mobile-trending-effects", "tiktok-mobile-user-followers", "tiktok-mobile-user-following", "tiktok-mobile-user-original-effects", "tiktok-mobile-user-original-music", "tiktok-mobile-user-posts", "tiktok-mobile-user-profile", "tiktok-mobile-user-recommendations", "tiktok-mobile-video-detail", "tiktok-mobile-video-subtitles"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"tiktok-mobile-anchor-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-anchor-list", "method": "GET", "params": [], "path": "/tiktok/mobile/anchor/list", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-collection-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-collection-detail", "method": "GET", "params": [{"description": "Collection id (`item_archive_id` from the collection list)", "in": "query", "name": "collection_id", "required": true, "type": "string", "x-example": "7394627756635573022"}], "path": "/tiktok/mobile/collection/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "collection_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-collection-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-collection-list", "method": "GET", "params": [{"description": "Creator's numeric user id", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "107955"}, {"default": 0, "description": "Pagination cursor (server token)", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Collections per page (max 30)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/collection/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-collection-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-collection-videos", "method": "GET", "params": [{"description": "Collection id (`item_archive_id` from the collection list)", "in": "query", "name": "collection_id", "required": true, "type": "string", "x-example": "7394627756635573022"}, {"default": 0, "description": "Paging cursor; use the previous page's max_cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Videos per page (max 30; the server serves about 30)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/collection/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "collection_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-comment-replies": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-comment-replies", "method": "GET", "params": [{"description": "Video id the comment belongs to", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7680168962218511636"}, {"description": "Comment id to list replies for", "in": "query", "name": "comment_id", "required": true, "type": "string", "x-example": "7680523330713240340"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Replies per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/comment/replies", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "comment_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-comments": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-comments", "method": "GET", "params": [{"description": "Video id to list comments for", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7681236055831416084"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Comments per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-feed": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-feed", "method": "GET", "params": [{"default": 0, "description": "Videos to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/feed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-feed-offline": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-feed-offline", "method": "GET", "params": [{"description": "Pull type forwarded to the app route (measured 0 and 11; default 11)", "in": "query", "name": "pull_type", "type": "integer", "x-example": 11}, {"description": "Page size, bounded at 50 (upstream default when omitted)", "in": "query", "name": "count", "type": "integer", "x-example": 10}], "path": "/tiktok/mobile/feed/offline", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "pull_type", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-feed-post": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-feed-post", "method": "GET", "params": [], "path": "/tiktok/mobile/feed/post", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtag": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtag", "method": "GET", "params": [{"description": "Hashtag name without the leading #", "in": "query", "name": "name", "required": true, "type": "string", "x-example": "readingvlog"}], "path": "/tiktok/mobile/hashtag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtag-posts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtag-posts", "method": "GET", "params": [{"description": "Hashtag name without the leading #", "in": "query", "name": "name", "required": true, "type": "string", "x-example": "readingvlog"}, {"default": "fresh", "description": "Listing: fresh (newest) or popular (hot)", "enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"default": 20, "description": "Videos per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/hashtag/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "required": true, "type": "string"}, {"enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtags": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtags", "method": "GET", "params": [{"description": "Keyword to search hashtags for", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "reading"}, {"default": 20, "description": "Results per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-effects", "method": "GET", "params": [], "path": "/tiktok/mobile/live/effects", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-gifts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-gifts", "method": "GET", "params": [], "path": "/tiktok/mobile/live/gifts", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-hashtags": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-hashtags", "method": "GET", "params": [], "path": "/tiktok/mobile/live/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-room": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-room", "method": "GET", "params": [{"description": "Numeric LIVE room id from /api/v1/tiktok/mobile/live/search (data[].lives.author.room_id)", "in": "query", "name": "room_id", "required": true, "type": "string", "x-example": "7699174209096059678"}], "path": "/tiktok/mobile/live/room", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "room_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-room-by-user": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-room-by-user", "method": "GET", "params": [{"description": "Numeric TikTok user id (e.g. the owner id from a profile, video author or live search row)", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "6707748031095751686"}], "path": "/tiktok/mobile/live/room-by-user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-search": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 0, "description": "Results to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/live/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-tabs": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-tabs", "method": "GET", "params": [], "path": "/tiktok/mobile/live/tabs", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-beats": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-beats", "method": "GET", "params": [{"default": 0, "description": "Accepted for compatibility; not measured to change the page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/music/beats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-chart": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-chart", "method": "GET", "params": [{"description": "Region of the chart: AE, BR, CA, DE, EG, FR, JP, KR, LB, MX, NG, SA, TR, US or ZA; omit for the default chart (same as US)", "enum": ["AE", "BR", "CA", "DE", "EG", "FR", "JP", "KR", "LB", "MX", "NG", "SA", "TR", "US", "ZA"], "in": "query", "name": "chart_region", "type": "string", "x-example": "US"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Rows per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/music/chart", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["AE", "BR", "CA", "DE", "EG", "FR", "JP", "KR", "LB", "MX", "NG", "SA", "TR", "US", "ZA"], "in": "query", "name": "chart_region", "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-choices": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-choices", "method": "GET", "params": [], "path": "/tiktok/mobile/music/choices", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-collection-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-collection-list", "method": "GET", "params": [{"description": "Page size: honoured (1-50 measured, capped by the collection set)", "in": "query", "name": "count", "type": "integer", "x-example": 5}, {"description": "Next-page token from the previous response (0 = first page)", "in": "query", "name": "cursor", "type": "integer", "x-example": 5}], "path": "/tiktok/mobile/music/collection-list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-collections": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-collections", "method": "GET", "params": [{"default": 0, "description": "Collections to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Accepted for shape compatibility only; not a verified page token", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-detail", "method": "GET", "params": [{"description": "Sound id", "in": "query", "name": "music_id", "required": true, "type": "string", "x-example": "7329791746055080709"}], "path": "/tiktok/mobile/music/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "music_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-pick": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-pick", "method": "GET", "params": [{"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/pick", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-posts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-posts", "method": "GET", "params": [{"description": "Sound (music) id", "in": "query", "name": "music_id", "required": true, "type": "string", "x-example": "6799585653702019073"}, {"default": "fresh", "description": "Listing: fresh (newest, default) or popular (app canonical music.posts list; requires the device-backed signer)", "enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"default": 0, "description": "Accepted for compatibility; the server ignores it (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "music_id", "required": true, "type": "string"}, {"enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-related": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-related", "method": "GET", "params": [{"description": "Video id to find related sounds for", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7681236055831416084"}, {"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/related", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-trending": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-trending", "method": "GET", "params": [{"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-mv-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-mv-videos", "method": "GET", "params": [{"description": "MV channel index (small integer; measured 0-10 populated, 100 empty)", "in": "query", "name": "mv_id", "required": true, "type": "string", "x-example": "1"}, {"description": "Next-page token from the previous response (0 = first page)", "in": "query", "name": "cursor", "type": "integer", "x-example": 0}], "path": "/tiktok/mobile/mv/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "mv_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-detail", "method": "GET", "params": [{"description": "Place id from the place search endpoint", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}, {"description": "Review preview size forwarded upstream (default 20, bounded at 50)", "in": "query", "name": "review_count", "type": "integer", "x-example": 20}, {"description": "Review cursor forwarded upstream (default 0)", "in": "query", "name": "review_cursor", "type": "integer", "x-example": 0}, {"description": "Posts page size forwarded upstream (default 9, bounded at 50)", "in": "query", "name": "merged_count", "type": "integer", "x-example": 9}, {"description": "Top-videos cursor forwarded upstream (default 0)", "in": "query", "name": "video_cursor", "type": "integer", "x-example": 0}, {"description": "Forwarded analytics origin (default search_places)", "in": "query", "name": "enter_from", "type": "string", "x-example": "search_places"}], "path": "/tiktok/mobile/place/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}, {"in": "query", "name": "review_count", "type": "integer"}, {"in": "query", "name": "review_cursor", "type": "integer"}, {"in": "query", "name": "merged_count", "type": "integer"}, {"in": "query", "name": "video_cursor", "type": "integer"}, {"in": "query", "name": "enter_from", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-info": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-info", "method": "GET", "params": [{"description": "Place id from the place search endpoint", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}], "path": "/tiktok/mobile/place/info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-media": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-media", "method": "GET", "params": [{"description": "Place id from the place search/detail endpoints", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}, {"description": "Opaque next_cursor token from the previous response", "in": "query", "name": "cursor", "type": "string"}, {"default": 6, "description": "Rows per page hint (max 30)", "in": "query", "name": "size", "type": "integer"}, {"description": "Paging data version carried with cursor (defaults to v1)", "in": "query", "name": "data_version", "type": "string", "x-example": "v1"}], "path": "/tiktok/mobile/place/media", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}, {"in": "query", "name": "size", "type": "integer"}, {"in": "query", "name": "data_version", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-photos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-photos", "method": "GET", "params": [{"description": "Place id from the place search endpoint", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}], "path": "/tiktok/mobile/place/photos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-reviews": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-reviews", "method": "GET", "params": [{"description": "Place id from the place search/detail endpoints", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Reviews per page (max 30)", "in": "query", "name": "count", "type": "integer"}, {"default": 1, "description": "Sort order: 1 = default, 2 = recent", "enum": [1, 2], "in": "query", "name": "sort_type", "type": "integer"}], "path": "/tiktok/mobile/place/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"enum": ["1", "2"], "in": "query", "name": "sort_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-place-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-place-videos", "method": "GET", "params": [{"description": "Place id from the place search endpoint", "in": "query", "name": "poi_id", "required": true, "type": "string", "x-example": "42203861086875992"}, {"description": "Page-size hint: 1-50 measured, server caps larger pages (default is the app default)", "in": "query", "name": "count", "type": "integer", "x-example": 10}, {"description": "Next-page token from the previous response (0 = first page)", "in": "query", "name": "cursor", "type": "integer", "x-example": 0}], "path": "/tiktok/mobile/place/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "poi_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-playlist-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-playlist-detail", "method": "GET", "params": [{"description": "Playlist id (web playlist id namespace)", "in": "query", "name": "mix_id", "required": true, "type": "string", "x-example": "7681171537575824159"}, {"description": "Playlist owner's numeric user id (one of user_id / sec_user_id is required)", "in": "query", "name": "user_id", "type": "string", "x-example": "107955"}, {"description": "Playlist owner's sec_user_id (one of user_id / sec_user_id is required)", "in": "query", "name": "sec_user_id", "type": "string"}], "path": "/tiktok/mobile/playlist/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "mix_id", "required": true, "type": "string"}, {"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "sec_user_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-playlist-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-playlist-list", "method": "GET", "params": [{"description": "Creator's numeric user id (one of user_id / sec_user_id is required)", "in": "query", "name": "user_id", "type": "string", "x-example": "107955"}, {"description": "Creator's sec_user_id (one of user_id / sec_user_id is required)", "in": "query", "name": "sec_user_id", "type": "string"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/playlist/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "sec_user_id", "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-playlist-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-playlist-videos", "method": "GET", "params": [{"description": "Playlist id (web playlist id namespace)", "in": "query", "name": "mix_id", "required": true, "type": "string", "x-example": "7681171537575824159"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Videos per page (max 30)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/playlist/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "mix_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 5, "description": "Results per page (max 20)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Result offset; pass search_id with a non-zero offset", "in": "query", "name": "offset", "type": "integer"}, {"description": "search_id returned by a previous page of the same search", "in": "query", "name": "search_id", "type": "string"}], "path": "/tiktok/mobile/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "search_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-effects", "method": "GET", "params": [{"description": "Effect name or text, e.g. green screen", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "green screen"}, {"description": "Accepted for shape parity; the server was measured to ignore it", "in": "query", "name": "count", "type": "integer", "x-example": 20}, {"description": "Next-page token from the previous response (0 = first page)", "in": "query", "name": "cursor", "type": "integer", "x-example": 100}, {"description": "Search-session token from the previous response; required together with cursor", "in": "query", "name": "search_id", "type": "string", "x-example": "20261021173221C8185FF1D4A1062AD97C"}], "path": "/tiktok/mobile/search/effects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "search_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-hashtags": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-hashtags", "method": "GET", "params": [{"description": "Text typed so far; the server also accepts prefixes (e.g. lofi -> lofihiphop)", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"description": "Accepted for shape parity; the server was measured to ignore it (always up to 10 rows)", "in": "query", "name": "count", "type": "integer", "x-example": 10}], "path": "/tiktok/mobile/search/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-music": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-music", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/tiktok/mobile/search/music", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-photos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-photos", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"description": "Rows per page, bounded at 50 (default 10)", "in": "query", "name": "count", "type": "integer", "x-example": 10}, {"description": "Row offset forwarded to the app route (first page only in guest mode)", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Sort: 0 relevance, 1 like count, 3 date posted", "in": "query", "name": "sort_type", "type": "integer", "x-example": 0}, {"description": "Recency window in days: 0 all, 1, 7, 30, 90, 180", "in": "query", "name": "publish_time", "type": "integer", "x-example": 0}, {"description": "Forwarded search source (default tab_search)", "in": "query", "name": "search_source", "type": "string", "x-example": "tab_search"}], "path": "/tiktok/mobile/search/photos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "sort_type", "type": "integer"}, {"in": "query", "name": "publish_time", "type": "integer"}, {"in": "query", "name": "search_source", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-place": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-place", "method": "GET", "params": [{"description": "Place name or category to search for", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "pizza"}, {"default": 10, "description": "Rows to return, 1-30 measured (a larger count yields an empty upstream page and is rejected)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/place", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-pre-info": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-pre-info", "method": "GET", "params": [{"description": "Seed keyword (optional; the app also requests this with an empty keyword)", "in": "query", "name": "keyword", "type": "string", "x-example": "lofi"}, {"default": 20, "description": "Suggestion count (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/pre-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-stream": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-stream", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 10, "description": "Requested page size (sanity bound: 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Row offset", "in": "query", "name": "offset", "type": "integer"}, {"description": "Search source hint forwarded to upstream (measured: video)", "in": "query", "name": "search_source", "type": "string", "x-example": "video"}, {"default": 0, "description": "Sort order: 0 relevance, 1 like count (stable ordering measured), 3 date posted", "enum": [0, 1, 3], "in": "query", "name": "sort_type", "type": "integer"}, {"default": 0, "description": "Recency window in days (0 = unlimited; 7 measured)", "in": "query", "name": "publish_time", "type": "integer"}, {"description": "Raw app filter blob as JSON; takes precedence over sort_type/publish_time", "in": "query", "name": "filter_selected", "type": "string", "x-example": "{\"sort_type\":\"1\",\"publish_time\":\"7\"}"}], "path": "/tiktok/mobile/search/stream", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "search_source", "type": "string"}, {"enum": ["0", "1", "3"], "in": "query", "name": "sort_type", "type": "integer"}, {"in": "query", "name": "publish_time", "type": "integer"}, {"in": "query", "name": "filter_selected", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-sug": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-sug", "method": "GET", "params": [{"description": "Seed keyword to expand", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 10, "description": "Suggestions to return (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/sug", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-tabs": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-tabs", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}], "path": "/tiktok/mobile/search/tabs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-user": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-user", "method": "GET", "params": [{"description": "Search keyword (a username or display name)", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "mrbeast"}, {"default": 20, "description": "Users per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/search/user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-videos", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 10, "description": "Rows per page (sanity bound: 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Row offset; pass search_id with a non-zero offset", "in": "query", "name": "offset", "type": "integer"}, {"default": 0, "description": "Sort order: 0 relevance, 1 like count, 3 date posted", "enum": [0, 1, 3], "in": "query", "name": "sort_type", "type": "integer"}, {"default": 0, "description": "Date-posted window in days (0 to 365; the app uses 0, 1, 7, 30, 90, 180)", "in": "query", "name": "publish_time", "type": "integer"}, {"default": "tab_search", "description": "Search source forwarded as the app sends it", "in": "query", "name": "search_source", "type": "string"}, {"description": "search_id returned by a previous page of the same search", "in": "query", "name": "search_id", "type": "string"}], "path": "/tiktok/mobile/search/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"enum": ["0", "1", "3"], "in": "query", "name": "sort_type", "type": "integer"}, {"in": "query", "name": "publish_time", "type": "integer"}, {"in": "query", "name": "search_source", "type": "string"}, {"in": "query", "name": "search_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-translation-description": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-translation-description", "method": "GET", "params": [{"description": "Video id to translate", "in": "query", "name": "item_id", "required": true, "type": "string", "x-example": "7650052642089225493"}, {"description": "Target language code (default en)", "in": "query", "name": "target_lang", "type": "string", "x-example": "en"}], "path": "/tiktok/mobile/translation/description", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "item_id", "required": true, "type": "string"}, {"in": "query", "name": "target_lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-trending-categories": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-trending-categories", "method": "GET", "params": [{"default": 20, "description": "Categories per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/trending/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-trending-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-trending-effects", "method": "GET", "params": [{"default": 20, "description": "Videos per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/trending/effects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-followers": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-followers", "method": "GET", "params": [{"description": "Creator user id", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "7141011492116005914"}, {"description": "Followers per page (sanity bound: 50; omitted = app default, not measured)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Page token: the max_time returned by the previous page (omitted at 0 = first page)", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/user/followers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-following": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-following", "method": "GET", "params": [{"description": "Creator's numeric user id", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "7343380121988285482"}, {"default": 20, "description": "Rows per page (sanity bound: 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Page token: max_time returned by the previous page (omitted at 0)", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/user/following", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-original-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-original-effects", "method": "GET", "params": [{"description": "Creator's numeric uid", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "107955"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Effects per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/user/original-effects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-original-music": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-original-music", "method": "GET", "params": [{"description": "Creator's numeric uid", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "107955"}, {"default": 0, "description": "Paging token from the previous response", "in": "query", "name": "cursor", "type": "integer"}, {"default": 10, "description": "Groups per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/user/original-music", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-posts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-posts", "method": "GET", "params": [{"description": "Creator user id; one of user_id or sec_user_id is required (user_id wins if both are sent)", "in": "query", "name": "user_id", "type": "string", "x-example": "7141011492116005914"}, {"description": "Creator sec_user_id; one of user_id or sec_user_id is required", "in": "query", "name": "sec_user_id", "type": "string"}, {"default": 9, "description": "Videos per page (sanity bound: 50; omitted = app default, measured 9)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Page token: the max_cursor returned by the previous page (omitted at 0 = first page)", "in": "query", "name": "cursor", "type": "integer"}, {"default": 0, "description": "Sort type (0 = the app default; always sent, non-zero values are forwarded as given)", "in": "query", "name": "sort_type", "type": "integer"}], "path": "/tiktok/mobile/user/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "sec_user_id", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "sort_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-profile": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-profile", "method": "GET", "params": [{"description": "Creator user id", "in": "query", "name": "user_id", "type": "string", "x-example": "7141011492116005914"}, {"description": "Creator sec_user_id (alternate identifier; use instead of user_id)", "in": "query", "name": "sec_user_id", "type": "string", "x-example": "MS4wLjABAAAAexample"}], "path": "/tiktok/mobile/user/profile", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "sec_user_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-user-recommendations": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-user-recommendations", "method": "GET", "params": [{"description": "Requested page size; forwarded when set, but the gateway was measured to ignore it", "in": "query", "name": "count", "type": "integer", "x-example": 10}], "path": "/tiktok/mobile/user/recommendations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-video-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-video-detail", "method": "GET", "params": [{"description": "Video id", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7329791719535283462"}], "path": "/tiktok/mobile/video/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-video-subtitles": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-video-subtitles", "method": "GET", "params": [{"description": "Numeric id of the video (aweme id)", "in": "query", "name": "video_id", "required": true, "type": "string", "x-example": "7696141388324293918"}, {"description": "Target language code: ar, de, en, es, fr, hi, id, it, ja, ko, pt, ru, th, tr, vi, zh", "in": "query", "name": "language", "required": true, "type": "string", "x-example": "en"}], "path": "/tiktok/mobile/video/subtitles", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "video_id", "required": true, "type": "string"}, {"in": "query", "name": "language", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-tiktok-mobile-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function anchor_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-anchor-list", $params, $responseType);
    }
    public function collection_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-collection-detail", $params, $responseType);
    }
    public function collection_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-collection-list", $params, $responseType);
    }
    public function collection_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-collection-videos", $params, $responseType);
    }
    public function comment_replies(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-comment-replies", $params, $responseType);
    }
    public function comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-comments", $params, $responseType);
    }
    public function feed(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-feed", $params, $responseType);
    }
    public function feed_offline(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-feed-offline", $params, $responseType);
    }
    public function feed_post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-feed-post", $params, $responseType);
    }
    public function hashtag(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtag", $params, $responseType);
    }
    public function hashtag_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtag-posts", $params, $responseType);
    }
    public function hashtags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtags", $params, $responseType);
    }
    public function live_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-effects", $params, $responseType);
    }
    public function live_gifts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-gifts", $params, $responseType);
    }
    public function live_hashtags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-hashtags", $params, $responseType);
    }
    public function live_room(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-room", $params, $responseType);
    }
    public function live_room_by_user(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-room-by-user", $params, $responseType);
    }
    public function live_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-search", $params, $responseType);
    }
    public function live_tabs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-tabs", $params, $responseType);
    }
    public function music_beats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-beats", $params, $responseType);
    }
    public function music_chart(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-chart", $params, $responseType);
    }
    public function music_choices(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-choices", $params, $responseType);
    }
    public function music_collection_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-collection-list", $params, $responseType);
    }
    public function music_collections(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-collections", $params, $responseType);
    }
    public function music_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-detail", $params, $responseType);
    }
    public function music_pick(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-pick", $params, $responseType);
    }
    public function music_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-posts", $params, $responseType);
    }
    public function music_related(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-related", $params, $responseType);
    }
    public function music_trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-trending", $params, $responseType);
    }
    public function mv_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-mv-videos", $params, $responseType);
    }
    public function place_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-detail", $params, $responseType);
    }
    public function place_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-info", $params, $responseType);
    }
    public function place_media(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-media", $params, $responseType);
    }
    public function place_photos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-photos", $params, $responseType);
    }
    public function place_reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-reviews", $params, $responseType);
    }
    public function place_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-place-videos", $params, $responseType);
    }
    public function playlist_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-playlist-detail", $params, $responseType);
    }
    public function playlist_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-playlist-list", $params, $responseType);
    }
    public function playlist_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-playlist-videos", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search", $params, $responseType);
    }
    public function search_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-effects", $params, $responseType);
    }
    public function search_hashtags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-hashtags", $params, $responseType);
    }
    public function search_music(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-music", $params, $responseType);
    }
    public function search_photos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-photos", $params, $responseType);
    }
    public function search_place(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-place", $params, $responseType);
    }
    public function search_pre_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-pre-info", $params, $responseType);
    }
    public function search_stream(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-stream", $params, $responseType);
    }
    public function search_sug(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-sug", $params, $responseType);
    }
    public function search_tabs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-tabs", $params, $responseType);
    }
    public function search_user(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-user", $params, $responseType);
    }
    public function search_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-videos", $params, $responseType);
    }
    public function translation_description(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-translation-description", $params, $responseType);
    }
    public function trending_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-trending-categories", $params, $responseType);
    }
    public function trending_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-trending-effects", $params, $responseType);
    }
    public function user_followers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-followers", $params, $responseType);
    }
    public function user_following(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-following", $params, $responseType);
    }
    public function user_original_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-original-effects", $params, $responseType);
    }
    public function user_original_music(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-original-music", $params, $responseType);
    }
    public function user_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-posts", $params, $responseType);
    }
    public function user_profile(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-profile", $params, $responseType);
    }
    public function user_recommendations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-user-recommendations", $params, $responseType);
    }
    public function video_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-video-detail", $params, $responseType);
    }
    public function video_subtitles(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-video-subtitles", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
