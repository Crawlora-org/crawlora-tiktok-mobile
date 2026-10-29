import { TikTokMobileClient } from "../src/index.js";

const client = new TikTokMobileClient({ apiKey: "test-key" });
void client.collectionDetail({"collection_id": "sample"});
void client.request("tiktok-mobile-collection-detail", {"collection_id": "sample"});
const streamResponse: Promise<Response> = client.request("tiktok-mobile-collection-detail", {"collection_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("tiktok-mobile-collection-detail", {"collection_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.collectionDetail({"collection_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("tiktok-mobile-collection-detail", {"collection_id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("tiktok-mobile-collection-detail", {"collection_id": "sample"}, { responseType: "text" });
void rawText;


void client.anchorList();
void client.request("tiktok-mobile-anchor-list");
// @ts-expect-error The selected operation requires its documented params.
void client.collectionDetail();
