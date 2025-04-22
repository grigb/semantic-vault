# LAN Audience Tracking

# **Summary of Tracking Methods**

| Tracking Type | Method | Accuracy | Cost Per Display |
| --- | --- | --- | --- |
| **Foot Traffic (Basic)** | PIR Motion Sensor | Low | $10 |
|  | Wi-Fi Probe Scanner | Low-Mid | Free - $100 |
|  | Infrared Beam Break Sensor | Mid | $25 - $50 |
| **Foot Traffic (AI)** | USB Camera + OpenCV | Mid | $100 |
|  | Commercial AI Camera | High | $500 |
| **Vehicle Traffic (Basic)** | Google API (Free) | Low | Free |
| **Vehicle Traffic (Mid-Level)** | Used Security Camera + OpenCV | Mid | $150 |
|  | DIY Radar Sensor | Mid | $150 |
| **Vehicle Traffic (High-Accuracy)** | Professional AI Camera | High | $1,000 |

# Technical Summary

## **1. PIR Motion Sensors (Foot Traffic - Basic)**

### **Concept**

Passive Infrared (PIR) motion sensors detect body heat when a person moves in front of the display. These sensors are simple and effective for **estimating foot traffic**, but they **do not count individual people** or track viewing time.

### **How It Works**

- Detects motion within a **5-10 foot range**.
- Only registers presence when movement occurs.
- Cannot differentiate between individuals or track dwell time.

### **Best For**

- **Low-budget tracking** in areas where **exact numbers are not required**.
- Estimating **relative** foot traffic trends.

💰 **Cost Per Display: $10**

⚠️ **Limitations:** No detailed data, only detects movement.

---

## **2. Wi-Fi Probe Request Scanner (Foot Traffic - Basic to Moderate)**

### **Concept**

Every Wi-Fi-enabled device (smartphone, tablet, laptop) constantly **sends out signals** looking for networks. A **Wi-Fi probe request scanner** detects these signals, estimating how many people are near the display.

### **How It Works**

- Detects **Wi-Fi-enabled devices** within range (~30-50 feet).
- **No app or login required**—works passively.
- Cannot differentiate **individuals** but provides a **rough count**.

### **Best For**

- **Businesses tracking engagement trends** without using cameras.
- Estimating traffic **patterns over time**.

💰 **Cost Per Display: Free (if using an existing router) or $100**

⚠️ **Limitations:** Only detects people with Wi-Fi-enabled devices.

---

## **3. Infrared Beam Break Sensors (Foot Traffic - Basic Counting)**

### **Concept**

An **infrared beam** is placed across an entryway or in front of a display. When someone **walks past and breaks the beam**, it **counts one person**. If two sensors are placed side by side, they can **determine the direction** of movement.

### **How It Works**

- Simple **"entry/exit" count** method.
- Can be used **indoors or outdoors**.
- **Dual-sensor setup** allows **directional tracking**.

### **Best For**

- **Narrow walkways** where people must pass through a specific area.
- Small spaces with **controlled access points**.

💰 **Cost Per Display: $25 - $50**

⚠️ **Limitations:** Cannot track dwell time or differentiate individuals.

---

## **4. AI USB Camera + Raspberry Pi (Foot Traffic - Mid-Level AI Counting)**

### **Concept**

A **USB camera connected to a Raspberry Pi** runs **AI software** that can detect and count people. Open-source tools like **OpenCV** analyze video feeds in real-time, providing **more accurate audience measurement**.

### **How It Works**

- Uses **computer vision** to detect people in real-time.
- Can estimate **dwell time** and **engagement**.
- Does not store personal data or facial features.

### **Best For**

- **Moderate-budget tracking** that balances **cost and accuracy**.
- **Indoor and outdoor installations** where cameras are allowed.

💰 **Cost Per Display: $100**

⚠️ **Limitations:** Requires **occasional recalibration** for best results.

---

## **5. Used Security Camera + OpenCV AI Vehicle Detection (Outdoor Vehicle Tracking - Mid-Level)**

### **Concept**

A **repurposed security camera** combined with **OpenCV AI software** can **count vehicles** passing an outdoor display. AI-powered object detection can even estimate **vehicle types (cars, trucks, motorcycles).**

### **How It Works**

- Camera records **video feed**, AI detects **vehicles**.
- Can track **speed, direction, and volume** of traffic.
- Works best in **consistent lighting conditions**.

### **Best For**

- **Outdoor digital billboards** needing vehicle impression data.
- Situations where city traffic data **is not available**.

💰 **Cost Per Display: $150**

⚠️ **Limitations:** Needs **periodic AI model updates**.

---

## **6. DIY Radar Sensor (Outdoor Vehicle Tracking - Mid-Level)**

### **Concept**

A **low-cost radar sensor** detects **motion and speed** of passing vehicles. This method provides a **simple way to estimate traffic volume**, even in **low-light conditions**.

### **How It Works**

- Radar detects **metal objects moving at speed**.
- Estimates **vehicle counts and speeds**.
- Works **day and night**, unlike cameras.

