# LAN Ad Analytics & Impression Tracking System

## **1. Overview**

This system will track **impressions** across **digital signage, website views, and Smart TV views** while providing granular control over **location-based analytics, primetime settings, QR code scans, and user engagement**. Additionally, the system will support **Promo Accounts** for advertisers to manage content visibility and performance.

---

## **2. Key Features**

### **A. Impression Tracking**

- **Total Impressions**: Count every instance a piece of content is displayed.
- **Unique Impressions**: Track unique viewers per device/location/session.
- **Time-Based Estimation**: Calculate impressions based on:
    - Screen time (rotation logic)
    - Audience estimation (traffic multiplier)
    - Real-time detection (if using cameras or sensors)
- **Primetime vs. Non-Primetime**:
    - Customizable **primetime slots** (admin-defined).
    - Different **weighting for impressions** based on viewership estimates.

### **B. Location-Based Analytics**

- Track **each digital signage screen separately**.
- Support **multiple screens per location**.
- Assign **expected foot traffic** to each location.
- Allow **real-time reporting** from connected screens.

### **C. Multi-Platform Tracking**

- **Digital Signage Views** (tracked per screen).
- **Website Views** (via embedded content tracking).
- **Smart TV Views** (via app-based tracking or logs).

### **D. QR Code Tracking**

- Every **piece of content** includes a **QR code**.
- **Track total QR scans** per content item.
- **Store metadata** for QR scans:
    - **Time of scan**
    - **Location of the signage**
    - **Device type** (if accessible)
- **Redirect users** to a website or landing page.
- **Track conversions** (e.g., sign-ups, purchases) on the remote website.

---

## **3. Admin Interface Specifications**

### **A. Dashboard**

- **Global Overview:**
    - Total impressions (segmented by platform).
    - Unique impressions.
    - Primetime vs. Non-Primetime breakdown.
    - Top locations & screens.
    - QR Code Scan Metrics.
    - Remote Action Tracking.
- **Per-Content Analytics:**
    - View impressions per **content piece**.
    - Breakdown by **location, device type, and time**.
    - **Track QR scans** and **website interactions**.

### **B. Promo Accounts (Advertisers)**

**Promo Accounts** will allow advertisers to:

- **Create and manage** promo content.
- **Set campaign budgets** for impression-based distribution.
- **Define scheduling** for specific time periods.
- **Target locations** based on foot traffic.
- **View performance analytics**, including:
    - Impressions (Digital Signage, Web, Smart TV).
    - QR Code Scans.
    - Conversion Events on their linked website.

### **C. QR Code & Remote Action Tracking**

- **Admin Panel:**
    - Track **total QR scans per campaign**.
    - View scans **by location, time, and device type**.
- **Remote Action Tracking:**
    - Use **UTM parameters** or **unique identifiers** in QR URLs.
    - Detect and **record user actions** on the destination website.
    - Actions include:
        - **Sign-ups**
        - **Purchases**
        - **Downloads**
        - **Other custom engagement metrics**
    - If using a **JavaScript tracker**, the website can **send engagement data** back to the system.

### **D. Location Management**

- **Add/Edit/Delete Locations**
- Assign:
    - **Screens to locations** (1-to-many relationship).
    - **Expected traffic data** (foot traffic estimation).
    - **Primetime hours per location**.

### **E. Impression Settings**

- **Primetime & Non-Primetime Customization**
    - Set primetime hours per location.
    - Set **impression weight for primetime** vs. non-primetime.
    - Example: If **primetime = 6 PM - 10 PM**, impressions could count as **1.5x normal weight**.
- **Impression Calculation Model**
    - Choose from:
        - **Time-Based (Fixed Rotation)**
        - **AI Estimation (if sensors available)**
        - **WiFi/Bluetooth-Based Tracking** (if devices detected nearby)
        - **QR Code & Click Engagement Data**

### **F. Multi-Platform Tracking**

- **Digital Signage**:
    - Logged per display.
    - Uses **time-based or sensor-based tracking**.
- **Website Views**:
    - Track embedded views **via JavaScript beacon**.
    - Capture **session details & engagement**.
- **Smart TV Views**:
    - Tracked via **log-based reporting**.
    - **Session analytics** stored per app instance.

---

## **4. Impression Goal Calculation**

To ensure a piece of content meets its **total impression goal** within its **scheduled start and end dates**, the system will calculate **required daily impressions** dynamically.

### **A. Formula for Daily Impressions**

Required Daily Impressions=Total Impressions GoalScheduled Days\text{Required Daily Impressions} = \frac{\text{Total Impressions Goal}}{\text{Scheduled Days}}

Where:

- **Total Impressions Goal**: Admin-set number of required views.
- **Scheduled Days**: The number of days between **start and end date**.

