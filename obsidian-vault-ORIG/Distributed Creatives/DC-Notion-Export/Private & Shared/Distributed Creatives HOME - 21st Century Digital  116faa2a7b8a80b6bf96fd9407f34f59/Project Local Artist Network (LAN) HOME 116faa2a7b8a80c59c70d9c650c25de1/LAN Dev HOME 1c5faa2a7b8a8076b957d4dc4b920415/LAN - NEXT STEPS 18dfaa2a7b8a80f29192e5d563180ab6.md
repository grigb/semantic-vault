# LAN - NEXT STEPS

note to self: I was working on the content library and working on the editor, and I realized that the editor needed more context and therefore, I had to create a more specific understanding of the metrics we were trying to gather so that we could create the perfect UI for it.

Once we've done the stuff below, the next step will be to go back to the content library section and refine the options, for example, in edit promo, there's an advertiser which is a field that you can fill out, this should actually be a selection from the available promoters which should be a promoters tag underneath the admin section. The target auditions shouldn't just be a field. Either hit needs to be some sort of choice from settings el. This way the system is based off of object types. Also take a look at the edit artwork section. The creator is a field and there as well, and that should obviously be a creator object that you select after it's been created in the admin section. Obviously the admin section is supposed to be for the organization to control not the user.

this is the doc I prepared to explain what needs to be functional, it is a little to much for an MVP

[LAN **Ad Analytics & Impression Tracking System**](LAN%20Ad%20Analytics%20&%20Impression%20Tracking%20System%2018dfaa2a7b8a8016b2a4ef4d6ce7b1b9.md)

