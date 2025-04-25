use rust_frontend_app::search::{search_backend, SearchRequest};
use reqwest::Client;

#[tokio::test]
async fn test_search_backend_returns_results() {
    // Assumes backend is running on localhost:8000
    let client = Client::new();
    let request = SearchRequest {
        query: "local artist network".to_string(),
        group_id: "notion".to_string(),
        max_facts: 3,
    };
    let backend_url = "http://localhost:9003/search";
    let result = search_backend(&client, backend_url, &request).await;
    assert!(result.is_ok(), "Expected Ok(_), got {:?}", result);
    let results = result.unwrap();
    assert!(!results.is_empty(), "Expected non-empty results");
    for r in results {
        println!("Result: {} | {}", r.title, r.summary);
        assert!(!r.title.is_empty());
        assert!(!r.summary.is_empty());
    }
}
