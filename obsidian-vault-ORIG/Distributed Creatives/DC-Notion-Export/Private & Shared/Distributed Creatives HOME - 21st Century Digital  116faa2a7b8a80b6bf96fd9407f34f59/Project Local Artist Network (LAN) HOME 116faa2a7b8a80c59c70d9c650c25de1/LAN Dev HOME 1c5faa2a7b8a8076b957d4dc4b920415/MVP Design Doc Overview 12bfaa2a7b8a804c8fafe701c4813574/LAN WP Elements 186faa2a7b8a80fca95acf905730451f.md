# LAN WP Elements

### **Custom Post Types (CPTs)**

Here are the CPTs I recommend for your LAN platform:

### **1. `lan_content`**

This CPT will handle all types of content (videos, artwork, events, advertisements).

| Field | Description |
| --- | --- |
| `post_title` | Title of the content (e.g., "Summer Art Festival Promo"). |
| `post_content` | Description or details of the content. |
| `post_type` | Set to `lan_content`. |
| `post_status` | Status of the content (e.g., `publish`, `draft`, `pending`). |
| `post_author` | ID of the user who created the content. |
| `thumbnail` | Featured image (thumbnail) for the content. |

### **2. `lan_artist`**

This CPT will store information about artists.

| Field | Description |
| --- | --- |
| `post_title` | Name of the artist (e.g., "Jane Smith"). |
| `post_content` | Biography or description of the artist. |
| `post_type` | Set to `lan_artist`. |
| `post_status` | Status of the artist profile (e.g., `publish`, `draft`). |
| `thumbnail` | Profile image of the artist. |

### **3. `lan_venue`**

This CPT will store information about venues.

| Field | Description |
| --- | --- |
| `post_title` | Name of the venue (e.g., "Downtown Art Gallery"). |
| `post_content` | Description or details about the venue. |
| `post_type` | Set to `lan_venue`. |
| `post_status` | Status of the venue profile (e.g., `publish`, `draft`). |
| `thumbnail` | Image of the venue. |

### **4. `lan_advertiser`**

This CPT will store information about advertisers.

| Field | Description |
| --- | --- |
| `post_title` | Name of the advertiser (e.g., "Local Coffee Shop"). |
| `post_content` | Description or details about the advertiser. |
| `post_type` | Set to `lan_advertiser`. |
| `post_status` | Status of the advertiser profile (e.g., `publish`, `draft`). |
| `thumbnail` | Logo of the advertiser. |

---

### **Advanced Custom Fields (ACF)**

ACF will allow you to add custom fields to your CPTs dynamically. Here are the fields I recommend for each CPT:

### **1. `lan_content` Fields**

| Field Name | Field Type | Description |
| --- | --- | --- |
| `content_type` | Select | Type of content (e.g., video, artwork, event, advertisement). |
| `duration` | Number | Duration of the content (in seconds). |
| `artist` | Relationship | Link to the `lan_artist` CPT (for artist attribution). |
| `venue` | Relationship | Link to the `lan_venue` CPT (for event location). |
| `start_date` | Date Picker | Start date for events or advertisements. |
| `end_date` | Date Picker | End date for events or advertisements. |
| `status` | Select | Status of the content (e.g., active, inactive, scheduled). |
| `external_link` | URL | Link to external content (e.g., ticket purchase page). |
| `categories` | Taxonomy | Link to categories (e.g., music, art, theater). |
| `tags` | Taxonomy | Link to tags (e.g., jazz, abstract, modern). |

### **2. `lan_artist` Fields**

| Field Name | Field Type | Description |
| --- | --- | --- |
| `artist_type` | Select | Type of artist (e.g., painter, musician, sculptor). |
| `website_url` | URL | Link to the artist's website. |
| `social_media` | Repeater | Social media links (platform, URL). |
| `contact_email` | Email | Contact email for the artist. |

### **3. `lan_venue` Fields**

| Field Name | Field Type | Description |
| --- | --- | --- |
| `address` | Text | Physical address of the venue. |
| `capacity` | Number | Maximum capacity of the venue. |
| `venue_type` | Select | Type of venue (e.g., indoor, outdoor, hybrid). |
| `contact_email` | Email | Contact email for the venue. |

### **4. `lan_advertiser` Fields**

| Field Name | Field Type | Description |
| --- | --- | --- |
| `contact_email` | Email | Contact email for the advertiser. |
| `ad_type` | Select | Type of advertisement (e.g., brand awareness, event promotion). |
| `target_audience` | Text | Target audience for the advertisement. |
| `budget` | Number | Budget for the advertisement campaign. |