- share this outline of what needs to be done next 1
    
    # Local Artist Network Platform Development Guide
    
    ## 1. UI Restructuring and Campaign Management (Priority)
    
    ### Navigation Restructuring
    
    1. Move Campaign Management to Main Menu
        - Separate from Analytics section
        - Add dedicated "Campaigns" main menu item
        - Sub-items should include:
            - Campaign Overview
            - Create Campaign
            - Campaign Settings
            - Campaign Analytics
    
    ### Location Management Redesign
    
    1. Create Location Selection System
        - Build searchable location directory
        - Add location filtering by:
            - Region
            - Type (Gallery, Museum, Public Space)
            - Traffic volume
            - Available screen types
        - Include location details preview
        - Show current performance metrics for available locations
    2. Location Target Management
        - Create location target addition workflow
            - Location search and selection
            - Initial target settings
            - Performance goals
        - For each targeted location:
            - Individual timeslot configuration
            - Traffic thresholds
            - Content rotation settings
            - Performance targets
            - Budget allocation
    3. Campaign Location Analytics
        - Per-location performance dashboard
        - Historical data visualization
        - Comparison tools between locations
        - Traffic pattern analysis
        - Engagement metrics
        - ROI calculation per location
    
    ### Campaign Creation Workflow Redesign
    
    1. Setup Phase
        - Basic campaign information
        - Budget allocation
        - Timeline setting
        - Content upload/selection
    2. Location Targeting Phase
        - Location search and selection
        - Bulk location addition
        - Location-specific settings
        - Preview estimated reach
    3. Schedule Configuration Phase
        - Global campaign schedule
        - Per-location schedule overrides
        - Prime time settings
        - Content rotation rules
    4. Performance Goals Phase
        - Overall campaign goals
        - Per-location targets
        - Budget distribution
        - Performance thresholds
    
    ### Campaign Management Interface
    
    1. Campaign Overview
        - Campaign status
        - Overall performance
        - Budget utilization
        - Active locations list
    2. Location Management
        - Active locations grid/list
        - Individual location performance
        - Schedule overview
        - Quick actions per location
    3. Performance Dashboard
        - Campaign-wide metrics
        - Location comparison tools
        - Time-based analysis
        - Goal tracking
    
    ### Required Components
    
    1. Location Directory
    
    ```jsx
    // LocationDirectory.js
    const LocationDirectory = () => {
      - Search interface
      - Filter controls
      - Location grid/list
      - Quick preview
      - Selection mechanism
    };
    
    ```
    
    1. Location Target Settings
    
    ```jsx
    // LocationTargetSettings.js
    const LocationTargetSettings = () => {
      - Time slot configuration
      - Traffic settings
      - Performance goals
      - Budget allocation
    };
    
    ```
    
    1. Campaign Location Dashboard
    
    ```jsx
    // CampaignLocationDashboard.js
    const CampaignLocationDashboard = () => {
      - Performance metrics
      - Historical data
      - Comparison tools
      - Action buttons
    };
    
    ```
    
    ### Data Structure Updates
    
    1. Locations
    
    ```tsx
    interface Location {
      id: string;
      name: string;
      type: LocationType;
      region: string;
      screens: Screen[];
      trafficPatterns: TrafficPattern[];
      operatingHours: OperatingHours;
      performanceHistory: PerformanceMetric[];
    }
    
    ```
    
    1. Campaign Locations
    
    ```tsx
    interface CampaignLocation {
      locationId: string;
      campaignId: string;
      schedule: TimeSlot[];
      budget: BudgetAllocation;
      performanceGoals: PerformanceGoals;
      metrics: LocationMetrics;
      status: LocationStatus;
    }
    
    ```
    
    1. Time Slots
    
    ```tsx
    interface TimeSlot {
      locationId: string;
      dayOfWeek: number;
      startTime: string;
      endTime: string;
      trafficMultiplier: number;
      contentRotation: RotationSettings;
    }
    
    ```
    
    ### Implementation Steps
    
    1. Phase 1: Navigation and Basic Structure
        - Implement new menu structure
        - Create basic location directory
        - Build location target settings component
    2. Phase 2: Location Management
        - Develop location search and filtering
        - Create location target configuration
        - Build location performance dashboard
    3. Phase 3: Campaign Workflow
        - Implement new campaign creation flow
        - Build location-specific settings
        - Create schedule management
    4. Phase 4: Analytics and Reporting
        - Develop location comparison tools
        - Build performance dashboards
        - Create reporting interfaces
    
    ## Current Implementation Status
    
    ### Completed Features
    
    1. Basic Campaign Management
        - Campaign overview with metrics
        - Budget tracking and visualization
        - Location targeting system
        - Time slot scheduling
        - Campaign performance metrics
    2. Location Management
        - Basic location configuration
        - Screen management per location
        - Traffic estimation settings
        - Operating hours configuration
    3. Analytics Dashboard
        - Impression tracking across platforms
        - Performance visualization
        - Basic metrics display
        - Time-range selection
    
    ### Required Implementations
    
    1. Impression Tracking System
        - Implement real-time impression counting mechanism
        - Add unique impression tracking using device/session identifiers
        - Build primetime vs non-primetime distinction
        - Create dynamic impression weight calculation based on:
            - Screen rotation time
            - Location traffic multipliers
            - Time-based adjustments
    2. Enhanced Location Analytics
        - Real-time screen status reporting
        - Traffic pattern analysis
        - Screen-specific performance metrics
        - Location comparison tools
        - Add support for AI-based traffic estimation
    3. QR Code System
        - QR code generation for each content piece
        - QR scan tracking with metadata:
            - Timestamp
            - Location correlation
            - Device information
            - Session tracking
        - QR code performance analytics
        - Conversion tracking from QR destinations
    4. Remote Action Tracking
        - Implement UTM parameter management
        - Add conversion tracking system for:
            - Sign-ups
            - Purchases
            - Downloads
            - Custom engagement metrics
        - Build JavaScript tracking beacon
        - Create engagement reporting dashboard
    5. Enhanced Budget Management
        - Dynamic budget allocation based on performance
        - Automated scheduling adjustments
        - Performance-based optimization
        - ROI calculation and reporting
    6. Promo Account Features
        - Account tier management
        - Budget allocation tools
        - Campaign scheduling interface
        - Performance reporting dashboard
        - Location targeting based on traffic patterns
    7. Data Analysis & Reporting
        - Custom report generation
        - Data export capabilities
        - Advanced filtering options
        - Cross-platform performance comparison
        - Historical trend analysis
    
    ## Technical Requirements
    
    1. Database Schema Extensions:
        - Add tables for impression tracking
        - QR code management
        - User session tracking
        - Conversion tracking
        - Performance metrics
    2. API Endpoints to Build:
        - Real-time impression tracking
        - QR code management
        - Analytics data retrieval
        - Campaign performance metrics
        - Location status updates
        - User engagement tracking
    3. Frontend Components Needed:
        - QR Code Management Interface
        - Advanced Analytics Dashboard
        - Real-time Performance Monitor
        - Campaign Optimization Tools
        - Location Performance Comparison
        - Custom Report Builder
    
    ## Priority Order for Implementation
    
    1. Core Functionality
        - Complete impression tracking system
        - Basic QR code implementation
        - Essential analytics tracking
    2. Enhanced Features
        - Advanced location analytics
        - Detailed performance tracking
        - Campaign optimization tools
    3. Advanced Features
        - AI-based traffic estimation
        - Advanced reporting tools
        - Custom integrations
    
    ## Technical Considerations
    
    1. Performance:
        - Implement efficient data storage for high-volume tracking
        - Use caching for frequently accessed metrics
        - Optimize real-time data processing
    2. Scalability:
        - Design for multi-location support
        - Plan for high-volume data processing
        - Consider distributed system architecture
    3. Security:
        - Implement proper data encryption
        - Add user authentication and authorization
        - Secure API endpoints
        - Protect sensitive analytics data
    
    ## Notes for Future Development
    
    - Focus on modular component design for easy updates
    - Maintain consistent error handling
    - Document all API endpoints and data structures
    - Consider implementing feature flags for gradual rollout
    - Plan for A/B testing capabilities
    - Consider implementing data archival strategies
    - Add comprehensive logging system
    
    This system should integrate seamlessly with the existing components while providing a foundation for future enhancements and scaling.
    
