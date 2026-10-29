use crawlora_tiktok_mobile::{Client, ModelTiktokmobileFeedResponseDoc, TiktokMobileFeedParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .tiktok_mobile
        .feed(TiktokMobileFeedParams {
            ..Default::default()
        })
        .await?;
    let data: ModelTiktokmobileFeedResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
