from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelTiktokmobileVideoSubtitlesResponseDoc = TypedDict('ModelTiktokmobileVideoSubtitlesResponseDoc', {
    'content_source': NotRequired[str],
    'cue_count': NotRequired[int],
    'cues': NotRequired[list[ModelTiktokmobileSubtitleCue]],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'language': NotRequired[str],
    'variant': NotRequired[str],
    'video_id': NotRequired[str],
    'webvtt': NotRequired[str],
}, total=False)

ModelTiktokmobileSubtitleCue = TypedDict('ModelTiktokmobileSubtitleCue', {
    'end': NotRequired[str],
    'end_ms': NotRequired[int],
    'start': NotRequired[str],
    'start_ms': NotRequired[int],
    'text': NotRequired[str],
}, total=False)

ModelTiktokmobileVideoDetailResponseDoc = TypedDict('ModelTiktokmobileVideoDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileVideoDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileVideoDetailResponse = TypedDict('ModelTiktokmobileVideoDetailResponse', {
    'aweme_detail': NotRequired[Any],
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserRecommendationsResponseDoc = TypedDict('ModelTiktokmobileUserRecommendationsResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileUserProfileResponseDoc = TypedDict('ModelTiktokmobileUserProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserProfileResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserProfileResponse = TypedDict('ModelTiktokmobileUserProfileResponse', {
    'common': NotRequired[Any],
    'extra': NotRequired[Any],
    'header': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'nav_bar': NotRequired[Any],
    'profile_tab': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserPostsResponseDoc = TypedDict('ModelTiktokmobileUserPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserPostsResponse = TypedDict('ModelTiktokmobileUserPostsResponse', {
    'aweme_list': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_cursor': NotRequired[int],
    'min_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalMusicResponseDoc = TypedDict('ModelTiktokmobileUserOriginalMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserOriginalMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalMusicResponse = TypedDict('ModelTiktokmobileUserOriginalMusicResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'groups': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'honor_label': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalEffectsResponseDoc = TypedDict('ModelTiktokmobileUserOriginalEffectsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserOriginalEffectsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalEffectsResponse = TypedDict('ModelTiktokmobileUserOriginalEffectsResponse', {
    'cursor': NotRequired[int],
    'effect': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserFollowingResponseDoc = TypedDict('ModelTiktokmobileUserFollowingResponseDoc', {
    'extra': NotRequired[Any],
    'followings': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_time': NotRequired[int],
    'min_time': NotRequired[int],
    'myself_user_id': NotRequired[Any],
    'next_page_token': NotRequired[str],
    'offset': NotRequired[int],
    'rec_has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileUserFollowersResponseDoc = TypedDict('ModelTiktokmobileUserFollowersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserFollowersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserFollowersResponse = TypedDict('ModelTiktokmobileUserFollowersResponse', {
    'extra': NotRequired[Any],
    'followers': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_time': NotRequired[int],
    'min_time': NotRequired[int],
    'myself_user_id': NotRequired[str],
    'next_page_token': NotRequired[str],
    'offset': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileStickerDiscoverResponseDoc = TypedDict('ModelTiktokmobileStickerDiscoverResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileStickerDiscoverResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileStickerDiscoverResponse = TypedDict('ModelTiktokmobileStickerDiscoverResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feed_session_id': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCategoryListResponseDoc = TypedDict('ModelTiktokmobileCategoryListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCategoryListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCategoryListResponse = TypedDict('ModelTiktokmobileCategoryListResponse', {
    'category_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'device_type': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileTranslationDescriptionResponseDoc = TypedDict('ModelTiktokmobileTranslationDescriptionResponseDoc', {
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'format': NotRequired[int],
    'host': NotRequired[str],
    'item_id': NotRequired[str],
    'log_pb': NotRequired[Any],
    'perf_metrics': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'target_lang': NotRequired[str],
    'text': NotRequired[str],
    'translated_client_text': NotRequired[Any],
    'variant': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchVideosResponseDoc = TypedDict('ModelTiktokmobileSearchVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchVideosResponse = TypedDict('ModelTiktokmobileSearchVideosResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'search_id': NotRequired[str],
    'search_item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchUsersResponseDoc = TypedDict('ModelTiktokmobileSearchUsersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchUsersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchUsersResponse = TypedDict('ModelTiktokmobileSearchUsersResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileSearchTabsResponseDoc = TypedDict('ModelTiktokmobileSearchTabsResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'is_failed': NotRequired[int],
    'keyword': NotRequired[str],
    'tabs': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileSearchSuggestionResponseDoc = TypedDict('ModelTiktokmobileSearchSuggestionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchSuggestionResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchSuggestionResponse = TypedDict('ModelTiktokmobileSearchSuggestionResponse', {
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'sug_list': NotRequired[list[ModelTiktokmobileSearchSuggestion]],
}, total=False)

ModelTiktokmobileSearchSuggestion = TypedDict('ModelTiktokmobileSearchSuggestion', {
    'content': NotRequired[str],
    'extra_info': NotRequired[Any],
    'highlight_pos': NotRequired[Any],
    'pos': NotRequired[Any],
    'rich_sug_sec_pos': NotRequired[Any],
    'sug_type': NotRequired[str],
    'word_record': NotRequired[Any],
}, total=False)

ModelTiktokmobileSearchStreamResponseDoc = TypedDict('ModelTiktokmobileSearchStreamResponseDoc', {
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'documents': NotRequired[list[Any]],
    'fetched_at': NotRequired[str],
    'frame_count': NotRequired[int],
    'frames': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'keyword': NotRequired[str],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchPreInfoResponseDoc = TypedDict('ModelTiktokmobileSearchPreInfoResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'pre_info_id': NotRequired[str],
    'ttl': NotRequired[int],
}, total=False)

ModelTiktokmobileSearchPlaceResponseDoc = TypedDict('ModelTiktokmobileSearchPlaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchPlaceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchPlaceResponse = TypedDict('ModelTiktokmobileSearchPlaceResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'poi_info': NotRequired[ModelTiktokmobilePlacePoicontainer],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlacePoicontainer = TypedDict('ModelTiktokmobilePlacePoicontainer', {
    'poi_info': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileSearchPhotosResponseDoc = TypedDict('ModelTiktokmobileSearchPhotosResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'backtrace': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[int],
    'log_pb': NotRequired[Any],
    'response_cropped': NotRequired[int],
    'search_item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchMusicResponseDoc = TypedDict('ModelTiktokmobileSearchMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchMusicResponse = TypedDict('ModelTiktokmobileSearchMusicResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'music': NotRequired[list[Any]],
    'music_info_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileHashtagSuggestionsResponseDoc = TypedDict('ModelTiktokmobileHashtagSuggestionsResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'sug_list': NotRequired[list[Any]],
    'words_query_record': NotRequired[Any],
}, total=False)

ModelTiktokmobileSearchEffectsResponseDoc = TypedDict('ModelTiktokmobileSearchEffectsResponseDoc', {
    'bind_effects': NotRequired[Any],
    'collection': NotRequired[Any],
    'cursor': NotRequired[int],
    'effects': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'search_id': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'use_hot': NotRequired[bool],
}, total=False)

ModelTiktokmobileSearchGeneralResponseDoc = TypedDict('ModelTiktokmobileSearchGeneralResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchGeneralResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchGeneralResponse = TypedDict('ModelTiktokmobileSearchGeneralResponse', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'search_id': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistVideosResponseDoc = TypedDict('ModelTiktokmobilePlaylistVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistVideosResponse = TypedDict('ModelTiktokmobilePlaylistVideosResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistListResponseDoc = TypedDict('ModelTiktokmobilePlaylistListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistListResponse = TypedDict('ModelTiktokmobilePlaylistListResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mix_list': NotRequired[list[ModelTiktokmobilePlaylistSummary]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobilePlaylistSummary = TypedDict('ModelTiktokmobilePlaylistSummary', {
    'author': NotRequired[Any],
    'creator_name': NotRequired[str],
    'last_add_video_timestamp': NotRequired[int],
    'mix_id': NotRequired[str],
    'mix_type': NotRequired[int],
    'name': NotRequired[str],
    'share_info': NotRequired[Any],
    'statistic': NotRequired[Any],
    'status': NotRequired[Any],
}, total=False)

ModelTiktokmobilePlaylistDetailResponseDoc = TypedDict('ModelTiktokmobilePlaylistDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistDetailResponse = TypedDict('ModelTiktokmobilePlaylistDetailResponse', {
    'extra': NotRequired[Any],
    'is_collect': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mix': NotRequired[ModelTiktokmobilePlaylistSummary],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceVideosResponseDoc = TypedDict('ModelTiktokmobilePlaceVideosResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'item_count': NotRequired[int],
    'poi_id': NotRequired[str],
    'poi_info': NotRequired[Any],
}, total=False)

ModelTiktokmobilePlaceReviewsResponseDoc = TypedDict('ModelTiktokmobilePlaceReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaceReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceReviewsResponse = TypedDict('ModelTiktokmobilePlaceReviewsResponse', {
    'collect_info': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'folded_cursor': NotRequired[int],
    'folded_has_more': NotRequired[bool],
    'has_more': NotRequired[bool],
    'is_hide_review_summary': NotRequired[bool],
    'landing_tab': NotRequired[int],
    'log_pb': NotRequired[Any],
    'poi_id': NotRequired[str],
    'poi_name': NotRequired[str],
    'post_review_description': NotRequired[str],
    'post_review_sub_description': NotRequired[str],
    'review_summary': NotRequired[Any],
    'review_tags': NotRequired[list[Any]],
    'reviews': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlacePhotosResponseDoc = TypedDict('ModelTiktokmobilePlacePhotosResponseDoc', {
    'categories': NotRequired[list[Any]],
    'category_tab_info': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'photo_count': NotRequired[int],
    'poi_id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceMediaResponseDoc = TypedDict('ModelTiktokmobilePlaceMediaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaceMediaResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceMediaResponse = TypedDict('ModelTiktokmobilePlaceMediaResponse', {
    'data_version': NotRequired[str],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'item_list': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'next_cursor': NotRequired[str],
    'pos': NotRequired[Any],
    'post_bottom_bar_style': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceInfoResponseDoc = TypedDict('ModelTiktokmobilePlaceInfoResponseDoc', {
    'address': NotRequired[str],
    'average_price': NotRequired[str],
    'category': NotRequired[str],
    'city_code': NotRequired[str],
    'claim_store_status': NotRequired[bool],
    'cover': NotRequired[Any],
    'favorite_count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'is_collected': NotRequired[bool],
    'latitude': NotRequired[str],
    'longitude': NotRequired[str],
    'name': NotRequired[str],
    'no_rating': NotRequired[bool],
    'opening_hours': NotRequired[str],
    'opening_status': NotRequired[bool],
    'parent_poi': NotRequired[Any],
    'place': NotRequired[dict[str, Any]],
    'poi_id': NotRequired[str],
    'region_code': NotRequired[str],
    'review_count': NotRequired[int],
    'review_score': NotRequired[float],
    'review_score_display': NotRequired[str],
    'share_desc': NotRequired[str],
    'share_url': NotRequired[str],
    'video_count': NotRequired[int],
}, total=False)

ModelTiktokmobilePlaceDetailResponseDoc = TypedDict('ModelTiktokmobilePlaceDetailResponseDoc', {
    'fetched_at': NotRequired[str],
    'frame_count': NotRequired[int],
    'frames': NotRequired[list[Any]],
    'has_more_posts': NotRequired[bool],
    'has_more_reviews': NotRequired[bool],
    'host': NotRequired[str],
    'layout': NotRequired[dict[str, Any]],
    'nodes': NotRequired[dict[str, Any]],
    'page_id': NotRequired[str],
    'poi_id': NotRequired[str],
    'post_count': NotRequired[int],
    'post_cursor': NotRequired[int],
    'review_count': NotRequired[int],
    'top_video_count': NotRequired[int],
}, total=False)

ModelTiktokmobileMvFeedResponseDoc = TypedDict('ModelTiktokmobileMvFeedResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'item_count': NotRequired[int],
    'log_pb': NotRequired[Any],
    'mv_id': NotRequired[str],
    'original_aweme_id': NotRequired[str],
    'page_extra': NotRequired[Any],
    'top_awemes': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileHotMusicResponseDoc = TypedDict('ModelTiktokmobileHotMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHotMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHotMusicResponse = TypedDict('ModelTiktokmobileHotMusicResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicRelatedResponseDoc = TypedDict('ModelTiktokmobileMusicRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicRelatedResponse = TypedDict('ModelTiktokmobileMusicRelatedResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'music_list': NotRequired[list[Any]],
    'music_type': NotRequired[int],
    'recall_info_list': NotRequired[list[Any]],
    'similar_song_ids': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicFreshAwemeResponseDoc = TypedDict('ModelTiktokmobileMusicFreshAwemeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicFreshAwemeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicFreshAwemeResponse = TypedDict('ModelTiktokmobileMusicFreshAwemeResponse', {
    'aweme_list': NotRequired[list[Any]],
    'can_pin_video': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'need_lazy_loading': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicPickResponseDoc = TypedDict('ModelTiktokmobileMusicPickResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicPickResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicPickResponse = TypedDict('ModelTiktokmobileMusicPickResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'mc_list': NotRequired[list[Any]],
    'music_list': NotRequired[list[Any]],
    'radio_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicDetailResponseDoc = TypedDict('ModelTiktokmobileMusicDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicDetailResponse = TypedDict('ModelTiktokmobileMusicDetailResponse', {
    'ai_recommend_music': NotRequired[Any],
    'ai_recommend_video': NotRequired[Any],
    'behind_the_song_exist': NotRequired[bool],
    'cost_time_info': NotRequired[Any],
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_chart_rank': NotRequired[Any],
    'music_info': NotRequired[Any],
    'rec_list': NotRequired[Any],
    'similar_music': NotRequired[Any],
    'similar_music_ids': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionFeedResponseDoc = TypedDict('ModelTiktokmobileMusicCollectionFeedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicCollectionFeedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionFeedResponse = TypedDict('ModelTiktokmobileMusicCollectionFeedResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mcf_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionListResponseDoc = TypedDict('ModelTiktokmobileMusicCollectionListResponseDoc', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mc_list': NotRequired[list[Any]],
    'msg': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChoicesResponseDoc = TypedDict('ModelTiktokmobileMusicChoicesResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChartResponseDoc = TypedDict('ModelTiktokmobileMusicChartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChartResponse = TypedDict('ModelTiktokmobileMusicChartResponse', {
    'chart_info': NotRequired[Any],
    'cover_image_url': NotRequired[str],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicBeatsSongsResponseDoc = TypedDict('ModelTiktokmobileMusicBeatsSongsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicBeatsSongsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicBeatsSongsResponse = TypedDict('ModelTiktokmobileMusicBeatsSongsResponse', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveTabsResponseDoc = TypedDict('ModelTiktokmobileLiveTabsResponseDoc', {
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveSearchResponseDoc = TypedDict('ModelTiktokmobileLiveSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileLiveSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveSearchResponse = TypedDict('ModelTiktokmobileLiveSearchResponse', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'extra_data': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'global_doodle_config': NotRequired[Any],
    'guide_search_words': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomInfoResponseDoc = TypedDict('ModelTiktokmobileLiveRoomInfoResponseDoc', {
    'cover': NotRequired[Any],
    'create_time': NotRequired[int],
    'data': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'owner': NotRequired[ModelTiktokmobileLiveRoomOwner],
    'room_id': NotRequired[str],
    'stats': NotRequired[ModelTiktokmobileLiveRoomStats],
    'status': NotRequired[int],
    'stream': NotRequired[ModelTiktokmobileLiveRoomStream],
    'title': NotRequired[str],
    'user_count': NotRequired[int],
    'user_id': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomStream = TypedDict('ModelTiktokmobileLiveRoomStream', {
    'candidate_resolution': NotRequired[list[str]],
    'default_resolution': NotRequired[str],
    'flv_pull_url': NotRequired[dict[str, str]],
    'hls_pull_url': NotRequired[str],
    'rtmp_pull_url': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomStats = TypedDict('ModelTiktokmobileLiveRoomStats', {
    'comment_count': NotRequired[int],
    'enter_count': NotRequired[int],
    'follow_count': NotRequired[int],
    'like_count': NotRequired[int],
    'replay_viewers': NotRequired[int],
    'share_count': NotRequired[int],
    'total_user': NotRequired[int],
    'watch_user_count': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveRoomOwner = TypedDict('ModelTiktokmobileLiveRoomOwner', {
    'avatar': NotRequired[Any],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveHashtagCatalogResponseDoc = TypedDict('ModelTiktokmobileLiveHashtagCatalogResponseDoc', {
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'game_hashtag': NotRequired[ModelTiktokmobileLiveHashtag],
    'game_tag_count': NotRequired[int],
    'game_tag_list': NotRequired[list[ModelTiktokmobileLiveGameTag]],
    'hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'host': NotRequired[str],
    'live_studio_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'live_voice_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'third_party_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
}, total=False)

ModelTiktokmobileLiveHashtag = TypedDict('ModelTiktokmobileLiveHashtag', {
    'id': NotRequired[int],
    'image': NotRequired[Any],
    'namespace': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGameTag = TypedDict('ModelTiktokmobileLiveGameTag', {
    'bundle_id': NotRequired[str],
    'full_name': NotRequired[str],
    'game_category': NotRequired[list[ModelTiktokmobileLiveGameCategory]],
    'gar': NotRequired[list[Any]],
    'hashtag_id': NotRequired[list[Any]],
    'hashtag_list': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'id': NotRequired[int],
    'is_new_game': NotRequired[bool],
    'landscape': NotRequired[int],
    'package_name': NotRequired[str],
    'short_name': NotRequired[str],
    'show_name': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGameCategory = TypedDict('ModelTiktokmobileLiveGameCategory', {
    'game_type': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGiftsResponseDoc = TypedDict('ModelTiktokmobileLiveGiftsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileWebcastGiftListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileWebcastGiftListResponse = TypedDict('ModelTiktokmobileWebcastGiftListResponse', {
    'data': NotRequired[Any],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveEffectsResponseDoc = TypedDict('ModelTiktokmobileLiveEffectsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileWebcastEffectsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileWebcastEffectsResponse = TypedDict('ModelTiktokmobileWebcastEffectsResponse', {
    'data': NotRequired[ModelTiktokmobileWebcastEffectsData],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileWebcastEffectsData = TypedDict('ModelTiktokmobileWebcastEffectsData', {
    'assets': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileHashtagSearchResponseDoc = TypedDict('ModelTiktokmobileHashtagSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagSearchResponse = TypedDict('ModelTiktokmobileHashtagSearchResponse', {
    'challenge_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagPostsResponseDoc = TypedDict('ModelTiktokmobileHashtagPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagPostsResponse = TypedDict('ModelTiktokmobileHashtagPostsResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagInfoResponseDoc = TypedDict('ModelTiktokmobileHashtagInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagInfoResponse = TypedDict('ModelTiktokmobileHashtagInfoResponse', {
    'ch_info': NotRequired[Any],
    'hashtag_name': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileFeedPostResponseDoc = TypedDict('ModelTiktokmobileFeedPostResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[dict[str, Any]],
    'note': NotRequired[str],
    'strings': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileOfflineFeedResponseDoc = TypedDict('ModelTiktokmobileOfflineFeedResponseDoc', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[dict[str, Any]],
    'note': NotRequired[str],
    'pull_type': NotRequired[int],
    'strings': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileFeedResponseDoc = TypedDict('ModelTiktokmobileFeedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileFeedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileFeedResponse = TypedDict('ModelTiktokmobileFeedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[list[ModelTiktokmobileFeedItem]],
}, total=False)

ModelTiktokmobileFeedItem = TypedDict('ModelTiktokmobileFeedItem', {
    'author_id': NotRequired[int],
    'author_id_str': NotRequired[str],
    'aweme_id': NotRequired[str],
    'create_time': NotRequired[int],
    'share_url': NotRequired[str],
    'statistics': NotRequired[ModelTiktokmobileFeedStatistics],
}, total=False)

ModelTiktokmobileFeedStatistics = TypedDict('ModelTiktokmobileFeedStatistics', {
    'aweme_id': NotRequired[str],
    'collect_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'digg_count': NotRequired[int],
    'download_count': NotRequired[int],
    'forward_count': NotRequired[int],
    'lose_comment_count': NotRequired[int],
    'lose_count': NotRequired[int],
    'play_count': NotRequired[int],
    'repost_count': NotRequired[int],
    'share_count': NotRequired[int],
    'whatsapp_share_count': NotRequired[int],
}, total=False)

ModelTiktokmobileCommentsResponseDoc = TypedDict('ModelTiktokmobileCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCommentsResponse = TypedDict('ModelTiktokmobileCommentsResponse', {
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileCommentRepliesResponseDoc = TypedDict('ModelTiktokmobileCommentRepliesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCommentRepliesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCommentRepliesResponse = TypedDict('ModelTiktokmobileCommentRepliesResponse', {
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileCollectionVideosResponseDoc = TypedDict('ModelTiktokmobileCollectionVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionVideosResponse = TypedDict('ModelTiktokmobileCollectionVideosResponse', {
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'max_cursor': NotRequired[int],
    'min_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionListResponseDoc = TypedDict('ModelTiktokmobileCollectionListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionListResponse = TypedDict('ModelTiktokmobileCollectionListResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'item_archive_detail_list': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionDetailResponseDoc = TypedDict('ModelTiktokmobileCollectionDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionDetailResponse = TypedDict('ModelTiktokmobileCollectionDetailResponse', {
    'extra': NotRequired[Any],
    'item_archive': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileAnchorListResponseDoc = TypedDict('ModelTiktokmobileAnchorListResponseDoc', {
    'anchors': NotRequired[list[Any]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
}, total=False)

TiktokMobileAnchorListResponse = ModelTiktokmobileAnchorListResponseDoc
TiktokMobileAnchorListParams = TypedDict('TiktokMobileAnchorListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileCollectionDetailResponse = ModelTiktokmobileCollectionDetailResponseDoc
TiktokMobileCollectionDetailParams = TypedDict('TiktokMobileCollectionDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionListResponse = ModelTiktokmobileCollectionListResponseDoc
TiktokMobileCollectionListParams = TypedDict('TiktokMobileCollectionListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosResponse = ModelTiktokmobileCollectionVideosResponseDoc
TiktokMobileCollectionVideosParams = TypedDict('TiktokMobileCollectionVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesResponse = ModelTiktokmobileCommentRepliesResponseDoc
TiktokMobileCommentRepliesParams = TypedDict('TiktokMobileCommentRepliesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsResponse = ModelTiktokmobileCommentsResponseDoc
TiktokMobileCommentsParams = TypedDict('TiktokMobileCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedResponse = ModelTiktokmobileFeedResponseDoc
TiktokMobileFeedParams = TypedDict('TiktokMobileFeedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineResponse = ModelTiktokmobileOfflineFeedResponseDoc
TiktokMobileFeedOfflineParams = TypedDict('TiktokMobileFeedOfflineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedPostResponse = ModelTiktokmobileFeedPostResponseDoc
TiktokMobileFeedPostParams = TypedDict('TiktokMobileFeedPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileHashtagResponse = ModelTiktokmobileHashtagInfoResponseDoc
TiktokMobileHashtagParams = TypedDict('TiktokMobileHashtagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagPostsResponse = ModelTiktokmobileHashtagPostsResponseDoc
TiktokMobileHashtagPostsParams = TypedDict('TiktokMobileHashtagPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsResponse = ModelTiktokmobileHashtagSearchResponseDoc
TiktokMobileHashtagsParams = TypedDict('TiktokMobileHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileLiveEffectsResponse = ModelTiktokmobileLiveEffectsResponseDoc
TiktokMobileLiveEffectsParams = TypedDict('TiktokMobileLiveEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveGiftsResponse = ModelTiktokmobileLiveGiftsResponseDoc
TiktokMobileLiveGiftsParams = TypedDict('TiktokMobileLiveGiftsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveHashtagsResponse = ModelTiktokmobileLiveHashtagCatalogResponseDoc
TiktokMobileLiveHashtagsParams = TypedDict('TiktokMobileLiveHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveRoomResponse = ModelTiktokmobileLiveRoomInfoResponseDoc
TiktokMobileLiveRoomParams = TypedDict('TiktokMobileLiveRoomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserResponse = ModelTiktokmobileLiveRoomInfoResponseDoc
TiktokMobileLiveRoomByUserParams = TypedDict('TiktokMobileLiveRoomByUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveSearchResponse = ModelTiktokmobileLiveSearchResponseDoc
TiktokMobileLiveSearchParams = TypedDict('TiktokMobileLiveSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveTabsResponse = ModelTiktokmobileLiveTabsResponseDoc
TiktokMobileLiveTabsParams = TypedDict('TiktokMobileLiveTabsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileMusicBeatsResponse = ModelTiktokmobileMusicBeatsSongsResponseDoc
TiktokMobileMusicBeatsParams = TypedDict('TiktokMobileMusicBeatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartResponse = ModelTiktokmobileMusicChartResponseDoc
TiktokMobileMusicChartParams = TypedDict('TiktokMobileMusicChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChoicesResponse = ModelTiktokmobileMusicChoicesResponseDoc
TiktokMobileMusicChoicesParams = TypedDict('TiktokMobileMusicChoicesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileMusicCollectionListResponse = ModelTiktokmobileMusicCollectionListResponseDoc
TiktokMobileMusicCollectionListParams = TypedDict('TiktokMobileMusicCollectionListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsResponse = ModelTiktokmobileMusicCollectionFeedResponseDoc
TiktokMobileMusicCollectionsParams = TypedDict('TiktokMobileMusicCollectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicDetailResponse = ModelTiktokmobileMusicDetailResponseDoc
TiktokMobileMusicDetailParams = TypedDict('TiktokMobileMusicDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicPickResponse = ModelTiktokmobileMusicPickResponseDoc
TiktokMobileMusicPickParams = TypedDict('TiktokMobileMusicPickParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsResponse = ModelTiktokmobileMusicFreshAwemeResponseDoc
TiktokMobileMusicPostsParams = TypedDict('TiktokMobileMusicPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedResponse = ModelTiktokmobileMusicRelatedResponseDoc
TiktokMobileMusicRelatedParams = TypedDict('TiktokMobileMusicRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingResponse = ModelTiktokmobileHotMusicResponseDoc
TiktokMobileMusicTrendingParams = TypedDict('TiktokMobileMusicTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosResponse = ModelTiktokmobileMvFeedResponseDoc
TiktokMobileMvVideosParams = TypedDict('TiktokMobileMvVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceDetailResponse = ModelTiktokmobilePlaceDetailResponseDoc
TiktokMobilePlaceDetailParams = TypedDict('TiktokMobilePlaceDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceInfoResponse = ModelTiktokmobilePlaceInfoResponseDoc
TiktokMobilePlaceInfoParams = TypedDict('TiktokMobilePlaceInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceMediaResponse = ModelTiktokmobilePlaceMediaResponseDoc
TiktokMobilePlaceMediaParams = TypedDict('TiktokMobilePlaceMediaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlacePhotosResponse = ModelTiktokmobilePlacePhotosResponseDoc
TiktokMobilePlacePhotosParams = TypedDict('TiktokMobilePlacePhotosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceReviewsResponse = ModelTiktokmobilePlaceReviewsResponseDoc
TiktokMobilePlaceReviewsParams = TypedDict('TiktokMobilePlaceReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceVideosResponse = ModelTiktokmobilePlaceVideosResponseDoc
TiktokMobilePlaceVideosParams = TypedDict('TiktokMobilePlaceVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistDetailResponse = ModelTiktokmobilePlaylistDetailResponseDoc
TiktokMobilePlaylistDetailParams = TypedDict('TiktokMobilePlaylistDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistListResponse = ModelTiktokmobilePlaylistListResponseDoc
TiktokMobilePlaylistListParams = TypedDict('TiktokMobilePlaylistListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosResponse = ModelTiktokmobilePlaylistVideosResponseDoc
TiktokMobilePlaylistVideosParams = TypedDict('TiktokMobilePlaylistVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchResponse = ModelTiktokmobileSearchGeneralResponseDoc
TiktokMobileSearchParams = TypedDict('TiktokMobileSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsResponse = ModelTiktokmobileSearchEffectsResponseDoc
TiktokMobileSearchEffectsParams = TypedDict('TiktokMobileSearchEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchHashtagsResponse = ModelTiktokmobileHashtagSuggestionsResponseDoc
TiktokMobileSearchHashtagsParams = TypedDict('TiktokMobileSearchHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicResponse = ModelTiktokmobileSearchMusicResponseDoc
TiktokMobileSearchMusicParams = TypedDict('TiktokMobileSearchMusicParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchPhotosResponse = ModelTiktokmobileSearchPhotosResponseDoc
TiktokMobileSearchPhotosParams = TypedDict('TiktokMobileSearchPhotosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPlaceResponse = ModelTiktokmobileSearchPlaceResponseDoc
TiktokMobileSearchPlaceParams = TypedDict('TiktokMobileSearchPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoResponse = ModelTiktokmobileSearchPreInfoResponseDoc
TiktokMobileSearchPreInfoParams = TypedDict('TiktokMobileSearchPreInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchStreamResponse = ModelTiktokmobileSearchStreamResponseDoc
TiktokMobileSearchStreamParams = TypedDict('TiktokMobileSearchStreamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchSugResponse = ModelTiktokmobileSearchSuggestionResponseDoc
TiktokMobileSearchSugParams = TypedDict('TiktokMobileSearchSugParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchTabsResponse = ModelTiktokmobileSearchTabsResponseDoc
TiktokMobileSearchTabsParams = TypedDict('TiktokMobileSearchTabsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchUserResponse = ModelTiktokmobileSearchUsersResponseDoc
TiktokMobileSearchUserParams = TypedDict('TiktokMobileSearchUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchVideosResponse = ModelTiktokmobileSearchVideosResponseDoc
TiktokMobileSearchVideosParams = TypedDict('TiktokMobileSearchVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionResponse = ModelTiktokmobileTranslationDescriptionResponseDoc
TiktokMobileTranslationDescriptionParams = TypedDict('TiktokMobileTranslationDescriptionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTrendingCategoriesResponse = ModelTiktokmobileCategoryListResponseDoc
TiktokMobileTrendingCategoriesParams = TypedDict('TiktokMobileTrendingCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsResponse = ModelTiktokmobileStickerDiscoverResponseDoc
TiktokMobileTrendingEffectsParams = TypedDict('TiktokMobileTrendingEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersResponse = ModelTiktokmobileUserFollowersResponseDoc
TiktokMobileUserFollowersParams = TypedDict('TiktokMobileUserFollowersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingResponse = ModelTiktokmobileUserFollowingResponseDoc
TiktokMobileUserFollowingParams = TypedDict('TiktokMobileUserFollowingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsResponse = ModelTiktokmobileUserOriginalEffectsResponseDoc
TiktokMobileUserOriginalEffectsParams = TypedDict('TiktokMobileUserOriginalEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicResponse = ModelTiktokmobileUserOriginalMusicResponseDoc
TiktokMobileUserOriginalMusicParams = TypedDict('TiktokMobileUserOriginalMusicParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserPostsResponse = ModelTiktokmobileUserPostsResponseDoc
TiktokMobileUserPostsParams = TypedDict('TiktokMobileUserPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserProfileResponse = ModelTiktokmobileUserProfileResponseDoc
TiktokMobileUserProfileParams = TypedDict('TiktokMobileUserProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserRecommendationsResponse = ModelTiktokmobileUserRecommendationsResponseDoc
TiktokMobileUserRecommendationsParams = TypedDict('TiktokMobileUserRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileVideoDetailResponse = ModelTiktokmobileVideoDetailResponseDoc
TiktokMobileVideoDetailParams = TypedDict('TiktokMobileVideoDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesResponse = ModelTiktokmobileVideoSubtitlesResponseDoc
TiktokMobileVideoSubtitlesParams = TypedDict('TiktokMobileVideoSubtitlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

class TiktokMobileGroup:
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...

OperationId = Literal[
    'tiktok-mobile-anchor-list',
    'tiktok-mobile-collection-detail',
    'tiktok-mobile-collection-list',
    'tiktok-mobile-collection-videos',
    'tiktok-mobile-comment-replies',
    'tiktok-mobile-comments',
    'tiktok-mobile-feed',
    'tiktok-mobile-feed-offline',
    'tiktok-mobile-feed-post',
    'tiktok-mobile-hashtag',
    'tiktok-mobile-hashtag-posts',
    'tiktok-mobile-hashtags',
    'tiktok-mobile-live-effects',
    'tiktok-mobile-live-gifts',
    'tiktok-mobile-live-hashtags',
    'tiktok-mobile-live-room',
    'tiktok-mobile-live-room-by-user',
    'tiktok-mobile-live-search',
    'tiktok-mobile-live-tabs',
    'tiktok-mobile-music-beats',
    'tiktok-mobile-music-chart',
    'tiktok-mobile-music-choices',
    'tiktok-mobile-music-collection-list',
    'tiktok-mobile-music-collections',
    'tiktok-mobile-music-detail',
    'tiktok-mobile-music-pick',
    'tiktok-mobile-music-posts',
    'tiktok-mobile-music-related',
    'tiktok-mobile-music-trending',
    'tiktok-mobile-mv-videos',
    'tiktok-mobile-place-detail',
    'tiktok-mobile-place-info',
    'tiktok-mobile-place-media',
    'tiktok-mobile-place-photos',
    'tiktok-mobile-place-reviews',
    'tiktok-mobile-place-videos',
    'tiktok-mobile-playlist-detail',
    'tiktok-mobile-playlist-list',
    'tiktok-mobile-playlist-videos',
    'tiktok-mobile-search',
    'tiktok-mobile-search-effects',
    'tiktok-mobile-search-hashtags',
    'tiktok-mobile-search-music',
    'tiktok-mobile-search-photos',
    'tiktok-mobile-search-place',
    'tiktok-mobile-search-pre-info',
    'tiktok-mobile-search-stream',
    'tiktok-mobile-search-sug',
    'tiktok-mobile-search-tabs',
    'tiktok-mobile-search-user',
    'tiktok-mobile-search-videos',
    'tiktok-mobile-translation-description',
    'tiktok-mobile-trending-categories',
    'tiktok-mobile-trending-effects',
    'tiktok-mobile-user-followers',
    'tiktok-mobile-user-following',
    'tiktok-mobile-user-original-effects',
    'tiktok-mobile-user-original-music',
    'tiktok-mobile-user-posts',
    'tiktok-mobile-user-profile',
    'tiktok-mobile-user-recommendations',
    'tiktok-mobile-video-detail',
    'tiktok-mobile-video-subtitles',
]

class CrawloraClient:
    tiktok_mobile: TiktokMobileGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-anchor-list'],
        params: TiktokMobileAnchorListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileAnchorListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-detail'],
        params: TiktokMobileCollectionDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-list'],
        params: TiktokMobileCollectionListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-videos'],
        params: TiktokMobileCollectionVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-comment-replies'],
        params: TiktokMobileCommentRepliesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-comments'],
        params: TiktokMobileCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed'],
        params: TiktokMobileFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed-offline'],
        params: TiktokMobileFeedOfflineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed-post'],
        params: TiktokMobileFeedPostParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtag'],
        params: TiktokMobileHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtag-posts'],
        params: TiktokMobileHashtagPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtags'],
        params: TiktokMobileHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-effects'],
        params: TiktokMobileLiveEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-gifts'],
        params: TiktokMobileLiveGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-hashtags'],
        params: TiktokMobileLiveHashtagsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-room'],
        params: TiktokMobileLiveRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-room-by-user'],
        params: TiktokMobileLiveRoomByUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-search'],
        params: TiktokMobileLiveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-tabs'],
        params: TiktokMobileLiveTabsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-beats'],
        params: TiktokMobileMusicBeatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-chart'],
        params: TiktokMobileMusicChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-choices'],
        params: TiktokMobileMusicChoicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-collection-list'],
        params: TiktokMobileMusicCollectionListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-collections'],
        params: TiktokMobileMusicCollectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-detail'],
        params: TiktokMobileMusicDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-pick'],
        params: TiktokMobileMusicPickParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPickResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-posts'],
        params: TiktokMobileMusicPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-related'],
        params: TiktokMobileMusicRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-trending'],
        params: TiktokMobileMusicTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-mv-videos'],
        params: TiktokMobileMvVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMvVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-detail'],
        params: TiktokMobilePlaceDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-info'],
        params: TiktokMobilePlaceInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-media'],
        params: TiktokMobilePlaceMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-photos'],
        params: TiktokMobilePlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-reviews'],
        params: TiktokMobilePlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-videos'],
        params: TiktokMobilePlaceVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-detail'],
        params: TiktokMobilePlaylistDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-list'],
        params: TiktokMobilePlaylistListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-videos'],
        params: TiktokMobilePlaylistVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search'],
        params: TiktokMobileSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-effects'],
        params: TiktokMobileSearchEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-hashtags'],
        params: TiktokMobileSearchHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-music'],
        params: TiktokMobileSearchMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-photos'],
        params: TiktokMobileSearchPhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-place'],
        params: TiktokMobileSearchPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-pre-info'],
        params: TiktokMobileSearchPreInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-stream'],
        params: TiktokMobileSearchStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-sug'],
        params: TiktokMobileSearchSugParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchSugResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-tabs'],
        params: TiktokMobileSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-user'],
        params: TiktokMobileSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-videos'],
        params: TiktokMobileSearchVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-translation-description'],
        params: TiktokMobileTranslationDescriptionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-trending-categories'],
        params: TiktokMobileTrendingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-trending-effects'],
        params: TiktokMobileTrendingEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-followers'],
        params: TiktokMobileUserFollowersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-following'],
        params: TiktokMobileUserFollowingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-original-effects'],
        params: TiktokMobileUserOriginalEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-original-music'],
        params: TiktokMobileUserOriginalMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-posts'],
        params: TiktokMobileUserPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-profile'],
        params: TiktokMobileUserProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-recommendations'],
        params: TiktokMobileUserRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-video-detail'],
        params: TiktokMobileVideoDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-video-subtitles'],
        params: TiktokMobileVideoSubtitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-anchor-list'],
        params: TiktokMobileAnchorListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileAnchorListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-detail'],
        params: TiktokMobileCollectionDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-list'],
        params: TiktokMobileCollectionListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-videos'],
        params: TiktokMobileCollectionVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-comment-replies'],
        params: TiktokMobileCommentRepliesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-comments'],
        params: TiktokMobileCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed'],
        params: TiktokMobileFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed-offline'],
        params: TiktokMobileFeedOfflineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed-post'],
        params: TiktokMobileFeedPostParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtag'],
        params: TiktokMobileHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtag-posts'],
        params: TiktokMobileHashtagPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtags'],
        params: TiktokMobileHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-effects'],
        params: TiktokMobileLiveEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-gifts'],
        params: TiktokMobileLiveGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-hashtags'],
        params: TiktokMobileLiveHashtagsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-room'],
        params: TiktokMobileLiveRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-room-by-user'],
        params: TiktokMobileLiveRoomByUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-search'],
        params: TiktokMobileLiveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-tabs'],
        params: TiktokMobileLiveTabsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-beats'],
        params: TiktokMobileMusicBeatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-chart'],
        params: TiktokMobileMusicChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-choices'],
        params: TiktokMobileMusicChoicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-collection-list'],
        params: TiktokMobileMusicCollectionListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-collections'],
        params: TiktokMobileMusicCollectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-detail'],
        params: TiktokMobileMusicDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-pick'],
        params: TiktokMobileMusicPickParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPickResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-posts'],
        params: TiktokMobileMusicPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-related'],
        params: TiktokMobileMusicRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-trending'],
        params: TiktokMobileMusicTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-mv-videos'],
        params: TiktokMobileMvVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMvVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-detail'],
        params: TiktokMobilePlaceDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-info'],
        params: TiktokMobilePlaceInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-media'],
        params: TiktokMobilePlaceMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-photos'],
        params: TiktokMobilePlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-reviews'],
        params: TiktokMobilePlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-videos'],
        params: TiktokMobilePlaceVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-detail'],
        params: TiktokMobilePlaylistDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-list'],
        params: TiktokMobilePlaylistListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-videos'],
        params: TiktokMobilePlaylistVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search'],
        params: TiktokMobileSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-effects'],
        params: TiktokMobileSearchEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-hashtags'],
        params: TiktokMobileSearchHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-music'],
        params: TiktokMobileSearchMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-photos'],
        params: TiktokMobileSearchPhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-place'],
        params: TiktokMobileSearchPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-pre-info'],
        params: TiktokMobileSearchPreInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-stream'],
        params: TiktokMobileSearchStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-sug'],
        params: TiktokMobileSearchSugParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchSugResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-tabs'],
        params: TiktokMobileSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-user'],
        params: TiktokMobileSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-videos'],
        params: TiktokMobileSearchVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-translation-description'],
        params: TiktokMobileTranslationDescriptionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-trending-categories'],
        params: TiktokMobileTrendingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-trending-effects'],
        params: TiktokMobileTrendingEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-followers'],
        params: TiktokMobileUserFollowersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-following'],
        params: TiktokMobileUserFollowingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-original-effects'],
        params: TiktokMobileUserOriginalEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-original-music'],
        params: TiktokMobileUserOriginalMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-posts'],
        params: TiktokMobileUserPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-profile'],
        params: TiktokMobileUserProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-recommendations'],
        params: TiktokMobileUserRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-video-detail'],
        params: TiktokMobileVideoDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-video-subtitles'],
        params: TiktokMobileVideoSubtitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class TikTokMobileClient(CrawloraClient):
    def __enter__(self) -> TikTokMobileClient: ...
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    def anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    def collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    def comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    def feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    def feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    def hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    def hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    def live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    def live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    def music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    def music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    def music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    def music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    def music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    def mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    def place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    def place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    def search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    def search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    def search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    def search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    def search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    def search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    def user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    def user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    def user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    def user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    def video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...

class AsyncTikTokMobileClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncTikTokMobileClient: ...
    tiktok_mobile: _AsyncTiktokMobileGroup
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...

class _AsyncTiktokMobileGroup:
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    async def anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    async def collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    async def collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    async def collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    async def comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    async def comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    async def feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    async def feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    async def feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    async def hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    async def hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    async def hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    async def live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    async def live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    async def live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    async def live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    async def live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    async def live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    async def live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    async def music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    async def music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    async def music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    async def music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    async def music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    async def music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    async def music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    async def music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    async def music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    async def music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    async def mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    async def place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    async def place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    async def place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    async def place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    async def playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    async def playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    async def playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    async def search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    async def search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    async def search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    async def search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    async def search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    async def search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    async def search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    async def search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    async def search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    async def translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    async def trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    async def user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    async def user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    async def user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    async def user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    async def user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    async def user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    async def video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    async def video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...

TiktokMobileAnchorListDefaultParams = TypedDict('TiktokMobileAnchorListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileAnchorListTextResponseParams = TypedDict('TiktokMobileAnchorListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileAnchorListStreamParams = TypedDict('TiktokMobileAnchorListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileCollectionDetailDefaultParams = TypedDict('TiktokMobileCollectionDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionDetailTextResponseParams = TypedDict('TiktokMobileCollectionDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionDetailStreamParams = TypedDict('TiktokMobileCollectionDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionListDefaultParams = TypedDict('TiktokMobileCollectionListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionListTextResponseParams = TypedDict('TiktokMobileCollectionListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionListStreamParams = TypedDict('TiktokMobileCollectionListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosDefaultParams = TypedDict('TiktokMobileCollectionVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosTextResponseParams = TypedDict('TiktokMobileCollectionVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosStreamParams = TypedDict('TiktokMobileCollectionVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesDefaultParams = TypedDict('TiktokMobileCommentRepliesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesTextResponseParams = TypedDict('TiktokMobileCommentRepliesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesStreamParams = TypedDict('TiktokMobileCommentRepliesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsDefaultParams = TypedDict('TiktokMobileCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsTextResponseParams = TypedDict('TiktokMobileCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsStreamParams = TypedDict('TiktokMobileCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedDefaultParams = TypedDict('TiktokMobileFeedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedTextResponseParams = TypedDict('TiktokMobileFeedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedStreamParams = TypedDict('TiktokMobileFeedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineDefaultParams = TypedDict('TiktokMobileFeedOfflineDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineTextResponseParams = TypedDict('TiktokMobileFeedOfflineTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineStreamParams = TypedDict('TiktokMobileFeedOfflineStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedPostDefaultParams = TypedDict('TiktokMobileFeedPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileFeedPostTextResponseParams = TypedDict('TiktokMobileFeedPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileFeedPostStreamParams = TypedDict('TiktokMobileFeedPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileHashtagDefaultParams = TypedDict('TiktokMobileHashtagDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagTextResponseParams = TypedDict('TiktokMobileHashtagTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagStreamParams = TypedDict('TiktokMobileHashtagStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagPostsDefaultParams = TypedDict('TiktokMobileHashtagPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagPostsTextResponseParams = TypedDict('TiktokMobileHashtagPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagPostsStreamParams = TypedDict('TiktokMobileHashtagPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsDefaultParams = TypedDict('TiktokMobileHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsTextResponseParams = TypedDict('TiktokMobileHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsStreamParams = TypedDict('TiktokMobileHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileLiveEffectsDefaultParams = TypedDict('TiktokMobileLiveEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveEffectsTextResponseParams = TypedDict('TiktokMobileLiveEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveEffectsStreamParams = TypedDict('TiktokMobileLiveEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveGiftsDefaultParams = TypedDict('TiktokMobileLiveGiftsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveGiftsTextResponseParams = TypedDict('TiktokMobileLiveGiftsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveGiftsStreamParams = TypedDict('TiktokMobileLiveGiftsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveHashtagsDefaultParams = TypedDict('TiktokMobileLiveHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveHashtagsTextResponseParams = TypedDict('TiktokMobileLiveHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveHashtagsStreamParams = TypedDict('TiktokMobileLiveHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveRoomDefaultParams = TypedDict('TiktokMobileLiveRoomDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomTextResponseParams = TypedDict('TiktokMobileLiveRoomTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomStreamParams = TypedDict('TiktokMobileLiveRoomStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserDefaultParams = TypedDict('TiktokMobileLiveRoomByUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserTextResponseParams = TypedDict('TiktokMobileLiveRoomByUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserStreamParams = TypedDict('TiktokMobileLiveRoomByUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveSearchDefaultParams = TypedDict('TiktokMobileLiveSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveSearchTextResponseParams = TypedDict('TiktokMobileLiveSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveSearchStreamParams = TypedDict('TiktokMobileLiveSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveTabsDefaultParams = TypedDict('TiktokMobileLiveTabsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveTabsTextResponseParams = TypedDict('TiktokMobileLiveTabsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveTabsStreamParams = TypedDict('TiktokMobileLiveTabsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileMusicBeatsDefaultParams = TypedDict('TiktokMobileMusicBeatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicBeatsTextResponseParams = TypedDict('TiktokMobileMusicBeatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicBeatsStreamParams = TypedDict('TiktokMobileMusicBeatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartDefaultParams = TypedDict('TiktokMobileMusicChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartTextResponseParams = TypedDict('TiktokMobileMusicChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartStreamParams = TypedDict('TiktokMobileMusicChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChoicesDefaultParams = TypedDict('TiktokMobileMusicChoicesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileMusicChoicesTextResponseParams = TypedDict('TiktokMobileMusicChoicesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileMusicChoicesStreamParams = TypedDict('TiktokMobileMusicChoicesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileMusicCollectionListDefaultParams = TypedDict('TiktokMobileMusicCollectionListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionListTextResponseParams = TypedDict('TiktokMobileMusicCollectionListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionListStreamParams = TypedDict('TiktokMobileMusicCollectionListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsDefaultParams = TypedDict('TiktokMobileMusicCollectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsTextResponseParams = TypedDict('TiktokMobileMusicCollectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsStreamParams = TypedDict('TiktokMobileMusicCollectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicDetailDefaultParams = TypedDict('TiktokMobileMusicDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicDetailTextResponseParams = TypedDict('TiktokMobileMusicDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicDetailStreamParams = TypedDict('TiktokMobileMusicDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicPickDefaultParams = TypedDict('TiktokMobileMusicPickDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPickTextResponseParams = TypedDict('TiktokMobileMusicPickTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPickStreamParams = TypedDict('TiktokMobileMusicPickStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsDefaultParams = TypedDict('TiktokMobileMusicPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsTextResponseParams = TypedDict('TiktokMobileMusicPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsStreamParams = TypedDict('TiktokMobileMusicPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedDefaultParams = TypedDict('TiktokMobileMusicRelatedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedTextResponseParams = TypedDict('TiktokMobileMusicRelatedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedStreamParams = TypedDict('TiktokMobileMusicRelatedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingDefaultParams = TypedDict('TiktokMobileMusicTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingTextResponseParams = TypedDict('TiktokMobileMusicTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingStreamParams = TypedDict('TiktokMobileMusicTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosDefaultParams = TypedDict('TiktokMobileMvVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosTextResponseParams = TypedDict('TiktokMobileMvVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosStreamParams = TypedDict('TiktokMobileMvVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceDetailDefaultParams = TypedDict('TiktokMobilePlaceDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceDetailTextResponseParams = TypedDict('TiktokMobilePlaceDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceDetailStreamParams = TypedDict('TiktokMobilePlaceDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceInfoDefaultParams = TypedDict('TiktokMobilePlaceInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceInfoTextResponseParams = TypedDict('TiktokMobilePlaceInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceInfoStreamParams = TypedDict('TiktokMobilePlaceInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceMediaDefaultParams = TypedDict('TiktokMobilePlaceMediaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlaceMediaTextResponseParams = TypedDict('TiktokMobilePlaceMediaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlaceMediaStreamParams = TypedDict('TiktokMobilePlaceMediaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlacePhotosDefaultParams = TypedDict('TiktokMobilePlacePhotosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlacePhotosTextResponseParams = TypedDict('TiktokMobilePlacePhotosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlacePhotosStreamParams = TypedDict('TiktokMobilePlacePhotosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceReviewsDefaultParams = TypedDict('TiktokMobilePlaceReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceReviewsTextResponseParams = TypedDict('TiktokMobilePlaceReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceReviewsStreamParams = TypedDict('TiktokMobilePlaceReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceVideosDefaultParams = TypedDict('TiktokMobilePlaceVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceVideosTextResponseParams = TypedDict('TiktokMobilePlaceVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceVideosStreamParams = TypedDict('TiktokMobilePlaceVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistDetailDefaultParams = TypedDict('TiktokMobilePlaylistDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistDetailTextResponseParams = TypedDict('TiktokMobilePlaylistDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistDetailStreamParams = TypedDict('TiktokMobilePlaylistDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistListDefaultParams = TypedDict('TiktokMobilePlaylistListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistListTextResponseParams = TypedDict('TiktokMobilePlaylistListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistListStreamParams = TypedDict('TiktokMobilePlaylistListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosDefaultParams = TypedDict('TiktokMobilePlaylistVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosTextResponseParams = TypedDict('TiktokMobilePlaylistVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosStreamParams = TypedDict('TiktokMobilePlaylistVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchDefaultParams = TypedDict('TiktokMobileSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchTextResponseParams = TypedDict('TiktokMobileSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchResponseStreamParams = TypedDict('TiktokMobileSearchResponseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsDefaultParams = TypedDict('TiktokMobileSearchEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsTextResponseParams = TypedDict('TiktokMobileSearchEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsStreamParams = TypedDict('TiktokMobileSearchEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchHashtagsDefaultParams = TypedDict('TiktokMobileSearchHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchHashtagsTextResponseParams = TypedDict('TiktokMobileSearchHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchHashtagsStreamParams = TypedDict('TiktokMobileSearchHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicDefaultParams = TypedDict('TiktokMobileSearchMusicDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicTextResponseParams = TypedDict('TiktokMobileSearchMusicTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicStreamParams = TypedDict('TiktokMobileSearchMusicStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchPhotosDefaultParams = TypedDict('TiktokMobileSearchPhotosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPhotosTextResponseParams = TypedDict('TiktokMobileSearchPhotosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPhotosStreamParams = TypedDict('TiktokMobileSearchPhotosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPlaceDefaultParams = TypedDict('TiktokMobileSearchPlaceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPlaceTextResponseParams = TypedDict('TiktokMobileSearchPlaceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPlaceStreamParams = TypedDict('TiktokMobileSearchPlaceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoDefaultParams = TypedDict('TiktokMobileSearchPreInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoTextResponseParams = TypedDict('TiktokMobileSearchPreInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoStreamParams = TypedDict('TiktokMobileSearchPreInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchStreamDefaultParams = TypedDict('TiktokMobileSearchStreamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchStreamTextResponseParams = TypedDict('TiktokMobileSearchStreamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchStreamStreamParams = TypedDict('TiktokMobileSearchStreamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchSugDefaultParams = TypedDict('TiktokMobileSearchSugDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchSugTextResponseParams = TypedDict('TiktokMobileSearchSugTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchSugStreamParams = TypedDict('TiktokMobileSearchSugStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchTabsDefaultParams = TypedDict('TiktokMobileSearchTabsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchTabsTextResponseParams = TypedDict('TiktokMobileSearchTabsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchTabsStreamParams = TypedDict('TiktokMobileSearchTabsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchUserDefaultParams = TypedDict('TiktokMobileSearchUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchUserTextResponseParams = TypedDict('TiktokMobileSearchUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchUserStreamParams = TypedDict('TiktokMobileSearchUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchVideosDefaultParams = TypedDict('TiktokMobileSearchVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchVideosTextResponseParams = TypedDict('TiktokMobileSearchVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchVideosStreamParams = TypedDict('TiktokMobileSearchVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionDefaultParams = TypedDict('TiktokMobileTranslationDescriptionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionTextResponseParams = TypedDict('TiktokMobileTranslationDescriptionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionStreamParams = TypedDict('TiktokMobileTranslationDescriptionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTrendingCategoriesDefaultParams = TypedDict('TiktokMobileTrendingCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingCategoriesTextResponseParams = TypedDict('TiktokMobileTrendingCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingCategoriesStreamParams = TypedDict('TiktokMobileTrendingCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsDefaultParams = TypedDict('TiktokMobileTrendingEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsTextResponseParams = TypedDict('TiktokMobileTrendingEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsStreamParams = TypedDict('TiktokMobileTrendingEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersDefaultParams = TypedDict('TiktokMobileUserFollowersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersTextResponseParams = TypedDict('TiktokMobileUserFollowersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersStreamParams = TypedDict('TiktokMobileUserFollowersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingDefaultParams = TypedDict('TiktokMobileUserFollowingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingTextResponseParams = TypedDict('TiktokMobileUserFollowingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingStreamParams = TypedDict('TiktokMobileUserFollowingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsDefaultParams = TypedDict('TiktokMobileUserOriginalEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsTextResponseParams = TypedDict('TiktokMobileUserOriginalEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsStreamParams = TypedDict('TiktokMobileUserOriginalEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicDefaultParams = TypedDict('TiktokMobileUserOriginalMusicDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicTextResponseParams = TypedDict('TiktokMobileUserOriginalMusicTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicStreamParams = TypedDict('TiktokMobileUserOriginalMusicStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserPostsDefaultParams = TypedDict('TiktokMobileUserPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserPostsTextResponseParams = TypedDict('TiktokMobileUserPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserPostsStreamParams = TypedDict('TiktokMobileUserPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserProfileDefaultParams = TypedDict('TiktokMobileUserProfileDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserProfileTextResponseParams = TypedDict('TiktokMobileUserProfileTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserProfileStreamParams = TypedDict('TiktokMobileUserProfileStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserRecommendationsDefaultParams = TypedDict('TiktokMobileUserRecommendationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserRecommendationsTextResponseParams = TypedDict('TiktokMobileUserRecommendationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserRecommendationsStreamParams = TypedDict('TiktokMobileUserRecommendationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileVideoDetailDefaultParams = TypedDict('TiktokMobileVideoDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoDetailTextResponseParams = TypedDict('TiktokMobileVideoDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoDetailStreamParams = TypedDict('TiktokMobileVideoDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesDefaultParams = TypedDict('TiktokMobileVideoSubtitlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesTextResponseParams = TypedDict('TiktokMobileVideoSubtitlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesStreamParams = TypedDict('TiktokMobileVideoSubtitlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)