- prompt for next session v1 - should be good
    
    # Local Artist Network Platform Development Guide
    
    ## Context and Current State
    
    This is a React-based dashboard for managing digital signage content, promotional campaigns, and analytics across multiple locations. The system currently has:
    
    1. Basic campaign management with:
        - Campaign overview metrics
        - Budget tracking
        - Basic location targeting
        - Performance visualization
    2. A PromoAnalytics section that currently handles:
        - Campaign performance metrics
        - Location targeting (incorrectly placed here)
        - Budget visualization
        - Basic scheduling
    
    ## Identified Issues
    
    During review, several structural and functional issues were identified:
    
    1. **Incorrect Feature Placement**
        - Location targeting is currently under PromoAnalytics
        - Campaign management features are mixed with analytics
        - Time slot management is not location-specific
    2. **Missing Location Management**
        - No master location directory
        - Cannot select from available locations
        - No per-location settings
        - Limited location performance tracking
    3. **Workflow Issues**
        - Campaign creation process is not streamlined
        - Location targeting is too simplified
        - Schedule management lacks granularity
    
    ## Required Changes
    
    ### 1. Navigation Restructuring
    
    Move campaign management out of analytics into its own main menu section:
    
    ```jsx
    const MENU_ITEMS = [
        {
            id: 'campaigns',
            icon: Campaign,
            label: 'Campaigns',
            subItems: [
                { id: 'overview', label: 'Campaign Overview' },
                { id: 'create', label: 'Create Campaign' },
                { id: 'settings', label: 'Campaign Settings' },
                { id: 'analytics', label: 'Campaign Analytics' }
            ]
        },
        // Existing analytics and other sections...
    ];
    
    ```
    
    ### 2. Location Management System
    
    Create a comprehensive location management system:
    
    ```jsx
    interface Location {
        id: string;
        name: string;
        type: LocationType;
        screens: Screen[];
        operatingHours: {
            [day: string]: {
                open: string;
                close: string;
                timeSlots: TimeSlot[];
            }
        };
        trafficPatterns: TrafficPattern[];
        performanceMetrics: PerformanceMetric[];
    }
    
    interface CampaignLocation extends Location {
        campaignId: string;
        targetSettings: {
            timeSlots: TimeSlot[];
            trafficThreshold: number;
            budget: BudgetAllocation;
        };
        performance: {
            impressions: number;
            engagement: number;
            roi: number;
        };
    }
    
    ```
    
    ### 3. Campaign Creation Workflow
    
    Implement a step-based campaign creation process:
    
    ```jsx
    const CampaignCreation = () => {
        const steps = [
            'basicInfo',
            'locationSelection',
            'locationSettings',
            'scheduling',
            'budgeting',
            'review'
        ];
    
        // Step components...
    };
    
    ```
    
    ## Implementation Priority
    
    1. **Phase 1: Structure**
        - New navigation system
        - Campaign management section
        - Location directory foundation
    2. **Phase 2: Location System**
        - Location management interface
        - Location selection system
        - Per-location settings
    3. **Phase 3: Campaign Workflow**
        - Step-based campaign creation
        - Location-specific targeting
        - Schedule management
    4. **Phase 4: Analytics**
        - Performance tracking
        - Location analytics
        - Campaign insights
    
    ## Technical Requirements
    
    ### Components to Create/Modify:
    
    1. **LocationDirectory.js**
        - Searchable location list
        - Filtering system
        - Location details view
        - Selection mechanism
    2. **LocationSettings.js**
        - Time slot configuration
        - Traffic settings
        - Performance goals
        - Budget allocation
    3. **CampaignWorkflow.js**
        - Step navigation
        - Form validation
        - Settings management
        - Preview capabilities
    
    ### Data Structure Updates:
    
    ```tsx
    // Add these tables/collections to your database
    interface CampaignSchema {
        id: string;
        name: string;
        status: CampaignStatus;
        locations: CampaignLocation[];
        budget: BudgetSettings;
        schedule: Schedule;
        performance: PerformanceMetrics;
    }
    
    interface LocationSchema {
        id: string;
        details: LocationDetails;
        screens: Screen[];
        settings: LocationSettings;
        metrics: LocationMetrics;
    }
    
    ```
    
    ## Design Guidelines
    
    1. **UI Principles**
        - Use consistent spacing (multiples of 4)
        - Follow existing color scheme
        - Maintain responsive design
        - Use existing component patterns
    2. **State Management**
        - Keep location state separate from campaign state
        - Cache location directory data
        - Implement optimistic updates
        - Handle loading states
    3. **Error Handling**
        - Validate location selections
        - Check schedule conflicts
        - Verify budget allocations
        - Handle network errors
    
    ## Development Notes
    
    1. The system uses:
        - React with TypeScript
        - Tailwind CSS for styling
        - Recharts for visualizations
        - Lucide for icons
    2. Existing components can be found in:
        - /components/PromoAnalytics
        - /components/LocationsManagement
        - /components/shared
    3. Folder structure follows:
    
    ```
    src/
    ├── components/
    │   ├── Campaign/
    │   ├── Location/
    │   ├── Analytics/
    │   └── shared/
    ├── hooks/
    ├── services/
    └── utils/
    
    ```
    
    ## Testing Requirements
    
    1. Unit tests for:
        - Location selection logic
        - Schedule validation
        - Budget calculations
    2. Integration tests for:
        - Campaign creation flow
        - Location management
        - Analytics generation
    
    ## Next Steps
    
    1. Begin with navigation restructuring
    2. Implement location directory
    3. Create campaign workflow
    4. Add location-specific settings
    5. Enhance analytics system
    
    The goal is to create a more structured, scalable system where campaign management and analytics are properly separated, and location management is comprehensive and granular.
    
    Note: All existing functionality should be preserved while implementing these changes. Use the existing UI components and patterns where possible to maintain consistency.
    
