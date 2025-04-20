use serde::{Deserialize, Serialize};
use reqwest::Client;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct SearchRequest {
    pub query: String,
    pub group_id: String,
    pub max_facts: usize,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct SearchResult {
    pub title: String,
    pub summary: String,
    pub link: Option<String>,
    pub uuid: String,
}

pub async fn search_backend(
    client: &Client,
    backend_url: &str,
    request: &SearchRequest,
) -> Result<Vec<SearchResult>, String> {
    let resp = client
        .post(backend_url)
        .json(request)
        .send()
        .await
        .map_err(|e| format!("HTTP error: {}", e))?;
    if !resp.status().is_success() {
        return Err(format!("Backend error: {}", resp.status()));
    }
    let json: serde_json::Value = resp.json().await.map_err(|e| format!("JSON error: {}", e))?;
    // Parse results (adapt as needed to actual API response)
    let mut results = Vec::new();
    if let Some(arr) = json.get("facts").and_then(|v| v.as_array()) {
        for fact in arr {
            let title = fact.get("name").and_then(|v| v.as_str()).unwrap_or("").to_string();
            let summary = fact.get("fact").and_then(|v| v.as_str()).unwrap_or("").to_string();
            let link = fact.get("file_path").and_then(|v| v.as_str()).map(|s| s.to_string());
            let uuid = fact.get("uuid").and_then(|v| v.as_str()).unwrap_or("").to_string();
            results.push(SearchResult { title, summary, link, uuid });
        }
    }
    Ok(results)
}