### **Best For**

- **Roadside displays** where counting cars is the main goal.
- Areas with **low visibility** where cameras are ineffective.

💰 **Cost Per Display: $150**

⚠️ **Limitations:** Does not differentiate **vehicle types**.

---

## **7. Commercial AI Camera with Facial Recognition & Heat Mapping (Foot Traffic - High Accuracy)**

### **Concept**

A **high-end commercial AI camera** can detect **precise audience engagement** using **heat maps** and **anonymous facial recognition**. This provides **highly detailed analytics**.

### **How It Works**

- Recognizes **how long someone looks at a display**.
- Tracks **engagement by age, gender, and mood** (anonymized).
- Heat maps show **which parts of a display are most viewed**.

### **Best For**

- **High-traffic locations** needing detailed audience analytics.
- Advertisers looking for **precise engagement data**.

💰 **Cost Per Display: $500**

⚠️ **Limitations:** High cost, may have **privacy concerns** in public areas.

---

## **8. Professional AI Traffic Camera (Outdoor Vehicle Tracking - High Accuracy)**

### **Concept**

A **commercial-grade AI traffic camera** can **identify vehicle types, count cars, and even track license plates** (if needed for private parking analytics). This is the **most accurate** way to count passing vehicles.

### **How It Works**

- Uses **machine learning** to detect **car types and counts**.
- Works **in all lighting conditions**.
- Can provide **live data feeds** to cloud analytics.

### **Best For**

- **Billboards on high-traffic streets** needing accurate impressions.
- Advertisers tracking **ROI on digital ads**.

💰 **Cost Per Display: $1,000**

⚠️ **Limitations:** High cost, requires **internet connection for cloud analytics**.

# **Budget**

This breakdown provides a **per-display cost** for measuring **foot traffic (people viewing the display) and vehicle impressions (cars passing by an outdoor display).**

## **1. Low-Budget (Basic Tracking) – $10 - $75 per Display**

**Goal:** Provide a **basic** audience estimate with low-cost sensors and free data sources.

| Feature | Item | Cost Per Display |
| --- | --- | --- |
| **People Counting (Foot Traffic)** | PIR Motion Sensor | $10 |
|  | DIY Wi-Fi Probe Scanner (Existing Router) | Free |
|  | Infrared Beam Break Sensor | $25 |
| **Vehicle Counting (Outdoor Displays)** | Google Maps Traffic API (Free Tier) | Free |
|  | DIY Microphone-Based Vehicle Counter | $30 |

💰 **Total Per Display: $10 - $75**

🚀 **Pros:** Cheapest option, low power consumption

⚠️ **Cons:** Limited accuracy, only rough estimates

---

## **2. Mid-Budget (Improved Accuracy) – $175 - $600 per Display**

**Goal:** More accurate tracking with **AI-powered** sensors and basic machine learning.

| Feature | Item | Cost Per Display |
| --- | --- | --- |
| **People Counting (Foot Traffic)** | AI USB Camera + Raspberry Pi (Object Detection) | $100 |
|  | Wi-Fi Probe Request Scanner (Dedicated Setup) | $100 |
|  | Dual Infrared Beam Break Sensor | $50 |
| **Vehicle Counting (Outdoor Displays)** | Used Security Camera + OpenCV AI Detection | $150 |
|  | DIY Radar Speed & Volume Sensor | $150 |
|  | Google API (Paid Tier) | $100/month |

💰 **Total Per Display: $175 - $600**

🚀 **Pros:** Real-time tracking, AI-powered counting

⚠️ **Cons:** Requires some setup & occasional software updates

---

## **3. High-End Budget (Advanced Analytics) – $1,750 - $5,000 per Display**

**Goal:** Commercial-grade **AI tracking** with cloud-based data insights.

| Feature | Item | Cost Per Display |
| --- | --- | --- |
| **People Counting (Foot Traffic)** | Commercial AI Camera (Facial Recognition & Heat Mapping) | $500 |
|  | Advanced Wi-Fi Analytics Router (Meraki, Cisco) | $1,000 |
|  | LiDAR Sensor (3D People Counting) | $750 |
| **Vehicle Counting (Outdoor Displays)** | Professional AI Traffic Camera (License Plate & Vehicle Type ID) | $1,000 |
|  | Cloud-Based Traffic Analytics Subscription | $500/year |
|  | Google API (High Accuracy Plan) | $300/month |

💰 **Total Per Display: $1,750 - $5,000**

🚀 **Pros:** Highly accurate, minimal maintenance

⚠️ **Cons:** Expensive, requires cloud-based data processing

---

# **Comparison Table (Per Display Cost)**

| Budget Tier | Per Display Cost | Accuracy | Best For |
| --- | --- | --- | --- |
| **Low Budget** | **$10 - $75** | Basic | Small installations, rough estimates |
| **Mid Budget** | **$175 - $600** | Moderate | Medium-sized networks, AI-powered tracking |
| **High Budget** | **$1,750 - $5,000** | High | Large-scale deployments, commercial tracking |