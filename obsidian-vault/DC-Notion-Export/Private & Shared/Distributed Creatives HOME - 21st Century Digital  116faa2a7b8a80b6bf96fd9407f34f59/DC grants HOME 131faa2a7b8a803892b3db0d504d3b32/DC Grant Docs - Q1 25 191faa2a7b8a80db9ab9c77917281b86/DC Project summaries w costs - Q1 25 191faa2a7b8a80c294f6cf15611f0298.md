# DC: Project summaries w/ costs - Q1 25

## Local Artist Network (LAN)

**Budget Details:**

- Beta launch ($1k)
    - Displays (used): $250-$400 each for 4k 55”
    - Dev: Done by Grig for free
    - Server: Paid for by Grig
- Boulder at scale (all basic features) - year 1-2 ($36k)
    - Displays w/ traffic estimator cams: $350-$600 * 30 screens = $15k
    - Dev: $20k
        - Basic features: Grig (free) or full-stack dev $100/hr for 150 hrs = $15k
        - AI traffic estimator code: $100/hr for 50 hours = $5k
    - Server: Additional server power $300-500/yr = $1k
- **Live streaming of events at six venues:** ($3k)
    - Hardware (mics, mixer, cameras, install) $500 per venue *6 venues = $3k
    - Streaming server service: $500/year
- **World-wide syndication (smart TV apps):** $10-$30k

**Implementation Details:**

- Content rotation every 1 minute to maintain viewer interest
- Mix of display sizes from 17" to 65" 4K screens
- Integration with venue POS systems for transactions
- Some venues may be willing to pay for hardware to be part of the network

**Revenue Potential:**

