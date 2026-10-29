package net.crawlora.tiktok_mobile;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(63, Client.OPERATION_IDS.size());
        assertEquals(List.of("tiktok-mobile-anchor-list", "tiktok-mobile-collection-detail", "tiktok-mobile-collection-list", "tiktok-mobile-collection-videos", "tiktok-mobile-comment-replies", "tiktok-mobile-comments", "tiktok-mobile-feed", "tiktok-mobile-feed-offline", "tiktok-mobile-feed-post", "tiktok-mobile-hashtag", "tiktok-mobile-hashtag-posts", "tiktok-mobile-hashtags", "tiktok-mobile-live-effects", "tiktok-mobile-live-gifts", "tiktok-mobile-live-hashtags", "tiktok-mobile-live-room", "tiktok-mobile-live-room-by-user", "tiktok-mobile-live-search", "tiktok-mobile-live-tabs", "tiktok-mobile-music-beats", "tiktok-mobile-music-chart", "tiktok-mobile-music-choices", "tiktok-mobile-music-collection-list", "tiktok-mobile-music-collections", "tiktok-mobile-music-detail", "tiktok-mobile-music-pick", "tiktok-mobile-music-posts", "tiktok-mobile-music-related", "tiktok-mobile-music-trending", "tiktok-mobile-mv-videos", "tiktok-mobile-place-detail", "tiktok-mobile-place-info", "tiktok-mobile-place-media", "tiktok-mobile-place-photos", "tiktok-mobile-place-reviews", "tiktok-mobile-place-videos", "tiktok-mobile-playlist-detail", "tiktok-mobile-playlist-list", "tiktok-mobile-playlist-videos", "tiktok-mobile-search", "tiktok-mobile-search-effects", "tiktok-mobile-search-hashtags", "tiktok-mobile-search-music", "tiktok-mobile-search-photos", "tiktok-mobile-search-place", "tiktok-mobile-search-pre-info", "tiktok-mobile-search-stream", "tiktok-mobile-search-sug", "tiktok-mobile-search-tabs", "tiktok-mobile-search-user", "tiktok-mobile-search-videos", "tiktok-mobile-translation-description", "tiktok-mobile-trending-categories", "tiktok-mobile-trending-effects", "tiktok-mobile-user-followers", "tiktok-mobile-user-following", "tiktok-mobile-user-original-effects", "tiktok-mobile-user-original-music", "tiktok-mobile-user-posts", "tiktok-mobile-user-profile", "tiktok-mobile-user-recommendations", "tiktok-mobile-video-detail", "tiktok-mobile-video-subtitles"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("tiktok-mobile-collection-detail", Map.ofEntries(Map.entry("collection_id", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            // This operation has no path parameters to encode.
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("collectionDetail", Map.class).invoke(client, Map.ofEntries(Map.entry("collection_id", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("tiktok-mobile-anchor-list", Map.of()));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("tiktok-mobile-collection-detail", Map.ofEntries(Map.entry("collection_id", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("tiktok-mobile-collection-detail", Map.ofEntries(Map.entry("collection_id", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("tiktok-mobile-hashtag-posts", Map.ofEntries(Map.entry("name", "sample"), Map.entry("sort", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("tiktok-mobile-collection-detail", Map.ofEntries(Map.entry("collection_id", "value &/one"))));
    }
}