### **B. Adjustments for Primetime & Location-Specific Factors**

1. **Primetime Weighting**:
    - Example: If **primetime multiplier = 1.5x**, then:
        
        Adjusted Primetime Views=Total Primetime Slots×1.5\text{Adjusted Primetime Views} = \text{Total Primetime Slots} \times 1.5
        
    - The system will **prioritize impressions during primetime** if not enough impressions are reached.
2. **Location Traffic Multiplier**:
    - Each signage **location has an expected foot traffic estimate**.
    - If traffic is **lower than expected**, impressions will redistribute across **other locations** or **website/Smart TV views**.

---

## **5. Data & Reporting API**

A **REST API** for integration with dashboards, ad platforms, and analytics tools.

### **API Endpoints**

- `GET /impressions` → Fetch total/unique impressions.
- `GET /locations` → Retrieve list of signage locations.
- `GET /content/:id/impressions` → Fetch impressions per content item.
- `POST /admin/settings/primetime` → Update primetime values.
- `POST /admin/settings/traffic-multiplier` → Update foot traffic estimates.
- `GET /content/:id/daily-impression-target` → Fetch required daily impressions.
- `GET /content/:id/qr-scans` → Fetch total QR scans for a content item.
- `GET /promo-accounts/:id/performance` → Fetch an advertiser's campaign performance.
- `POST /track-remote-action` → Log user actions on a remote website.

---

## **6. Expansion Possibilities**

- **Automated Scheduling Adjustments**: If a campaign is underperforming, the system **increases its rotation frequency** dynamically.
- **Promo Account Tiers**: Allow different pricing models based on reach.
- **AI-Powered Traffic Estimation**: Integrate **foot traffic sensors**.
- **Real-Time Heatmaps**: Show **content engagement** across locations.

---

This spec ensures **each content piece meets its impression goal**, dynamically **adjusting for real-world viewership trends**, while **tracking QR code engagement and advertiser performance**.