- Sponsor advertising limited to 10% of air time (144 impressions)
- Venue subscriptions (tiered based on location prestige and foot traffic)
- Commission on artwork sales through the network
- Data licensing for urban planning and cultural impact studies
- Revenue (assuming maximum slots sold)
    - **Monthly Revenue Matrix**
        - Humble (2 venues): $3,697.80
        - Humble (10 venues): $18,489.00
        - Humble (25 venues): $46,222.50
        - In-demand (2 venues): $19,831.20
        - In-demand (10 venues): $99,156.00
        - In-demand (25 venues): $247,890.00
        - Premier (2 venues): $43,435.80
        - Premier (10 venues): $217,179.00
        - Premier (25 venues): $542,947.50
    - Humble? ($.10 - $.50 per impression/per venue) = $61.63/day
        - Code and graph
            
            ![image.png](DC%20Project%20summaries%20w%20costs%20-%20Q1%2025%20191faa2a7b8a80c294f6cf15611f0298/image.png)
            
            ```jsx
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Define the hours in the day (0 to 23)
            hours = np.arange(0, 24, 1)
            
            # --- Example Assumptions ---
            # We create a revenue rate (price per impression) that varies with time.
            # For simplicity, let’s assume a sinusoidal function that peaks during
            # “high viewership” hours (say around 8 AM, noon, and 6 PM) and is lower at night.
            # (These numbers are illustrative.)
            
            # Base rate: $0.10 per impression during the low end.
            # Additional premium: up to an extra $0.50 during peaks.
            revenue_rate = 0.10 + .5 * np.sin((hours - 8) * np.pi / 12)
            
            # To avoid negative rates (since sine goes negative), we clip the values.
            revenue_rate = np.clip(revenue_rate, 0.05, None)
            
            # Total ad impressions per day is 144.
            # Let’s assume that the impressions are distributed across the day in proportion
            # to the revenue rate (i.e. higher viewership times get more impressions).
            impressions_per_hour = (revenue_rate / revenue_rate.sum()) * 144
            
            # Calculate the revenue per hour (dollars) = (impressions sold that hour) * (price per impression)
            hourly_revenue = revenue_rate * impressions_per_hour
            
            # Calculate total daily revenue by summing hourly revenues
            total_daily_revenue = hourly_revenue.sum()
            
            # Print the total daily revenue
            print("Total daily revenue from ad impressions: ${:.2f}".format(total_daily_revenue))
            
            # --- Plotting ---
            plt.figure(figsize=(10, 6))
            plt.plot(hours, hourly_revenue, marker='o', linestyle='-', color='b')
            plt.title("Potential Revenue per Hour from Ad Impressions")
            plt.xlabel("Hour of Day")
            plt.ylabel("Revenue ($)")
            plt.xticks(hours)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            ```
            
    - In-demand  ($.50 - $2.50 per impression/per venue) $330.52/day
        - Code and graph
            
            ![image.png](DC%20Project%20summaries%20w%20costs%20-%20Q1%2025%20191faa2a7b8a80c294f6cf15611f0298/image%201.png)
            
            ```jsx
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Define the hours in the day (0 to 23)
            hours = np.arange(0, 24, 1)
            
            # --- Example Assumptions ---
            # We create a revenue rate (price per impression) that varies with time.
            # For simplicity, let’s assume a sinusoidal function that peaks during
            # “high viewership” hours (say around 8 AM, noon, and 6 PM) and is lower at night.
            # (These numbers are illustrative.)
            
            # Base rate: $0.10 per impression during the low end.
            # Additional premium: up to an extra $0.50 during peaks.
            revenue_rate = 0.50 + 2.5 * np.sin((hours - 8) * np.pi / 12)
            
            # To avoid negative rates (since sine goes negative), we clip the values.
            revenue_rate = np.clip(revenue_rate, 0.05, None)
            
            # Total ad impressions per day is 144.
            # Let’s assume that the impressions are distributed across the day in proportion
            # to the revenue rate (i.e. higher viewership times get more impressions).
            impressions_per_hour = (revenue_rate / revenue_rate.sum()) * 144
            
            # Calculate the revenue per hour (dollars) = (impressions sold that hour) * (price per impression)
            hourly_revenue = revenue_rate * impressions_per_hour
            
            # Calculate total daily revenue by summing hourly revenues
            total_daily_revenue = hourly_revenue.sum()
            
            # Print the total daily revenue
            print("Total daily revenue from ad impressions: ${:.2f}".format(total_daily_revenue))
            
            # --- Plotting ---
            plt.figure(figsize=(10, 6))
            plt.plot(hours, hourly_revenue, marker='o', linestyle='-', color='b')
            plt.title("Potential Revenue per Hour from Ad Impressions")
            plt.xlabel("Hour of Day")
            plt.ylabel("Revenue ($)")
            plt.xticks(hours)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            ```
            
    - Major-demand  ($.50 - $2.50 per impression/per venue) $723.93/day
        - Code and graph
            
            ![image.png](DC%20Project%20summaries%20w%20costs%20-%20Q1%2025%20191faa2a7b8a80c294f6cf15611f0298/image%202.png)
            
            ```jsx
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Define the hours in the day (0 to 23)
            hours = np.arange(0, 24, 1)
            
            # --- Example Assumptions ---
            # We create a revenue rate (price per impression) that varies with time.
            # For simplicity, let’s assume a sinusoidal function that peaks during
            # “high viewership” hours (say around 8 AM, noon, and 6 PM) and is lower at night.
            # (These numbers are illustrative.)
            
            # Base rate: $0.10 per impression during the low end.
            # Additional premium: up to an extra $0.50 during peaks.
            revenue_rate = 0.50 + 2.5 * np.sin((hours - 8) * np.pi / 12)
            
            # To avoid negative rates (since sine goes negative), we clip the values.
            revenue_rate = np.clip(revenue_rate, 0.05, None)
            
            # Total ad impressions per day is 144.
            # Let’s assume that the impressions are distributed across the day in proportion
            # to the revenue rate (i.e. higher viewership times get more impressions).
            impressions_per_hour = (revenue_rate / revenue_rate.sum()) * 144
            
            # Calculate the revenue per hour (dollars) = (impressions sold that hour) * (price per impression)
            hourly_revenue = revenue_rate * impressions_per_hour
            
            # Calculate total daily revenue by summing hourly revenues
            total_daily_revenue = hourly_revenue.sum()
            
            # Print the total daily revenue
            print("Total daily revenue from ad impressions: ${:.2f}".format(total_daily_revenue))
            
            # --- Plotting ---
            plt.figure(figsize=(10, 6))
            plt.plot(hours, hourly_revenue, marker='o', linestyle='-', color='b')
            plt.title("Potential Revenue per Hour from Ad Impressions")
            plt.xlabel("Hour of Day")
            plt.ylabel("Revenue ($)")
            plt.xticks(hours)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            ```
            
    - Matrix calculations
        
        ![image.png](DC%20Project%20summaries%20w%20costs%20-%20Q1%2025%20191faa2a7b8a80c294f6cf15611f0298/image%203.png)
        
        - Code
            
            ```jsx
            import numpy as np
            import matplotlib.pyplot as plt
            
            # --- Parameters ---
            
            # Daily revenue per venue for each venue type:
            daily_revenues = {
                "Humble": 61.63,
                "In-demand": 330.52,
                "Premier": 723.93
            }
            
            # List of venue types and their corresponding daily revenues
            venue_types = list(daily_revenues.keys())
            daily_rev_values = np.array([daily_revenues[vt] for vt in venue_types])
            
            # Calculate monthly revenue per venue (assuming 30 days per month)
            monthly_revenue_per_venue = daily_rev_values * 30
            
            # Venue count scenarios
            venues_counts = np.array([2, 10, 25])
            
            # --- Calculation ---
            # For each venue type, the total monthly revenue for a given number of venues is:
            # total_monthly_revenue = (monthly revenue per venue) * (number of venues)
            revenue_matrix = np.outer(monthly_revenue_per_venue, venues_counts)
            
            # --- Output the matrix values ---
            print("Monthly Revenue Matrix (Rows: Venue Types, Columns: Number of Venues):\n")
            for i, vt in enumerate(venue_types):
                for j, count in enumerate(venues_counts):
                    revenue = revenue_matrix[i, j]
                    print(f"{vt} ({count} venues): ${revenue:,.2f}")
                print()
            
            # --- Plotting as a Heatmap (Matrix Graph) ---
            plt.figure(figsize=(8, 6))
            # Create the heatmap
            im = plt.imshow(revenue_matrix, cmap='plasma', aspect='auto')
            
            # Add a colorbar to show the revenue scale
            plt.colorbar(im, label="Monthly Revenue ($)")
            
            # Set the tick labels:
            plt.xticks(ticks=np.arange(len(venues_counts)), labels=venues_counts)
            plt.yticks(ticks=np.arange(len(venue_types)), labels=venue_types)
            
            plt.xlabel("Number of Venues")
            plt.ylabel("Venue Type")
            plt.title("Monthly Revenue by Venue Type and Number of Venues")
            
            # Get normalization and colormap objects to map data values to colors
            norm = plt.Normalize(vmin=revenue_matrix.min(), vmax=revenue_matrix.max())
            cmap = plt.get_cmap("plasma")
            
            # Annotate each cell with the revenue value.
            for i in range(revenue_matrix.shape[0]):
                for j in range(revenue_matrix.shape[1]):
                    cell_value = revenue_matrix[i, j]
                    # Get the RGBA color for this cell's value
                    cell_color = cmap(norm(cell_value))
                    # cell_color is a tuple (R, G, B, A) with values in [0, 1]
                    # If the background is yellowish, use black text; otherwise, use white text.
                    if cell_color[0] > 0.9 and cell_color[1] > 0.8 and cell_color[2] < 0.4:
                        text_color = "black"
                    else:
                        text_color = "white"
                    
                    plt.text(j, i, f"${cell_value:,.0f}",
                             ha="center", va="center", color=text_color, fontsize=10)
            
            plt.tight_layout()
            plt.show()
            ```
            

