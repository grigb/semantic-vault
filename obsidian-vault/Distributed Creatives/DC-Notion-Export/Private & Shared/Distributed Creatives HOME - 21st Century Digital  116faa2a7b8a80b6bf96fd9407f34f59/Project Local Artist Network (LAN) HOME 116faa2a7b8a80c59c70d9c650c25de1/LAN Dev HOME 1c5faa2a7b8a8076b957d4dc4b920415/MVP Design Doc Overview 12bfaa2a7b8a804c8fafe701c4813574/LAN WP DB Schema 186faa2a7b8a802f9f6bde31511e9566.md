# LAN WP DB Schema

### **1. Core Tables**

These tables will store the foundational data for the platform.

| Table Name | Description |
| --- | --- |
| `wp_users` | Default WordPress users table (for user management). |
| `wp_content` | Stores all content types (videos, artwork, events, ads). |
| `wp_content_meta` | Stores additional metadata for content (key-value pairs for flexibility). |
| `wp_categories` | Categories for content (e.g., music, art, theater). |
| `wp_tags` | Tags for content (e.g., jazz, abstract, modern). |
| `wp_schedules` | Stores scheduling information for content display. |
| `wp_venues` | Stores information about venues where content is displayed. |
| `wp_artists` | Stores information about artists/creators. |
| `wp_advertisers` | Stores information about advertisers. |

---

### **2. Table Details**

### **`wp_content`**

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | BIGINT (PK) | Unique ID for the content. |
| `title` | VARCHAR(255) | Title of the content. |
| `slug` | VARCHAR(255) | URL-friendly slug. |
| `type` | ENUM | Content type (video, artwork, event, advertisement). |
| `status` | ENUM | Content status (active, inactive, scheduled). |
| `created_at` | DATETIME | Timestamp when the content was created. |
| `updated_at` | DATETIME | Timestamp when the content was last updated. |
| `author_id` | BIGINT | ID of the user who created the content (foreign key to `wp_users`). |
| `thumbnail_url` | VARCHAR(255) | URL of the thumbnail image. |
| `description` | TEXT | Description of the content. |

### **`wp_content_meta`**

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | BIGINT (PK) | Unique ID for the metadata entry. |
| `content_id` | BIGINT | Foreign key to `wp_content`. |
| `meta_key` | VARCHAR(255) | Key for the metadata (e.g., `duration`, `artist_name`, `event_date`). |
| `meta_value` | TEXT | Value for the metadata. |

### **`wp_schedules`**

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | BIGINT (PK) | Unique ID for the schedule. |
| `content_id` | BIGINT | Foreign key to `wp_content`. |
| `start_time` | DATETIME | Start time for the content display. |
| `end_time` | DATETIME | End time for the content display. |
| `frequency` | VARCHAR(50) | Frequency of display (e.g., hourly, daily). |
| `venue_id` | BIGINT | Foreign key to `wp_venues`. |

### **`wp_artists`**

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | BIGINT (PK) | Unique ID for the artist. |
| `name` | VARCHAR(255) | Name of the artist. |
| `bio` | TEXT | Biography of the artist. |
| `profile_image_url` | VARCHAR(255) | URL of the artist's profile image. |
| `website_url` | VARCHAR(255) | URL of the artist's website. |

### **`wp_advertisers`**

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | BIGINT (PK) | Unique ID for the advertiser. |
| `name` | VARCHAR(255) | Name of the advertiser. |
| `contact_email` | VARCHAR(255) | Contact email for the advertiser. |
| `logo_url` | VARCHAR(255) | URL of the advertiser's logo. |

---

---