```jsx
import React, { useState } from 'react';
import { 
  LineChart, BarChart, PieChart, ResponsiveContainer, 
  Line, Bar, Pie, XAxis, YAxis, CartesianGrid, Tooltip, Legend 
} from 'recharts';
import { 
  LayoutDashboard, Users, MapPin, Clock, Settings,
  TrendingUp, QrCode, Radio, Monitor, Smartphone,
  Calendar, Image, BarChart3
} from 'lucide-react';

// Main Navigation Items
const MENU_ITEMS = [
  {
    id: 'analytics',
    icon: LayoutDashboard,
    label: 'Content Analytics',
    subItems: [
      { id: 'overview', label: 'Aesthetic Overview' },
      { id: 'platform-metrics', label: 'Platform Metrics' },
      { id: 'engagement', label: 'Engagement Analytics' }
    ]
  },
  {
    id: 'promo',
    icon: TrendingUp,
    label: 'Promo Dashboard',
    subItems: [
      { id: 'campaigns', label: 'Active Campaigns' },
      { id: 'performance', label: 'Performance Metrics' },
      { id: 'scheduling', label: 'Campaign Scheduling' }
    ]
  },
  {
    id: 'qr',
    icon: QrCode,
    label: 'QR Analytics',
    subItems: [
      { id: 'scan-metrics', label: 'Scan Metrics' },
      { id: 'location-data', label: 'Location Data' },
      { id: 'conversions', label: 'Conversion Tracking' }
    ]
  }
];

// Admin-only menu items
const ADMIN_MENU_ITEMS = [
  {
    id: 'settings',
    icon: Settings,
    label: 'Admin Settings',
    subItems: [
      { id: 'primetime', label: 'Primetime Configuration' },
      { id: 'locations', label: 'Location Management' },
      { id: 'traffic', label: 'Traffic Estimation' },
      { id: 'platform', label: 'Platform Settings' }
    ]
  }
];

const MainNavigation = ({ activeView, setActiveView, isAdmin }) => (
  <nav className="w-64 bg-white shadow-sm p-4 border-r">
    <div className="space-y-6">
      <h1 className="text-xl font-bold">Local Artist Network</h1>
      
      {/* Regular Menu Items */}
      {MENU_ITEMS.map(item => (
        <div key={item.id} className="space-y-2">
          <div className="flex items-center text-sm font-medium text-gray-600">
            <item.icon className="mr-2" size={16} />
            {item.label}
          </div>
          <div className="pl-6 space-y-1">
            {item.subItems.map(subItem => (
              <button
                key={subItem.id}
                onClick={() => setActiveView(subItem.id)}
                className={`w-full text-left px-2 py-1 text-sm rounded transition-colors ${
                  activeView === subItem.id 
                    ? 'bg-blue-50 text-blue-600' 
                    : 'text-gray-600 hover:bg-gray-100'
                }`}
              >
                {subItem.label}
              </button>
            ))}
          </div>
        </div>
      ))}

      {/* Admin-only Menu Items */}
      {isAdmin && (
        <>
          <div className="border-t my-4" />
          {ADMIN_MENU_ITEMS.map(item => (
            <div key={item.id} className="space-y-2">
              <div className="flex items-center text-sm font-medium text-gray-600">
                <item.icon className="mr-2" size={16} />
                {item.label}
              </div>
              <div className="pl-6 space-y-1">
                {item.subItems.map(subItem => (
                  <button
                    key={subItem.id}
                    onClick={() => setActiveView(subItem.id)}
                    className={`w-full text-left px-2 py-1 text-sm rounded transition-colors ${
                      activeView === subItem.id 
                        ? 'bg-blue-50 text-blue-600' 
                        : 'text-gray-600 hover:bg-gray-100'
                    }`}
                  >
                    {subItem.label}
                  </button>
                ))}
              </div>
            </div>
          ))}
        </>
      )}
    </div>
  </nav>
);

// Admin Settings Components
const AdminSettings = ({ view }) => {
  switch (view) {
    case 'primetime':
      return (
        <div className="p-6 space-y-6">
          <h2 className="text-2xl font-bold">Primetime Configuration</h2>
          
          {/* Primetime Slots */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-bold mb-4">Primetime Slots</h3>
            <div className="space-y-4">
              {/* Global Primetime Settings */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">Default Start Time</label>
                  <input type="time" className="w-full border rounded p-2" />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Default End Time</label>
                  <input type="time" className="w-full border rounded p-2" />
                </div>
              </div>
              
              {/* Impression Weights */}
              <div>
                <label className="block text-sm font-medium mb-1">Primetime Weight Multiplier</label>
                <input 
                  type="number" 
                  step="0.1" 
                  className="w-32 border rounded p-2" 
                  placeholder="1.5"
                />
              </div>
            </div>
          </div>

          {/* Location-specific Overrides */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-bold mb-4">Location-Specific Settings</h3>
            <div className="space-y-4">
              {['Downtown Gallery', 'Arts District', 'City Museum'].map(location => (
                <div key={location} className="border-b pb-4">
                  <h4 className="font-medium mb-2">{location}</h4>
                  <div className="grid grid-cols-3 gap-4">
                    <div>
                      <label className="block text-sm text-gray-500">Custom Start Time</label>
                      <input type="time" className="border rounded p-2" />
                    </div>
                    <div>
                      <label className="block text-sm text-gray-500">Custom End Time</label>
                      <input type="time" className="border rounded p-2" />
                    </div>
                    <div>
                      <label className="block text-sm text-gray-500">Weight Multiplier</label>
                      <input type="number" step="0.1" className="border rounded p-2" />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );

    case 'traffic':
      return (
        <div className="p-6 space-y-6">
          <h2 className="text-2xl font-bold">Traffic Estimation Settings</h2>
          
          {/* Estimation Method */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-bold mb-4">Estimation Method</h3>
            <div className="space-y-4">
              <select className="w-full border rounded p-2">
                <option value="time">Time-Based (Fixed Rotation)</option>
                <option value="ai">AI Estimation (Camera Sensors)</option>
                <option value="wifi">WiFi/Bluetooth Detection</option>
                <option value="hybrid">Hybrid (Multiple Methods)</option>
              </select>
              
              <div className="text-sm text-gray-500">
                Selected method will be used for calculating impression weights
              </div>
            </div>
          </div>

          {/* Location Traffic Settings */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-bold mb-4">Location Traffic Configuration</h3>
            <div className="space-y-4">
              {['Downtown Gallery', 'Arts District', 'City Museum'].map(location => (
                <div key={location} className="border-b pb-4">
                  <h4 className="font-medium mb-2">{location}</h4>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm text-gray-500">Average Daily Traffic</label>
                      <input type="number" className="border rounded p-2" placeholder="500" />
                    </div>
                    <div>
                      <label className="block text-sm text-gray-500">Peak Hours Multiplier</label>
                      <input type="number" step="0.1" className="border rounded p-2" placeholder="1.5" />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );

    default:
      return null;
  }
};

const DashboardLayout = () => {
  const [activeView, setActiveView] = useState('overview');
  const isAdmin = true; // This would come from your auth context

  return (
    <div className="flex h-screen bg-gray-100">
      <MainNavigation 
        activeView={activeView} 
        setActiveView={setActiveView} 
        isAdmin={isAdmin} 
      />
      
      <main className="flex-1 overflow-auto">
        {activeView.startsWith('primetime') || activeView.startsWith('traffic') ? (
          <AdminSettings view={activeView} />
        ) : (
          // Your existing dashboard content components would render here
          // based on the activeView state
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-6">
              {MENU_ITEMS.find(item => 
                item.subItems.some(sub => sub.id === activeView)
              )?.subItems.find(sub => sub.id === activeView)?.label || 
              'Dashboard'}
            </h2>
            {/* Render your existing dashboard content here */}
          </div>
        )}
      </main>
    </div>
  );
};

export default DashboardLayout;
```