**Content Distribution:**

- Average of 1,440 impressions per day per location (1 per minute)
- 70% or more for creators
- Tribal Nations content: Showcasing the history of tribal nations in Boulder, CO
- Youth art opportunities: Updates for programs like CU Boulder, YOAB, and other youth projects
- Venue-specific content: Event promotions, schedules, and announcements
- Sponsor/advertising content (limited to 10% of air time)

**Key Features:**

- Digital signage network in public spaces and venues
- Interactive smart TV app for artist-venue-audience connection
- Live streaming capabilities
- Creator profiles with booking management and ticketing
- QR code integration for direct artist connections to Musely.social

## Forever Sites

**Budget Details:**

- Admin team for onboarding content:
- Perpetual storage costs
    - Arweave: ~$30/GB
    - [Lighthouse](https://files.lighthouse.storage/) (Filecoin):
        - 1 GB - Free
        - 150 GB - $500
- 1000 year CDs
    - Per disc / per location

**Key Features:**

- Decentralized storage across multiple platforms (Arweave, FileCoin, DIG network)
- Paid for by the creator or sponsor per org/creator/collection
- High-fidelity content preservation
- AI-assisted format conversion and upscaling
- Blockchain-based authentication system
- [Schema.org](http://Schema.org) metadata framework

## Musely.Social

- **Social plugin:** ([PeepSo](https://www.peepso.com/pricing/#plugin)) $440/2 years

**Current Features:**

- File sharing capabilities
- Group and page management
- User profiles
- Community engagement tools

**Possible Features/Cost:**

- **Ticketing/Event Management:** ([WP Event Manager](https://wp-eventmanager.com/pricing/)) $800/2 years (Tier One)
- Community/collective support ✅
    - Make groups, organize members, tabs, organize the brand
    - Needs dev to clean up, improve UX
- Monetization
    - **Selling digital files:** ([Easy Digital Downloads](https://easydigitaldownloads.com/)) $400/2 years
    - **Donations:** ([GiveWP](https://givewp.com/pricing/)) - $1k/2 years (Tier One)
    - **Membership like Patreon:** ([Paid Memberships Pro](https://www.paidmembershipspro.com/)) $600/2 years (or $3000 lifetime) (Tier Two)
    - **Tipping:** ([Micro Payments by CMinds](https://www.cminds.com/wordpress-plugins-library/cm-micropayments-peepso-social-network-integration-addon-wordpress/)) $150/2 years (Tier One)
    - **Physical product marketplace per user:** ([Dokan](https://dokan.co/wordpress/pricing/)) $2121 - lifetime (Tier Two)
    - **Classified ads:** ([WPAdverts](https://wpadverts.com/features/)) ($300 / 2 years)
    - **Job Boards:** ([WP Job Manager](https://wpjobmanager.com/add-ons/bundle/)) - $318 / 2 years (Tier Two)
    - **eLearning / Courseware:** ([LearnDash](https://www.learndash.com/)/[TutorLMS](https://tutorlms.com/)) - $1000/2 years
    - **Ads from sponsors/members in feed:** ([AdvancedAds](https://wpadvancedads.com/pricing/)) - $340/2 years
- Gamification:
    - **User credits for activities:** ([myCred](https://mycred.me/pricing/#pricing-addons)) - $700 / lifetime (Tier Two)
- Networking
    - **Email list support / newsletter per user/group:** ([The Newsletter Plugin](https://www.thenewsletterplugin.com/premium)) - $99 lifetime (Tier Two)
    - **Forums for individual groups:** ([bbPress](https://wbcomdesigns.com/downloads/peepso-bbpress-addon/ref/Tracz/)) - $200 / 2 years (Tier Two)
    - **Push posts to federated sites:** ([ActivityPub](https://wordpress.org/plugins/activitypub/)) - Free
    - **Cross posting to socials:** ([SNAP by NextScripts](https://www.nextscripts.com/social-networks-auto-poster-for-wordpress/)) - $500 / 2 years (Tier Two)
    - Invite app (like Partiful or Apple’s new invite app)
    - **Affiliate Program:** ([Affiliate WP](https://affiliatewp.com/pricing/#pricing-table)) - $600 / 2 years (Tier Two)
- Hosting media locally - $200-$2000/month
    - $200-$2000/month
    - Value always increases because all data must be stored forever
- Music Player - custom code required for all features
    - Streaming radio w/ tagging system
    - Social comments on waveforms
    - Beat matching/live mixing
    - Remixing
    - Composable/remixable music stems
- Web3
    - Quadratic funding ([Allo](https://allo.xyz/)) - Custom dev
    - **NFT Store on Chia:** Free / In Kind donation from Sumset Tech
    - **NFT Collection Management/Mint on Chia:** Free / In Kind donation from Sumset Tech
    - **NFT Rewards System:** Free / In Kind donation from Sumset Tech
    - **Sell with Crypto:** ([BTCPay](https://btcpayserver.org/)) - Free

## The Show

**Budget:**

- Low res hardware: $3k
- 4k hardware: $20k
- Streaming fees: $250/month

**Key Features:**

- Regular live-streamed performances
- Archived content library
- Interactive audience participation
- Talent discovery platform

## VOD & Live video

**Budget Details: $2,500**

Based on using api.video

The table below summarizes these average monthly metrics for each of the three years:

| Year | VOD Uploads per Month (GB) | VOD Total Traffic per Month (GB) | Cost/Yearly | Live Streaming Duration per Month (hours) | Live Streaming Traffic per Month (GB) | Cost/Year |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 9088 | $2,165 | 180 | 463 | 2,617 |
| 2 | 559 | 28521 | $6,794 | 180 | 10000 | 4,524 |
| 3 | 1754 | 89464 | $18,906 | 3508 | 40000 | 9,471.94 |
|  |  |  |  |  |  |  |