- prompt for next session v2 - created this because I couldn’t see the v1, but it looks a little vauge, but might be a good backup
    
    # Local Artist Network Platform Development Guide
    
    Hello, future AI assistant. You are continuing development on a digital signage platform that manages content, promotional campaigns, and analytics across multiple locations. Let me explain the current state and what needs to be done.
    
    ## Current Implementation Status
    
    The platform currently has:
    
    - A campaign management system with basic metrics and budget tracking
    - Location targeting (incorrectly placed in PromoAnalytics section)
    - Basic performance visualization
    - Campaign budget management
    - Simple scheduling features
    
    ## Key Issues Identified
    
    1. Location Targeting is misplaced:
        - Currently exists as tabs within PromoAnalytics
        - Should be part of campaign management
        - Lacks granular location-specific settings
    2. Time Slot Management is too broad:
        - Currently applies globally
        - Should be configurable per location
        - Needs to account for location-specific traffic patterns
    3. Location Selection is limited:
        - No master location directory
        - Can't select from available locations
        - Missing location-specific performance metrics
        - No historical data per location
    
    ## Required Changes
    
    ### 1. Navigation Restructuring
    
    The main menu needs to be reorganized:
    
    - Move Campaigns to main navigation
    - Separate analytics from management
    - Create dedicated location management section
    
    ### 2. New Campaign Management Flow
    
    Create a new step-based campaign creation:
    
    1. Basic Campaign Info
    2. Location Selection
        - Searchable location directory
        - Location details preview
        - Bulk location selection
    3. Per-Location Settings
        - Time slots configuration
        - Traffic thresholds
        - Performance goals
    4. Budget Allocation
        - Overall campaign budget
        - Per-location budget settings
    5. Review and Launch
    
    ### 3. Location Management System
    
    Build a comprehensive location system:
    
    - Master location directory
    - Location profiles with:
        - Operating hours
        - Screen inventory
        - Traffic patterns
        - Historical performance
    - Location targeting settings
    - Performance tracking per location
    
    ## Component Structure
    
    ```jsx
    // New main components needed:
    
    // CampaignCreationFlow.js
    const CampaignCreationFlow = () => {
      const steps = [
        'basicInfo',
        'locationSelection',
        'locationSettings',
        'budgeting',
        'review'
      ];
      // Step management logic
    };
    
    // LocationDirectory.js
    const LocationDirectory = () => {
      // Search and filter interface
      // Location grid/list view
      // Quick actions
      // Selection mechanism
    };
    
    // LocationSettings.js
    const LocationSettings = ({ locationId, campaignId }) => {
      // Time slot configuration
      // Traffic settings
      // Budget allocation
      // Performance goals
    };
    
    // LocationPerformance.js
    const LocationPerformance = ({ locationId, campaignId }) => {
      // Performance metrics
      // Historical data
      // Comparison tools
    };
    
    ```
    
    ## Data Structures Needed
    
    ```tsx
    interface Location {
      id: string;
      name: string;
      type: string;
      screens: {
        id: string;
        type: string;
        resolution: string;
        orientation: string;
      }[];
      operatingHours: {
        [day: string]: {
          open: string;
          close: string;
        };
      };
      trafficPatterns: {
        timeSlot: string;
        averageTraffic: number;
        peakMultiplier: number;
      }[];
    }
    
    interface CampaignLocation {
      locationId: string;
      campaignId: string;
      settings: {
        timeSlots: TimeSlot[];
        trafficThreshold: number;
        budgetAllocation: number;
      };
      performance: {
        impressions: number;
        engagement: number;
        spend: number;
      };
    }
    
    ```
    
    ## Implementation Steps
    
    1. First Phase:
        - Create new navigation structure
        - Build location directory
        - Implement basic location selection
    2. Second Phase:
        - Develop location settings interface
        - Create time slot management
        - Add traffic settings
    3. Third Phase:
        - Build performance tracking
        - Implement analytics
        - Add comparison tools
    
    ## Technical Notes
    
    - The project uses React with TypeScript
    - Styling is done with Tailwind CSS
    - Charts use Recharts library
    - Icons from Lucide-react
    - All new components should follow existing patterns
    - Maintain responsive design throughout
    - Use existing color schemes and spacing
    
    ## Important Considerations
    
    1. Data Management:
        - Cache location directory
        - Implement optimistic updates
        - Handle loading states properly
        - Add error boundaries
    2. User Experience:
        - Maintain consistent navigation
        - Add proper loading states
        - Implement error handling
        - Provide user feedback
    3. Performance:
        - Optimize location directory for large datasets
        - Implement pagination where needed
        - Cache frequently accessed data
        - Use proper memoization
    
    ## Testing Requirements
    
    Ensure test coverage for:
    
    - Location selection logic
    - Time slot validation
    - Budget calculations
    - Performance metric accuracy
    
    ## Final Notes
    
    The goal is to create a more organized and efficient system where:
    
    1. Campaign management is separate from analytics
    2. Locations can be easily managed and monitored
    3. Settings can be configured at both campaign and location levels
    4. Performance can be tracked granularly
    
    Maintain backwards compatibility while implementing these changes. Use existing UI patterns and components where possible to ensure consistency.