![image.png](LAN%20Ad%20Analytics%20&%20Impression%20Tracking%20System%2018dfaa2a7b8a8016b2a4ef4d6ce7b1b9/image.png)

- Overview tab code
    
    
    ```jsx
    import React, { useState, useEffect } from 'react';
    import { 
      LineChart, Line, BarChart, Bar, PieChart, Pie, AreaChart, Area,
      XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
      Cell // Added Cell to imports
    } from 'recharts';
    import { 
      LayoutDashboard, TrendingUp, QrCode, Settings,
      Monitor, Radio, Smartphone, Users, Clock, Calendar,
      AlertCircle, ArrowUp, ArrowDown
    } from 'lucide-react';
    
    // Color palette for consistent usage
    const COLORS = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b'];
    
    // Mock Data Generators
    const generateViewData = (days = 30) => {
      return Array.from({ length: days }, (_, i) => ({
        date: new Date(Date.now() - (days - i) * 24 * 60 * 60 * 1000)
          .toISOString().split('T')[0],
        digitalSignage: Math.floor(Math.random() * 1000) + 500,
        webViews: Math.floor(Math.random() * 800) + 300,
        smartTv: Math.floor(Math.random() * 600) + 200,
      }));
    };
    
    const generateLocationData = () => [
      { name: 'Downtown', value: 400, screens: 3 },
      { name: 'Art Gallery', value: 300, screens: 2 },
      { name: 'Museum', value: 250, screens: 2 },
      { name: 'Train Station', value: 200, screens: 1 },
    ];
    
    // Stat Card Component
    const StatCard = ({ title, value, trend, trendValue, icon: Icon, color }) => (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex justify-between items-start">
          <div>
            <p className="text-gray-500">{title}</p>
            <p className="text-2xl font-bold">{value.toLocaleString()}</p>
            <p className={`text-sm flex items-center ${
              trend === 'up' ? 'text-green-500' : 'text-red-500'
            }`}>
              {trend === 'up' ? (
                <ArrowUp size={16} className="mr-1" />
              ) : (
                <ArrowDown size={16} className="mr-1" />
              )}
              {trendValue}% vs last week
            </p>
          </div>
          <Icon className={`text-${color}-500`} />
        </div>
      </div>
    );
    
    // Overview Tab Component
    const OverviewTab = () => {
      const [viewData, setViewData] = useState(generateViewData());
      const [locationData] = useState(generateLocationData());
      const [isLoading, setIsLoading] = useState(true);
    
      useEffect(() => {
        const timer = setTimeout(() => setIsLoading(false), 1000);
        return () => clearTimeout(timer);
      }, []);
    
      if (isLoading) {
        return (
          <div className="flex items-center justify-center h-full">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500" />
          </div>
        );
      }
    
      return (
        <div className="space-y-6 p-6">
          {/* Platform Stats */}
          <div className="grid grid-cols-3 gap-4">
            <StatCard
              title="Digital Signage"
              value={45231}
              trend="up"
              trendValue={12}
              icon={Monitor}
              color="blue"
            />
            <StatCard
              title="Web Views"
              value={32845}
              trend="up"
              trendValue={8}
              icon={Radio}
              color="purple"
            />
            <StatCard
              title="Smart TV"
              value={18632}
              trend="down"
              trendValue={3}
              icon={Smartphone}
              color="green"
            />
          </div>
    
          {/* View Trends Chart */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold mb-4">View Trends</h3>
            <div className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={viewData}>
                  <defs>
                    {COLORS.map((color, index) => (
                      <linearGradient
                        key={`gradient-${index}`}
                        id={`color${index}`}
                        x1="0" y1="0" x2="0" y2="1"
                      >
                        <stop offset="5%" stopColor={color} stopOpacity={0.8}/>
                        <stop offset="95%" stopColor={color} stopOpacity={0}/>
                      </linearGradient>
                    ))}
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="date" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Area
                    type="monotone"
                    dataKey="digitalSignage"
                    stroke={COLORS[0]}
                    fillOpacity={1}
                    fill={`url(#color0)`}
                    name="Digital Signage"
                  />
                  <Area
                    type="monotone"
                    dataKey="webViews"
                    stroke={COLORS[1]}
                    fillOpacity={1}
                    fill={`url(#color1)`}
                    name="Web Views"
                  />
                  <Area
                    type="monotone"
                    dataKey="smartTv"
                    stroke={COLORS[2]}
                    fillOpacity={1}
                    fill={`url(#color2)`}
                    name="Smart TV"
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>
    
          {/* Location Distribution */}
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold mb-4">Location Distribution</h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={locationData}
                      dataKey="value"
                      nameKey="name"
                      cx="50%"
                      cy="50%"
                      outerRadius={80}
                      label
                    >
                      {locationData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>
    
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold mb-4">Location Details</h3>
              <div className="space-y-4">
                {locationData.map((location, index) => (
                  <div key={location.name} className="flex justify-between items-center">
                    <div className="flex items-center">
                      <div 
                        className="w-3 h-3 rounded-full mr-2" 
                        style={{ backgroundColor: COLORS[index % COLORS.length] }}
                      />
                      <div>
                        <p className="font-medium">{location.name}</p>
                        <p className="text-sm text-gray-500">{location.screens} screens</p>
                      </div>
                    </div>
                    <p className="text-lg font-medium">{location.value.toLocaleString()}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      );
    };
    
    // Tab Navigation Component
    const TabNavigation = ({ activeTab, onTabChange }) => {
      const tabs = [
        { id: 'overview', label: 'Overview', icon: LayoutDashboard },
        { id: 'promo', label: 'Promo Analytics', icon: TrendingUp },
        { id: 'qr', label: 'QR Analytics', icon: QrCode },
        { id: 'settings', label: 'Settings', icon: Settings },
      ];
    
      return (
        <div className="border-b border-gray-200">
          <div className="flex space-x-4 p-4">
            {tabs.map(tab => (
              <button
                key={tab.id}
                onClick={() => onTabChange(tab.id)}
                className={`flex items-center px-4 py-2 rounded-lg transition-colors ${
                  activeTab === tab.id
                    ? 'bg-blue-50 text-blue-600'
                    : 'text-gray-600 hover:bg-gray-50'
                }`}
              >
                <tab.icon className="w-5 h-5 mr-2" />
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      );
    };
    
    // Placeholder components for other tabs
    const PromoTab = () => (
      <div className="p-6">
        <h2 className="text-2xl font-bold">Promo Analytics</h2>
        {/* Add promo content */}
      </div>
    );
    
    const QRTab = () => (
      <div className="p-6">
        <h2 className="text-2xl font-bold">QR Analytics</h2>
        {/* Add QR content */}
      </div>
    );
    
    const SettingsTab = () => (
      <div className="p-6">
        <h2 className="text-2xl font-bold">Settings</h2>
        {/* Add settings content */}
      </div>
    );
    
    // Main Dashboard Component
    const Dashboard = () => {
      const [activeTab, setActiveTab] = useState('overview');
    
      const renderActiveTab = () => {
        switch (activeTab) {
          case 'overview':
            return <OverviewTab />;
          case 'promo':
            return <PromoTab />;
          case 'qr':
            return <QRTab />;
          case 'settings':
            return <SettingsTab />;
          default:
            return <OverviewTab />;
        }
      };
    
      return (
        <div className="min-h-screen bg-gray-100">
          <TabNavigation activeTab={activeTab} onTabChange={setActiveTab} />
          <div className="container mx-auto">
            {renderActiveTab()}
          </div>
        </div>
      );
    };
    
    export default Dashboard;
    ```
    

![image.png](LAN%20Ad%20Analytics%20&%20Impression%20Tracking%20System%2018dfaa2a7b8a8016b2a4ef4d6ce7b1b9/image%201.png)

- Promo analytics code
    
    ```jsx
    import React, { useState, useEffect } from 'react';
    import { 
      LineChart, Line, BarChart, Bar, PieChart, Pie,
      XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer 
    } from 'recharts';
    import { 
      TrendingUp, Users, Clock, Calendar, Target, ArrowUp, 
      ArrowDown, Activity 
    } from 'lucide-react';
    
    const COLORS = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b'];
    
    // Mock Data Generator
    const generateCampaignData = () => ({
      active: [
        {
          id: 1,
          name: 'Summer Arts Festival',
          status: 'active',
          impressions: 45200,
          target: 100000,
          budget: 5000,
          spent: 2300,
          startDate: '2024-06-01',
          endDate: '2024-08-31',
          locations: ['Downtown', 'Arts District'],
          performance: Array.from({ length: 30 }, (_, i) => ({
            date: new Date(Date.now() - (30 - i) * 24 * 60 * 60 * 1000)
              .toISOString().split('T')[0],
            impressions: Math.floor(Math.random() * 2000) + 1000,
            engagement: Math.floor(Math.random() * 500) + 200
          }))
        },
        {
          id: 2,
          name: 'Local Artist Spotlight',
          status: 'active',
          impressions: 28300,
          target: 50000,
          budget: 3000,
          spent: 1800,
          startDate: '2024-05-15',
          endDate: '2024-07-15',
          locations: ['Museum Quarter', 'Arts District'],
          performance: Array.from({ length: 30 }, (_, i) => ({
            date: new Date(Date.now() - (30 - i) * 24 * 60 * 60 * 1000)
              .toISOString().split('T')[0],
            impressions: Math.floor(Math.random() * 1500) + 800,
            engagement: Math.floor(Math.random() * 400) + 150
          }))
        }
      ],
      scheduled: [
        {
          id: 3,
          name: 'Fall Exhibition Series',
          status: 'scheduled',
          target: 75000,
          budget: 4500,
          startDate: '2024-09-01',
          endDate: '2024-11-30',
          locations: ['Downtown', 'Museum Quarter']
        }
      ]
    });
    
    const MetricCard = ({ title, value, trend, trendValue, icon: Icon }) => (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex justify-between items-start">
          <div>
            <p className="text-gray-500">{title}</p>
            <p className="text-2xl font-bold">
              {typeof value === 'number' ? value.toLocaleString() : value}
            </p>
            {trend && (
              <p className={`text-sm flex items-center ${
                trend === 'up' ? 'text-green-500' : 'text-red-500'
              }`}>
                {trend === 'up' ? (
                  <ArrowUp size={16} className="mr-1" />
                ) : (
                  <ArrowDown size={16} className="mr-1" />
                )}
                {trendValue}% vs last period
              </p>
            )}
          </div>
          <Icon className="text-blue-500" size={24} />
        </div>
      </div>
    );
    
    const TimeRangeSelector = ({ selected, onChange }) => (
      <div className="flex justify-end space-x-2 mb-6">
        {['24h', '7d', '30d', '90d'].map(range => (
          <button
            key={range}
            onClick={() => onChange(range)}
            className={`px-4 py-2 rounded-lg transition-colors ${
              selected === range
                ? 'bg-blue-500 text-white'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-600'
            }`}
          >
            {range}
          </button>
        ))}
      </div>
    );
    
    const CampaignList = ({ campaigns, onSelectCampaign }) => (
      <div className="bg-white rounded-lg shadow">
        <div className="p-4 border-b">
          <h3 className="text-lg font-bold">Active Campaigns</h3>
        </div>
        <div className="divide-y">
          {campaigns.map(campaign => (
            <div 
              key={campaign.id}
              onClick={() => onSelectCampaign(campaign)}
              className="p-4 hover:bg-gray-50 cursor-pointer transition-colors"
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <h4 className="font-medium">{campaign.name}</h4>
                  <p className="text-sm text-gray-500">
                    {new Date(campaign.startDate).toLocaleDateString()} - 
                    {new Date(campaign.endDate).toLocaleDateString()}
                  </p>
                </div>
                <div className="text-right">
                  <p className="font-medium">
                    {campaign.impressions?.toLocaleString() || 0} / 
                    {campaign.target.toLocaleString()}
                  </p>
                  <p className="text-sm text-gray-500">
                    ${campaign.spent?.toLocaleString() || 0} of ${campaign.budget.toLocaleString()}
                  </p>
                </div>
              </div>
              
              {campaign.impressions && (
                <div className="space-y-2">
                  <div className="space-y-1">
                    <div className="flex justify-between text-sm text-gray-500">
                      <span>Impressions Progress</span>
                      <span>{Math.round((campaign.impressions / campaign.target) * 100)}%</span>
                    </div>
                    <div className="h-2 bg-gray-100 rounded">
                      <div 
                        className="h-full bg-blue-500 rounded"
                        style={{ width: `${(campaign.impressions / campaign.target) * 100}%` }}
                      />
                    </div>
                  </div>
                  
                  <div className="space-y-1">
                    <div className="flex justify-between text-sm text-gray-500">
                      <span>Budget Utilization</span>
                      <span>{Math.round((campaign.spent / campaign.budget) * 100)}%</span>
                    </div>
                    <div className="h-2 bg-gray-100 rounded">
                      <div 
                        className="h-full bg-green-500 rounded"
                        style={{ width: `${(campaign.spent / campaign.budget) * 100}%` }}
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    );
    
    const PromoTab = () => {
      const [campaigns, setCampaigns] = useState(generateCampaignData());
      const [selectedCampaign, setSelectedCampaign] = useState(null);
      const [timeRange, setTimeRange] = useState('7d');
    
      return (
        <div className="p-6 space-y-6">
          <TimeRangeSelector selected={timeRange} onChange={setTimeRange} />
    
          <div className="grid grid-cols-4 gap-4">
            <MetricCard
              title="Active Campaigns"
              value={campaigns.active.length}
              trend="up"
              trendValue={15}
              icon={Target}
            />
            <MetricCard
              title="Total Impressions"
              value={campaigns.active.reduce((sum, c) => sum + c.impressions, 0)}
              trend="up"
              trendValue={8}
              icon={Users}
            />
            <MetricCard
              title="Avg Engagement Rate"
              value="18.3%"
              trend="up"
              trendValue={5}
              icon={Activity}
            />
            <MetricCard
              title="Scheduled Campaigns"
              value={campaigns.scheduled.length}
              icon={Calendar}
            />
          </div>
    
          <CampaignList 
            campaigns={[...campaigns.active, ...campaigns.scheduled]} 
            onSelectCampaign={setSelectedCampaign}
          />
    
          {selectedCampaign && selectedCampaign.performance && (
            <div className="bg-white rounded-lg shadow p-6">
              <div className="flex justify-between items-start mb-6">
                <div>
                  <h3 className="text-lg font-bold">{selectedCampaign.name}</h3>
                  <p className="text-gray-500">Performance Overview</p>
                </div>
                <button 
                  onClick={() => setSelectedCampaign(null)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ×
                </button>
              </div>
    
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={selectedCampaign.performance}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="date" />
                    <YAxis yAxisId="left" />
                    <YAxis yAxisId="right" orientation="right" />
                    <Tooltip />
                    <Legend />
                    <Line
                      yAxisId="left"
                      type="monotone"
                      dataKey="impressions"
                      stroke={COLORS[0]}
                      name="Impressions"
                    />
                    <Line
                      yAxisId="right"
                      type="monotone"
                      dataKey="engagement"
                      stroke={COLORS[1]}
                      name="Engagement"
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
    
              <div className="grid grid-cols-2 gap-4 mt-6">
                <div className="space-y-2">
                  <h4 className="font-medium">Campaign Locations</h4>
                  <div className="flex flex-wrap gap-2">
                    {selectedCampaign.locations.map(location => (
                      <span 
                        key={location}
                        className="px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-sm"
                      >
                        {location}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      );
    };
    
    export default PromoTab;
    ```
    

![image.png](LAN%20Ad%20Analytics%20&%20Impression%20Tracking%20System%2018dfaa2a7b8a8016b2a4ef4d6ce7b1b9/image%202.png)

- QR code analytics
    
    ```jsx
    import React, { useState, useEffect } from 'react';
    import { 
      LineChart, Line, BarChart, Bar, PieChart, Pie,
      XAxis, YAxis, CartesianGrid, Tooltip, Legend, 
      ResponsiveContainer, Cell
    } from 'recharts';
    import { 
      QrCode, Users, Target, MapPin, Smartphone, 
      Share2, ArrowUp, ArrowDown
    } from 'lucide-react';
    
    const COLORS = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b'];
    
    // Mock Data Generator
    const generateQRData = () => {
      return {
        hourly: Array.from({ length: 24 }, (_, i) => ({
          hour: `${String(i).padStart(2, '0')}:00`,
          scans: Math.floor(Math.random() * 100) + 20,
          conversions: Math.floor(Math.random() * 50) + 10
        })),
        locations: [
          { name: 'Downtown', scans: 2451, conversions: 1230 },
          { name: 'Arts District', scans: 1832, conversions: 920 },
          { name: 'Museum Quarter', scans: 1654, conversions: 825 },
          { name: 'Transit Hub', scans: 1243, conversions: 610 }
        ],
        devices: [
          { name: 'iOS', value: 45 },
          { name: 'Android', value: 40 },
          { name: 'Other', value: 15 }
        ]
      };
    };
    
    const MetricCard = ({ title, value, trend, trendValue, icon: Icon }) => (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex justify-between items-start">
          <div>
            <p className="text-gray-500">{title}</p>
            <p className="text-2xl font-bold">
              {typeof value === 'number' ? value.toLocaleString() : value}
            </p>
            {trend && (
              <p className={`text-sm flex items-center ${
                trend === 'up' ? 'text-green-500' : 'text-red-500'
              }`}>
                {trend === 'up' ? (
                  <ArrowUp size={16} className="mr-1" />
                ) : (
                  <ArrowDown size={16} className="mr-1" />
                )}
                {trendValue}% vs last period
              </p>
            )}
          </div>
          <Icon className="text-blue-500" size={24} />
        </div>
      </div>
    );
    
    const TimeRangeSelector = ({ selected, onChange }) => (
      <div className="flex justify-end space-x-2 mb-6">
        {['24h', '7d', '30d', '90d'].map(range => (
          <button
            key={range}
            onClick={() => onChange(range)}
            className={`px-4 py-2 rounded-lg transition-colors ${
              selected === range
                ? 'bg-blue-500 text-white'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-600'
            }`}
          >
            {range}
          </button>
        ))}
      </div>
    );
    
    const QRTab = () => {
      const [qrData, setQRData] = useState(generateQRData());
      const [timeRange, setTimeRange] = useState('24h');
      const [selectedLocation, setSelectedLocation] = useState(null);
    
      useEffect(() => {
        const interval = setInterval(() => {
          setQRData(generateQRData());
        }, 300000); // Update every 5 minutes
    
        return () => clearInterval(interval);
      }, []);
    
      return (
        <div className="p-6 space-y-6">
          <TimeRangeSelector selected={timeRange} onChange={setTimeRange} />
    
          {/* QR Overview Stats */}
          <div className="grid grid-cols-4 gap-4">
            <MetricCard
              title="Total Scans"
              value={8392}
              trend="up"
              trendValue={23}
              icon={QrCode}
            />
            <MetricCard
              title="Unique Users"
              value={6147}
              trend="up"
              trendValue={15}
              icon={Users}
            />
            <MetricCard
              title="Conversion Rate"
              value="42%"
              trend="up"
              trendValue={5}
              icon={Target}
            />
            <MetricCard
              title="Active Locations"
              value={12}
              icon={MapPin}
            />
          </div>
    
          {/* Scan Activity Chart */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold mb-4">Hourly Scan Activity</h3>
            <div className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={qrData.hourly}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hour" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="scans" fill={COLORS[0]} name="Scans" />
                  <Bar dataKey="conversions" fill={COLORS[1]} name="Conversions" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
    
          <div className="grid grid-cols-2 gap-4">
            {/* Device Distribution */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold mb-4">Device Distribution</h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={qrData.devices}
                      dataKey="value"
                      nameKey="name"
                      cx="50%"
                      cy="50%"
                      outerRadius={80}
                      label
                    >
                      {qrData.devices.map((entry, index) => (
                        <Cell 
                          key={`cell-${index}`} 
                          fill={COLORS[index % COLORS.length]} 
                        />
                      ))}
                    </Pie>
                    <Tooltip />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>
    
            {/* Location Performance */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold mb-4">Location Performance</h3>
              <div className="space-y-4">
                {qrData.locations.map((location, index) => (
                  <div 
                    key={location.name}
                    className="space-y-2"
                    onClick={() => setSelectedLocation(location)}
                  >
                    <div className="flex justify-between items-center">
                      <div>
                        <p className="font-medium">{location.name}</p>
                        <p className="text-sm text-gray-500">
                          {location.conversions} conversions
                        </p>
                      </div>
                      <p className="text-lg font-medium">
                        {location.scans.toLocaleString()} scans
                      </p>
                    </div>
                    <div className="h-2 bg-gray-100 rounded">
                      <div
                        className="h-full rounded"
                        style={{
                          width: `${(location.scans / qrData.locations[0].scans) * 100}%`,
                          backgroundColor: COLORS[index % COLORS.length]
                        }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
    
          {/* Additional Analytics */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold mb-4">Conversion Funnel</h3>
            <div className="grid grid-cols-4 gap-4 text-center">
              {[
                { label: 'QR Scans', value: 8392 },
                { label: 'Page Views', value: 7253 },
                { label: 'Interactions', value: 4521 },
                { label: 'Conversions', value: 2134 }
              ].map((step, index) => (
                <div key={step.label} className="relative">
                  <div className="bg-gray-50 p-4 rounded">
                    <p className="text-sm text-gray-500">{step.label}</p>
                    <p className="text-xl font-bold">{step.value.toLocaleString()}</p>
                    {index < 3 && (
                      <div className="absolute right-0 top-1/2 transform translate-x-1/2 -translate-y-1/2">
                        <Share2 className="text-gray-300" size={20} />
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    };
    
    export default QRTab;
    ```
    

src/
├── components/
│   ├── Dashboard/
│   │   ├── Overview.js         # Main dashboard view
│   │   ├── ContentAnalytics.js # Content performance metrics
│   │   └── SystemStats.js      # System-wide statistics
│   ├── PromoAnalytics/
│   │   ├── index.js           # Main promo analytics view
│   │   ├── CampaignList.js    # Campaign management
│   │   └── Performance.js      # Performance metrics
│   ├── QRAnalytics/
│   │   ├── index.js           # Main QR analytics view
│   │   ├── ScanMetrics.js     # Scan statistics
│   │   └── LocationData.js     # Location-based analytics
│   ├── AdminSettings/
│   │   ├── index.js           # Admin settings container
│   │   ├── Primetime.js       # Primetime configuration
│   │   ├── Locations.js       # Location management
│   │   ├── Traffic.js         # Traffic estimation
│   │   └── Platform.js        # Platform settings
│   └── common/
│       ├── MetricCard.js      # Reusable metric card
│       ├── TimeSelector.js    # Time range selector
│       └── Charts.js          # Common chart components
└── layouts/
└── DashboardLayout.js     # Main layout with navigation