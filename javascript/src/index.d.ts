import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class TikTokMobileClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  anchorList(params?: OperationParamsMap["tiktok-mobile-anchor-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collectionDetail(params: OperationParamsMap["tiktok-mobile-collection-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collectionList(params: OperationParamsMap["tiktok-mobile-collection-list"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collectionVideos(params: OperationParamsMap["tiktok-mobile-collection-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  commentReplies(params: OperationParamsMap["tiktok-mobile-comment-replies"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  comments(params: OperationParamsMap["tiktok-mobile-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  feed(params?: OperationParamsMap["tiktok-mobile-feed"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  feedOffline(params?: OperationParamsMap["tiktok-mobile-feed-offline"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  feedPost(params?: OperationParamsMap["tiktok-mobile-feed-post"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hashtag(params: OperationParamsMap["tiktok-mobile-hashtag"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hashtagPosts(params: OperationParamsMap["tiktok-mobile-hashtag-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hashtags(params: OperationParamsMap["tiktok-mobile-hashtags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveEffects(params?: OperationParamsMap["tiktok-mobile-live-effects"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveGifts(params?: OperationParamsMap["tiktok-mobile-live-gifts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveHashtags(params?: OperationParamsMap["tiktok-mobile-live-hashtags"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveRoom(params: OperationParamsMap["tiktok-mobile-live-room"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveRoomByUser(params: OperationParamsMap["tiktok-mobile-live-room-by-user"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveSearch(params: OperationParamsMap["tiktok-mobile-live-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveTabs(params?: OperationParamsMap["tiktok-mobile-live-tabs"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicBeats(params?: OperationParamsMap["tiktok-mobile-music-beats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicChart(params?: OperationParamsMap["tiktok-mobile-music-chart"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicChoices(params?: OperationParamsMap["tiktok-mobile-music-choices"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicCollectionList(params?: OperationParamsMap["tiktok-mobile-music-collection-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicCollections(params?: OperationParamsMap["tiktok-mobile-music-collections"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicDetail(params: OperationParamsMap["tiktok-mobile-music-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicPick(params?: OperationParamsMap["tiktok-mobile-music-pick"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicPosts(params: OperationParamsMap["tiktok-mobile-music-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicRelated(params: OperationParamsMap["tiktok-mobile-music-related"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  musicTrending(params?: OperationParamsMap["tiktok-mobile-music-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mvVideos(params: OperationParamsMap["tiktok-mobile-mv-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placeDetail(params: OperationParamsMap["tiktok-mobile-place-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placeInfo(params: OperationParamsMap["tiktok-mobile-place-info"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placeMedia(params: OperationParamsMap["tiktok-mobile-place-media"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placePhotos(params: OperationParamsMap["tiktok-mobile-place-photos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placeReviews(params: OperationParamsMap["tiktok-mobile-place-reviews"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  placeVideos(params: OperationParamsMap["tiktok-mobile-place-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playlistDetail(params: OperationParamsMap["tiktok-mobile-playlist-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playlistList(params?: OperationParamsMap["tiktok-mobile-playlist-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playlistVideos(params: OperationParamsMap["tiktok-mobile-playlist-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["tiktok-mobile-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchEffects(params: OperationParamsMap["tiktok-mobile-search-effects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchHashtags(params: OperationParamsMap["tiktok-mobile-search-hashtags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchMusic(params: OperationParamsMap["tiktok-mobile-search-music"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchPhotos(params: OperationParamsMap["tiktok-mobile-search-photos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchPlace(params: OperationParamsMap["tiktok-mobile-search-place"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchPreInfo(params?: OperationParamsMap["tiktok-mobile-search-pre-info"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchStream(params: OperationParamsMap["tiktok-mobile-search-stream"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchSug(params: OperationParamsMap["tiktok-mobile-search-sug"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchTabs(params: OperationParamsMap["tiktok-mobile-search-tabs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchUser(params: OperationParamsMap["tiktok-mobile-search-user"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchVideos(params: OperationParamsMap["tiktok-mobile-search-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  translationDescription(params: OperationParamsMap["tiktok-mobile-translation-description"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendingCategories(params?: OperationParamsMap["tiktok-mobile-trending-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendingEffects(params?: OperationParamsMap["tiktok-mobile-trending-effects"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userFollowers(params: OperationParamsMap["tiktok-mobile-user-followers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userFollowing(params: OperationParamsMap["tiktok-mobile-user-following"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userOriginalEffects(params: OperationParamsMap["tiktok-mobile-user-original-effects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userOriginalMusic(params: OperationParamsMap["tiktok-mobile-user-original-music"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userPosts(params?: OperationParamsMap["tiktok-mobile-user-posts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userProfile(params?: OperationParamsMap["tiktok-mobile-user-profile"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userRecommendations(params?: OperationParamsMap["tiktok-mobile-user-recommendations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videoDetail(params: OperationParamsMap["tiktok-mobile-video-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videoSubtitles(params: OperationParamsMap["tiktok-mobile-video-subtitles"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  anchorList(params?: OperationParamsMap["tiktok-mobile-anchor-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collectionDetail(params: OperationParamsMap["tiktok-mobile-collection-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collectionList(params: OperationParamsMap["tiktok-mobile-collection-list"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collectionVideos(params: OperationParamsMap["tiktok-mobile-collection-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  commentReplies(params: OperationParamsMap["tiktok-mobile-comment-replies"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  comments(params: OperationParamsMap["tiktok-mobile-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  feed(params?: OperationParamsMap["tiktok-mobile-feed"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  feedOffline(params?: OperationParamsMap["tiktok-mobile-feed-offline"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  feedPost(params?: OperationParamsMap["tiktok-mobile-feed-post"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hashtag(params: OperationParamsMap["tiktok-mobile-hashtag"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hashtagPosts(params: OperationParamsMap["tiktok-mobile-hashtag-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hashtags(params: OperationParamsMap["tiktok-mobile-hashtags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveEffects(params?: OperationParamsMap["tiktok-mobile-live-effects"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveGifts(params?: OperationParamsMap["tiktok-mobile-live-gifts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveHashtags(params?: OperationParamsMap["tiktok-mobile-live-hashtags"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveRoom(params: OperationParamsMap["tiktok-mobile-live-room"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveRoomByUser(params: OperationParamsMap["tiktok-mobile-live-room-by-user"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveSearch(params: OperationParamsMap["tiktok-mobile-live-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveTabs(params?: OperationParamsMap["tiktok-mobile-live-tabs"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicBeats(params?: OperationParamsMap["tiktok-mobile-music-beats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicChart(params?: OperationParamsMap["tiktok-mobile-music-chart"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicChoices(params?: OperationParamsMap["tiktok-mobile-music-choices"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicCollectionList(params?: OperationParamsMap["tiktok-mobile-music-collection-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicCollections(params?: OperationParamsMap["tiktok-mobile-music-collections"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicDetail(params: OperationParamsMap["tiktok-mobile-music-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicPick(params?: OperationParamsMap["tiktok-mobile-music-pick"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicPosts(params: OperationParamsMap["tiktok-mobile-music-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicRelated(params: OperationParamsMap["tiktok-mobile-music-related"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  musicTrending(params?: OperationParamsMap["tiktok-mobile-music-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mvVideos(params: OperationParamsMap["tiktok-mobile-mv-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placeDetail(params: OperationParamsMap["tiktok-mobile-place-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placeInfo(params: OperationParamsMap["tiktok-mobile-place-info"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placeMedia(params: OperationParamsMap["tiktok-mobile-place-media"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placePhotos(params: OperationParamsMap["tiktok-mobile-place-photos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placeReviews(params: OperationParamsMap["tiktok-mobile-place-reviews"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  placeVideos(params: OperationParamsMap["tiktok-mobile-place-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playlistDetail(params: OperationParamsMap["tiktok-mobile-playlist-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playlistList(params?: OperationParamsMap["tiktok-mobile-playlist-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playlistVideos(params: OperationParamsMap["tiktok-mobile-playlist-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["tiktok-mobile-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchEffects(params: OperationParamsMap["tiktok-mobile-search-effects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchHashtags(params: OperationParamsMap["tiktok-mobile-search-hashtags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchMusic(params: OperationParamsMap["tiktok-mobile-search-music"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchPhotos(params: OperationParamsMap["tiktok-mobile-search-photos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchPlace(params: OperationParamsMap["tiktok-mobile-search-place"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchPreInfo(params?: OperationParamsMap["tiktok-mobile-search-pre-info"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchStream(params: OperationParamsMap["tiktok-mobile-search-stream"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchSug(params: OperationParamsMap["tiktok-mobile-search-sug"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchTabs(params: OperationParamsMap["tiktok-mobile-search-tabs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchUser(params: OperationParamsMap["tiktok-mobile-search-user"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchVideos(params: OperationParamsMap["tiktok-mobile-search-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  translationDescription(params: OperationParamsMap["tiktok-mobile-translation-description"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendingCategories(params?: OperationParamsMap["tiktok-mobile-trending-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendingEffects(params?: OperationParamsMap["tiktok-mobile-trending-effects"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userFollowers(params: OperationParamsMap["tiktok-mobile-user-followers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userFollowing(params: OperationParamsMap["tiktok-mobile-user-following"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userOriginalEffects(params: OperationParamsMap["tiktok-mobile-user-original-effects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userOriginalMusic(params: OperationParamsMap["tiktok-mobile-user-original-music"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userPosts(params?: OperationParamsMap["tiktok-mobile-user-posts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userProfile(params?: OperationParamsMap["tiktok-mobile-user-profile"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userRecommendations(params?: OperationParamsMap["tiktok-mobile-user-recommendations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videoDetail(params: OperationParamsMap["tiktok-mobile-video-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videoSubtitles(params: OperationParamsMap["tiktok-mobile-video-subtitles"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  anchorList(...args: OperationRequestArgs<"tiktok-mobile-anchor-list">): Promise<OperationResponseMap["tiktok-mobile-anchor-list"]>;
  collectionDetail(...args: OperationRequestArgs<"tiktok-mobile-collection-detail">): Promise<OperationResponseMap["tiktok-mobile-collection-detail"]>;
  collectionList(...args: OperationRequestArgs<"tiktok-mobile-collection-list">): Promise<OperationResponseMap["tiktok-mobile-collection-list"]>;
  collectionVideos(...args: OperationRequestArgs<"tiktok-mobile-collection-videos">): Promise<OperationResponseMap["tiktok-mobile-collection-videos"]>;
  commentReplies(...args: OperationRequestArgs<"tiktok-mobile-comment-replies">): Promise<OperationResponseMap["tiktok-mobile-comment-replies"]>;
  comments(...args: OperationRequestArgs<"tiktok-mobile-comments">): Promise<OperationResponseMap["tiktok-mobile-comments"]>;
  feed(...args: OperationRequestArgs<"tiktok-mobile-feed">): Promise<OperationResponseMap["tiktok-mobile-feed"]>;
  feedOffline(...args: OperationRequestArgs<"tiktok-mobile-feed-offline">): Promise<OperationResponseMap["tiktok-mobile-feed-offline"]>;
  feedPost(...args: OperationRequestArgs<"tiktok-mobile-feed-post">): Promise<OperationResponseMap["tiktok-mobile-feed-post"]>;
  hashtag(...args: OperationRequestArgs<"tiktok-mobile-hashtag">): Promise<OperationResponseMap["tiktok-mobile-hashtag"]>;
  hashtagPosts(...args: OperationRequestArgs<"tiktok-mobile-hashtag-posts">): Promise<OperationResponseMap["tiktok-mobile-hashtag-posts"]>;
  hashtags(...args: OperationRequestArgs<"tiktok-mobile-hashtags">): Promise<OperationResponseMap["tiktok-mobile-hashtags"]>;
  liveEffects(...args: OperationRequestArgs<"tiktok-mobile-live-effects">): Promise<OperationResponseMap["tiktok-mobile-live-effects"]>;
  liveGifts(...args: OperationRequestArgs<"tiktok-mobile-live-gifts">): Promise<OperationResponseMap["tiktok-mobile-live-gifts"]>;
  liveHashtags(...args: OperationRequestArgs<"tiktok-mobile-live-hashtags">): Promise<OperationResponseMap["tiktok-mobile-live-hashtags"]>;
  liveRoom(...args: OperationRequestArgs<"tiktok-mobile-live-room">): Promise<OperationResponseMap["tiktok-mobile-live-room"]>;
  liveRoomByUser(...args: OperationRequestArgs<"tiktok-mobile-live-room-by-user">): Promise<OperationResponseMap["tiktok-mobile-live-room-by-user"]>;
  liveSearch(...args: OperationRequestArgs<"tiktok-mobile-live-search">): Promise<OperationResponseMap["tiktok-mobile-live-search"]>;
  liveTabs(...args: OperationRequestArgs<"tiktok-mobile-live-tabs">): Promise<OperationResponseMap["tiktok-mobile-live-tabs"]>;
  musicBeats(...args: OperationRequestArgs<"tiktok-mobile-music-beats">): Promise<OperationResponseMap["tiktok-mobile-music-beats"]>;
  musicChart(...args: OperationRequestArgs<"tiktok-mobile-music-chart">): Promise<OperationResponseMap["tiktok-mobile-music-chart"]>;
  musicChoices(...args: OperationRequestArgs<"tiktok-mobile-music-choices">): Promise<OperationResponseMap["tiktok-mobile-music-choices"]>;
  musicCollectionList(...args: OperationRequestArgs<"tiktok-mobile-music-collection-list">): Promise<OperationResponseMap["tiktok-mobile-music-collection-list"]>;
  musicCollections(...args: OperationRequestArgs<"tiktok-mobile-music-collections">): Promise<OperationResponseMap["tiktok-mobile-music-collections"]>;
  musicDetail(...args: OperationRequestArgs<"tiktok-mobile-music-detail">): Promise<OperationResponseMap["tiktok-mobile-music-detail"]>;
  musicPick(...args: OperationRequestArgs<"tiktok-mobile-music-pick">): Promise<OperationResponseMap["tiktok-mobile-music-pick"]>;
  musicPosts(...args: OperationRequestArgs<"tiktok-mobile-music-posts">): Promise<OperationResponseMap["tiktok-mobile-music-posts"]>;
  musicRelated(...args: OperationRequestArgs<"tiktok-mobile-music-related">): Promise<OperationResponseMap["tiktok-mobile-music-related"]>;
  musicTrending(...args: OperationRequestArgs<"tiktok-mobile-music-trending">): Promise<OperationResponseMap["tiktok-mobile-music-trending"]>;
  mvVideos(...args: OperationRequestArgs<"tiktok-mobile-mv-videos">): Promise<OperationResponseMap["tiktok-mobile-mv-videos"]>;
  placeDetail(...args: OperationRequestArgs<"tiktok-mobile-place-detail">): Promise<OperationResponseMap["tiktok-mobile-place-detail"]>;
  placeInfo(...args: OperationRequestArgs<"tiktok-mobile-place-info">): Promise<OperationResponseMap["tiktok-mobile-place-info"]>;
  placeMedia(...args: OperationRequestArgs<"tiktok-mobile-place-media">): Promise<OperationResponseMap["tiktok-mobile-place-media"]>;
  placePhotos(...args: OperationRequestArgs<"tiktok-mobile-place-photos">): Promise<OperationResponseMap["tiktok-mobile-place-photos"]>;
  placeReviews(...args: OperationRequestArgs<"tiktok-mobile-place-reviews">): Promise<OperationResponseMap["tiktok-mobile-place-reviews"]>;
  placeVideos(...args: OperationRequestArgs<"tiktok-mobile-place-videos">): Promise<OperationResponseMap["tiktok-mobile-place-videos"]>;
  playlistDetail(...args: OperationRequestArgs<"tiktok-mobile-playlist-detail">): Promise<OperationResponseMap["tiktok-mobile-playlist-detail"]>;
  playlistList(...args: OperationRequestArgs<"tiktok-mobile-playlist-list">): Promise<OperationResponseMap["tiktok-mobile-playlist-list"]>;
  playlistVideos(...args: OperationRequestArgs<"tiktok-mobile-playlist-videos">): Promise<OperationResponseMap["tiktok-mobile-playlist-videos"]>;
  search(...args: OperationRequestArgs<"tiktok-mobile-search">): Promise<OperationResponseMap["tiktok-mobile-search"]>;
  searchEffects(...args: OperationRequestArgs<"tiktok-mobile-search-effects">): Promise<OperationResponseMap["tiktok-mobile-search-effects"]>;
  searchHashtags(...args: OperationRequestArgs<"tiktok-mobile-search-hashtags">): Promise<OperationResponseMap["tiktok-mobile-search-hashtags"]>;
  searchMusic(...args: OperationRequestArgs<"tiktok-mobile-search-music">): Promise<OperationResponseMap["tiktok-mobile-search-music"]>;
  searchPhotos(...args: OperationRequestArgs<"tiktok-mobile-search-photos">): Promise<OperationResponseMap["tiktok-mobile-search-photos"]>;
  searchPlace(...args: OperationRequestArgs<"tiktok-mobile-search-place">): Promise<OperationResponseMap["tiktok-mobile-search-place"]>;
  searchPreInfo(...args: OperationRequestArgs<"tiktok-mobile-search-pre-info">): Promise<OperationResponseMap["tiktok-mobile-search-pre-info"]>;
  searchStream(...args: OperationRequestArgs<"tiktok-mobile-search-stream">): Promise<OperationResponseMap["tiktok-mobile-search-stream"]>;
  searchSug(...args: OperationRequestArgs<"tiktok-mobile-search-sug">): Promise<OperationResponseMap["tiktok-mobile-search-sug"]>;
  searchTabs(...args: OperationRequestArgs<"tiktok-mobile-search-tabs">): Promise<OperationResponseMap["tiktok-mobile-search-tabs"]>;
  searchUser(...args: OperationRequestArgs<"tiktok-mobile-search-user">): Promise<OperationResponseMap["tiktok-mobile-search-user"]>;
  searchVideos(...args: OperationRequestArgs<"tiktok-mobile-search-videos">): Promise<OperationResponseMap["tiktok-mobile-search-videos"]>;
  translationDescription(...args: OperationRequestArgs<"tiktok-mobile-translation-description">): Promise<OperationResponseMap["tiktok-mobile-translation-description"]>;
  trendingCategories(...args: OperationRequestArgs<"tiktok-mobile-trending-categories">): Promise<OperationResponseMap["tiktok-mobile-trending-categories"]>;
  trendingEffects(...args: OperationRequestArgs<"tiktok-mobile-trending-effects">): Promise<OperationResponseMap["tiktok-mobile-trending-effects"]>;
  userFollowers(...args: OperationRequestArgs<"tiktok-mobile-user-followers">): Promise<OperationResponseMap["tiktok-mobile-user-followers"]>;
  userFollowing(...args: OperationRequestArgs<"tiktok-mobile-user-following">): Promise<OperationResponseMap["tiktok-mobile-user-following"]>;
  userOriginalEffects(...args: OperationRequestArgs<"tiktok-mobile-user-original-effects">): Promise<OperationResponseMap["tiktok-mobile-user-original-effects"]>;
  userOriginalMusic(...args: OperationRequestArgs<"tiktok-mobile-user-original-music">): Promise<OperationResponseMap["tiktok-mobile-user-original-music"]>;
  userPosts(...args: OperationRequestArgs<"tiktok-mobile-user-posts">): Promise<OperationResponseMap["tiktok-mobile-user-posts"]>;
  userProfile(...args: OperationRequestArgs<"tiktok-mobile-user-profile">): Promise<OperationResponseMap["tiktok-mobile-user-profile"]>;
  userRecommendations(...args: OperationRequestArgs<"tiktok-mobile-user-recommendations">): Promise<OperationResponseMap["tiktok-mobile-user-recommendations"]>;
  videoDetail(...args: OperationRequestArgs<"tiktok-mobile-video-detail">): Promise<OperationResponseMap["tiktok-mobile-video-detail"]>;
  videoSubtitles(...args: OperationRequestArgs<"tiktok-mobile-video-subtitles">): Promise<OperationResponseMap["tiktok-mobile-video-subtitles"]>;
}
export { TikTokMobileClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default TikTokMobileClient;
