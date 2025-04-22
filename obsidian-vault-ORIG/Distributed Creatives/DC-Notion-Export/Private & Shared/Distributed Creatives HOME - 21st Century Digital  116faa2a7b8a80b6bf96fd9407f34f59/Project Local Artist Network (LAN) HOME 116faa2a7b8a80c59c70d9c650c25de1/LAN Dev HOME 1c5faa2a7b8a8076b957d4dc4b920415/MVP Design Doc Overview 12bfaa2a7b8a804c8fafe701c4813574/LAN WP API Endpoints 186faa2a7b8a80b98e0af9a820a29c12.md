# LAN WP API Endpoints

The WordPress REST API will serve as the backend for the React frontend. Here are the key endpoints:

### **Content Endpoints**

- `GET /lan/v1/content`
    
    Fetch all content with filters (e.g., type, status, category).
    
- `GET /lan/v1/content/{id}`
    
    Fetch a single content item by ID.
    
- `POST /lan/v1/content`
    
    Create new content.
    
- `PUT /lan/v1/content/{id}`
    
    Update existing content.
    
- `DELETE /lan/v1/content/{id}`
    
    Delete content.
    

### **Schedule Endpoints**

- `GET /lan/v1/schedules`
    
    Fetch all schedules.
    
- `POST /lan/v1/schedules`
    
    Create a new schedule.
    

### **Artist Endpoints**

- `GET /lan/v1/artists`
    
    Fetch all artists.
    
- `GET /lan/v1/artists/{id}`
    
    Fetch a single artist by ID.
    

### **Advertiser Endpoints**

- `GET /lan/v1/advertisers`
    
    Fetch all advertisers.