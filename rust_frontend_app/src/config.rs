use std::fs;
use std::path::PathBuf;
use serde::{Serialize, Deserialize};
use directories::ProjectDirs;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct AppConfig {
    pub backend_url: String,
    pub group_id: String,
}

impl Default for AppConfig {
    fn default() -> Self {
        Self {
            backend_url: "http://localhost:9003/search".to_string(),
            group_id: "notion".to_string(),
        }
    }
}

impl AppConfig {
    pub fn config_path() -> PathBuf {
        if let Some(proj_dirs) = ProjectDirs::from("org", "distributedcreatives", "GraphitiRustApp") {
            let dir = proj_dirs.config_dir();
            fs::create_dir_all(dir).ok();
            dir.join("config.json")
        } else {
            PathBuf::from("./config.json")
        }
    }

    pub fn load() -> Self {
        let path = Self::config_path();
        if path.exists() {
            let data = fs::read_to_string(&path).unwrap_or_default();
            serde_json::from_str(&data).unwrap_or_default()
        } else {
            Self::default()
        }
    }

    pub fn save(&self) {
        let path = Self::config_path();
        let data = serde_json::to_string_pretty(self).unwrap();
        fs::write(path, data).ok();
    }
}
