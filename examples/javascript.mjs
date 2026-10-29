import { TikTokMobileClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new TikTokMobileClient({ apiKey });

  const feed = await client.feed({  });
  console.log("feed", feed);
  const searchSug = await client.searchSug({ keyword: "science" });
  console.log("searchSug", searchSug);
