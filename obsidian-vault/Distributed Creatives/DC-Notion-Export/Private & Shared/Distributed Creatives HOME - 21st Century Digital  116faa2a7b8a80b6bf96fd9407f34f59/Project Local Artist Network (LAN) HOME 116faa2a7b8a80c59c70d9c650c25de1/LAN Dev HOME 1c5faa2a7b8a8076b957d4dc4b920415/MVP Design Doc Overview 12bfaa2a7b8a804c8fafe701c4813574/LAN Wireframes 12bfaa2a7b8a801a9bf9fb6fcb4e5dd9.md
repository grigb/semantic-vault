# LAN Wireframes

### Backend

- Dashboard
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { Camera, Upload, Clock, Grid, Settings, PlayCircle, LayoutGrid, Users, ChevronRight, PlusCircle } from 'lucide-react';
        
        const ContentManagementWireframes = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-8">
              {/* Top Navigation */}
              <div className="w-full bg-gray-100 p-4 rounded-lg">
                <div className="flex justify-between items-center">
                  <div className="text-xl font-bold">LAN Content Management</div>
                  <div className="flex gap-4">
                    <button className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2">
                      <PlusCircle size={20} />
                      Add New Content
                    </button>
                    <button className="p-2 text-gray-600 hover:bg-gray-200 rounded-full">
                      <Settings size={20} />
                    </button>
                  </div>
                </div>
              </div>
        
              {/* Main Content Area */}
              <div className="flex gap-4">
                {/* Sidebar Navigation */}
                <div className="w-64 bg-gray-100 p-4 rounded-lg space-y-2">
                  <div className="flex items-center gap-3 p-2 bg-blue-100 rounded-lg cursor-pointer">
                    <Grid size={20} />
                    <span>Dashboard</span>
                  </div>
                  <div className="flex items-center gap-3 p-2 hover:bg-gray-200 rounded-lg cursor-pointer">
                    <PlayCircle size={20} />
                    <span>Content Library</span>
                  </div>
                  <div className="flex items-center gap-3 p-2 hover:bg-gray-200 rounded-lg cursor-pointer">
                    <Clock size={20} />
                    <span>Schedules</span>
                  </div>
                  <div className="flex items-center gap-3 p-2 hover:bg-gray-200 rounded-lg cursor-pointer">
                    <LayoutGrid size={20} />
                    <span>Display Layouts</span>
                  </div>
                  <div className="flex items-center gap-3 p-2 hover:bg-gray-200 rounded-lg cursor-pointer">
                    <Users size={20} />
                    <span>User Management</span>
                  </div>
                </div>
        
                {/* Main Content Grid */}
                <div className="flex-1 space-y-6">
                  {/* Content Library Header */}
                  <div className="flex justify-between items-center">
                    <h2 className="text-xl font-semibold">Content Library</h2>
                    <div className="flex gap-2">
                      <input 
                        type="text" 
                        placeholder="Search content..." 
                        className="px-4 py-2 border rounded-lg"
                      />
                      <select className="px-4 py-2 border rounded-lg">
                        <option>All Types</option>
                        <option>Videos</option>
                        <option>Images</option>
                        <option>Advertisements</option>
                      </select>
                    </div>
                  </div>
        
                  {/* Content Grid */}
                  <div className="grid grid-cols-3 gap-4">
                    {/* Content Card 1 */}
                    <div className="border rounded-lg overflow-hidden">
                      <div className="aspect-video bg-gray-200 relative">
                        <div className="absolute inset-0 flex items-center justify-center">
                          <Camera size={40} className="text-gray-400" />
                        </div>
                      </div>
                      <div className="p-4 space-y-2">
                        <h3 className="font-semibold">Artist Showcase Video</h3>
                        <div className="text-sm text-gray-500">Duration: 2:30</div>
                        <div className="flex justify-between items-center">
                          <span className="text-sm bg-green-100 text-green-800 px-2 py-1 rounded">Active</span>
                          <button className="text-blue-500 hover:text-blue-700">
                            <ChevronRight size={20} />
                          </button>
                        </div>
                      </div>
                    </div>
        
                    {/* Upload Card */}
                    <div className="border rounded-lg overflow-hidden border-dashed">
                      <div className="aspect-video bg-gray-50 flex items-center justify-center">
                        <div className="text-center">
                          <Upload size={40} className="mx-auto text-gray-400 mb-2" />
                          <div className="text-sm text-gray-500">Drop files to upload</div>
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Scheduling Panel */}
                  <div className="bg-gray-100 p-4 rounded-lg">
                    <h3 className="font-semibold mb-4">Quick Schedule</h3>
                    <div className="grid grid-cols-4 gap-4">
                      <div className="space-y-2">
                        <label className="text-sm text-gray-600">Content</label>
                        <select className="w-full px-3 py-2 rounded border">
                          <option>Select content...</option>
                        </select>
                      </div>
                      <div className="space-y-2">
                        <label className="text-sm text-gray-600">Start Date</label>
                        <input type="date" className="w-full px-3 py-2 rounded border" />
                      </div>
                      <div className="space-y-2">
                        <label className="text-sm text-gray-600">Display Duration</label>
                        <input type="time" className="w-full px-3 py-2 rounded border" />
                      </div>
                      <div className="flex items-end">
                        <button className="w-full px-4 py-2 bg-blue-500 text-white rounded-lg">
                          Schedule
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        };
        
        export default ContentManagementWireframes;
        ```
        
- Content Library
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%201.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Plus,
          Search,
          Filter,
          Play,
          Paintbrush,
          Calendar,
          Speaker,
          Clock,
          Settings,
          MoreVertical,
          CheckCircle,
          XCircle,
          Image
        } from 'lucide-react';
        
        const ContentLibrary = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-6 pb-8">
              {/* Header */}
              <div className="flex justify-between items-center bg-white p-4 rounded-lg border">
                <h1 className="text-xl font-bold">Content Library</h1>
                <div className="flex gap-2">
                  <button className="px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-lg">
                    <Settings size={20} />
                  </button>
                </div>
              </div>
        
              {/* Content Type Selection */}
              <div className="bg-white p-6 rounded-lg border">
                <h2 className="text-lg font-semibold mb-4">Create New Content</h2>
                <div className="grid grid-cols-5 gap-4">
                  <button className="p-6 border rounded-lg hover:border-blue-500 hover:bg-blue-50 flex flex-col items-center gap-2 group">
                    <Play size={24} className="text-gray-400 group-hover:text-blue-500" />
                    <span className="text-sm font-medium">Video</span>
                  </button>
                  
                  <button className="p-6 border rounded-lg hover:border-blue-500 hover:bg-blue-50 flex flex-col items-center gap-2 group">
                    <Paintbrush size={24} className="text-gray-400 group-hover:text-blue-500" />
                    <span className="text-sm font-medium">Artwork</span>
                  </button>
                  
                  <button className="p-6 border rounded-lg hover:border-blue-500 hover:bg-blue-50 flex flex-col items-center gap-2 group">
                    <Calendar size={24} className="text-gray-400 group-hover:text-blue-500" />
                    <span className="text-sm font-medium">Event</span>
                  </button>
                  
                  <button className="p-6 border rounded-lg hover:border-blue-500 hover:bg-blue-50 flex flex-col items-center gap-2 group">
                    <Image size={24} className="text-gray-400 group-hover:text-blue-500" />
                    <span className="text-sm font-medium">Promotion</span>
                  </button>
                  
                  <button className="p-6 border rounded-lg hover:border-blue-500 hover:bg-blue-50 flex flex-col items-center gap-2 group">
                    <Speaker size={24} className="text-gray-400 group-hover:text-blue-500" />
                    <span className="text-sm font-medium">Advertisement</span>
                  </button>
                </div>
              </div>
        
              {/* Content Filter Bar */}
              <div className="flex gap-4 items-center bg-white p-4 rounded-lg border">
                <div className="relative flex-1">
                  <Search size={20} className="absolute left-3 top-2.5 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search content..."
                    className="w-full pl-10 pr-4 py-2 border rounded-lg"
                  />
                </div>
                <div className="flex items-center gap-2">
                  <label className="text-sm font-medium">Type:</label>
                  <select className="px-3 py-2 border rounded-lg">
                    <option>All Types</option>
                    <option>Video</option>
                    <option>Artwork</option>
                    <option>Event</option>
                    <option>Promotion</option>
                    <option>Advertisement</option>
                  </select>
                </div>
                <div className="flex items-center gap-2">
                  <label className="text-sm font-medium">Status:</label>
                  <select className="px-3 py-2 border rounded-lg">
                    <option>All Status</option>
                    <option>Active</option>
                    <option>Inactive</option>
                    <option>Scheduled</option>
                  </select>
                </div>
              </div>
        
              {/* Content Grid */}
              <div className="grid grid-cols-3 gap-4">
                {/* Content Item */}
                <div className="bg-white rounded-lg border overflow-hidden hover:shadow-md transition-shadow">
                  <div className="relative aspect-video bg-gray-100">
                    <div className="absolute top-2 right-2 bg-green-100 text-green-800 px-2 py-1 rounded text-xs font-medium flex items-center gap-1">
                      <CheckCircle size={12} />
                      Active
                    </div>
                    <div className="absolute bottom-2 right-2 bg-black/75 text-white px-2 py-1 rounded text-xs font-medium flex items-center gap-1">
                      <Clock size={12} />
                      0:30
                    </div>
                    <div className="absolute inset-0 flex items-center justify-center">
                      <Play size={40} className="text-gray-400" />
                    </div>
                  </div>
                  <div className="p-4">
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <h3 className="font-medium line-clamp-1">Summer Art Festival Promo</h3>
                        <p className="text-sm text-gray-500">Video Content</p>
                      </div>
                      <button className="text-gray-400 hover:text-gray-600">
                        <MoreVertical size={20} />
                      </button>
                    </div>
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                      <Calendar size={14} />
                      <span>Scheduled: Jul 1 - Aug 31</span>
                    </div>
                  </div>
                </div>
        
                {/* Inactive Content Item */}
                <div className="bg-white rounded-lg border overflow-hidden hover:shadow-md transition-shadow">
                  <div className="relative aspect-video bg-gray-100">
                    <div className="absolute top-2 right-2 bg-red-100 text-red-800 px-2 py-1 rounded text-xs font-medium flex items-center gap-1">
                      <XCircle size={12} />
                      Inactive
                    </div>
                    <div className="absolute bottom-2 right-2 bg-black/75 text-white px-2 py-1 rounded text-xs font-medium flex items-center gap-1">
                      <Clock size={12} />
                      1:00
                    </div>
                    <div className="absolute inset-0 flex items-center justify-center">
                      <Paintbrush size={40} className="text-gray-400" />
                    </div>
                  </div>
                  <div className="p-4">
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <h3 className="font-medium line-clamp-1">Local Artist Showcase</h3>
                        <p className="text-sm text-gray-500">Artwork Gallery</p>
                      </div>
                      <button className="text-gray-400 hover:text-gray-600">
                        <MoreVertical size={20} />
                      </button>
                    </div>
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                      <Calendar size={14} />
                      <span>Last active: Jun 15</span>
                    </div>
                  </div>
                </div>
        
                {/* Add more content items as needed */}
              </div>
            </div>
          );
        };
        
        export default ContentLibrary;
        ```
        
- Add/Edit Video Content
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%202.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Video,
          Upload,
          Save,
          Eye,
          Clock,
          Tag,
          User,
          Volume2,
          Subtitles,
          ChevronLeft,
          Trash2
        } from 'lucide-react';
        
        const VideoContentEditor = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-6 pb-8">
              {/* Header */}
              <div className="flex justify-between items-center bg-gray-100 p-4 rounded-lg">
                <div className="flex items-center gap-3">
                  <button className="hover:bg-gray-200 p-2 rounded-full">
                    <ChevronLeft size={20} />
                  </button>
                  <div className="flex items-center gap-2">
                    <Video size={20} />
                    <h1 className="text-xl font-bold">Video Content</h1>
                  </div>
                </div>
                <div className="flex gap-3">
                  <button className="px-4 py-2 flex items-center gap-2 text-red-600 hover:bg-red-50 rounded-lg">
                    <Trash2 size={20} />
                    Delete
                  </button>
                  <button className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2">
                    <Save size={20} />
                    Save Content
                  </button>
                </div>
              </div>
        
              {/* Main Content */}
              <div className="grid grid-cols-3 gap-6">
                {/* Left Column - Main Content */}
                <div className="col-span-2 space-y-6">
                  {/* Video Upload */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Video Upload</h2>
                    <div className="border-2 border-dashed rounded-lg p-8">
                      <div className="text-center">
                        <Upload size={40} className="mx-auto text-gray-400 mb-4" />
                        <div className="text-sm text-gray-600 mb-2">
                          Drag and drop your video file here, or click to browse
                        </div>
                        <div className="text-xs text-gray-500 mb-4">
                          Supported formats: MP4, MOV, AVI (Max size: 2GB)
                        </div>
                        <button className="px-4 py-2 bg-blue-500 text-white rounded-lg">
                          Select Video
                        </button>
                      </div>
                    </div>
                    
                    {/* Upload Progress */}
                    <div className="mt-4">
                      <div className="flex justify-between text-sm mb-1">
                        <span>video_file.mp4</span>
                        <span>75%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div className="bg-blue-500 rounded-full h-2 w-3/4"></div>
                      </div>
                    </div>
                  </div>
        
                  {/* Video Details */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Video Details</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Title</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Enter video title..."
                        />
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Artist/Creator</label>
                          <div className="relative">
                            <User size={16} className="absolute left-3 top-3 text-gray-400" />
                            <input 
                              type="text"
                              className="w-full pl-10 pr-3 py-2 border rounded-lg"
                              placeholder="Artist name..."
                            />
                          </div>
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Video Length</label>
                          <div className="relative">
                            <Clock size={16} className="absolute left-3 top-3 text-gray-400" />
                            <input 
                              type="text"
                              className="w-full pl-10 pr-3 py-2 border rounded-lg"
                              placeholder="Duration..."
                            />
                          </div>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Categories</label>
                        <div className="flex flex-wrap gap-2">
                          <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                            Music
                          </span>
                          <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                            Performance
                          </span>
                          <button className="px-3 py-1 border rounded-full text-sm">
                            + Add Category
                          </button>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Description</label>
                        <textarea 
                          className="w-full px-3 py-2 border rounded-lg"
                          rows={4}
                          placeholder="Enter video description..."
                        />
                      </div>
                    </div>
                  </div>
                </div>
        
                {/* Right Column - Settings */}
                <div className="space-y-6">
                  {/* Playback Settings */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Playback Settings</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Mode</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Full Screen</option>
                          <option>Picture-in-Picture</option>
                          <option>Split Screen</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Audio Settings</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Play with Sound</option>
                          <option>Muted</option>
                          <option>Sound on Interaction</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Enable Captions</span>
                        </label>
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Loop Video</span>
                        </label>
                      </div>
                    </div>
                  </div>
        
                  {/* Schedule Settings */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Schedule</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Period</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Continuous</option>
                          <option>Specific Times</option>
                          <option>Custom Schedule</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Frequency</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Every Hour</option>
                          <option>Every 2 Hours</option>
                          <option>Custom</option>
                        </select>
                      </div>
                    </div>
                  </div>
        
                  {/* Preview Button */}
                  <button className="w-full px-4 py-3 bg-gray-100 text-gray-700 rounded-lg flex items-center justify-center gap-2 hover:bg-gray-200">
                    <Eye size={20} />
                    Preview Video Display
                  </button>
                </div>
              </div>
            </div>
          );
        };
        
        export default VideoContentEditor;
        ```
        
- Add/Edit Artwork Content
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%203.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Paintbrush,
          Upload,
          Save,
          Eye,
          ChevronLeft,
          Trash2,
          Image,
          DollarSign,
          QrCode,
          Tag,
          ImagePlus,
          Maximize,
          Link
        } from 'lucide-react';
        
        const ArtworkDisplayEditor = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-6 pb-8">
              {/* Header */}
              <div className="flex justify-between items-center bg-gray-100 p-4 rounded-lg">
                <div className="flex items-center gap-3">
                  <button className="hover:bg-gray-200 p-2 rounded-full">
                    <ChevronLeft size={20} />
                  </button>
                  <div className="flex items-center gap-2">
                    <Paintbrush size={20} />
                    <h1 className="text-xl font-bold">Artwork Display</h1>
                  </div>
                </div>
                <div className="flex gap-3">
                  <button className="px-4 py-2 flex items-center gap-2 text-red-600 hover:bg-red-50 rounded-lg">
                    <Trash2 size={20} />
                    Delete
                  </button>
                  <button className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2">
                    <Save size={20} />
                    Save Artwork
                  </button>
                </div>
              </div>
        
              {/* Main Content */}
              <div className="grid grid-cols-3 gap-6">
                {/* Left Column - Main Content */}
                <div className="col-span-2 space-y-6">
                  {/* Artwork Images */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Artwork Images</h2>
                    <div className="grid grid-cols-2 gap-4">
                      {/* Primary Image */}
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Primary Image</label>
                        <div className="border-2 border-dashed rounded-lg p-6 bg-gray-50">
                          <div className="text-center">
                            <Image size={40} className="mx-auto text-gray-400 mb-4" />
                            <div className="text-sm text-gray-600 mb-2">
                              High-quality primary view
                            </div>
                            <button className="px-4 py-2 bg-blue-500 text-white rounded-lg">
                              Upload Image
                            </button>
                          </div>
                        </div>
                      </div>
                      
                      {/* Detail Images */}
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Detail Images</label>
                        <div className="border-2 border-dashed rounded-lg p-6 bg-gray-50">
                          <div className="text-center">
                            <ImagePlus size={40} className="mx-auto text-gray-400 mb-4" />
                            <div className="text-sm text-gray-600 mb-2">
                              Additional views (up to 5)
                            </div>
                            <button className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg">
                              Add Images
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    {/* Image Requirements */}
                    <div className="mt-4 p-3 bg-blue-50 rounded-lg text-sm text-blue-800">
                      <ul className="list-disc list-inside space-y-1">
                        <li>Minimum resolution: 2000x2000px</li>
                        <li>File types: JPG, PNG, TIFF</li>
                        <li>Max file size: 20MB per image</li>
                      </ul>
                    </div>
                  </div>
        
                  {/* Artwork Details */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Artwork Details</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Artwork Title</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Enter artwork title..."
                        />
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Artist Name</label>
                          <input 
                            type="text"
                            className="w-full px-3 py-2 border rounded-lg"
                            placeholder="Artist name..."
                          />
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Year Created</label>
                          <input 
                            type="text"
                            className="w-full px-3 py-2 border rounded-lg"
                            placeholder="Year..."
                          />
                        </div>
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Medium</label>
                          <input 
                            type="text"
                            className="w-full px-3 py-2 border rounded-lg"
                            placeholder="e.g., Oil on canvas..."
                          />
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Style</label>
                          <select className="w-full px-3 py-2 border rounded-lg">
                            <option>Abstract</option>
                            <option>Realism</option>
                            <option>Impressionism</option>
                            <option>Digital</option>
                            <option>Other</option>
                          </select>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Dimensions</label>
                        <div className="grid grid-cols-3 gap-4">
                          <input 
                            type="text"
                            className="px-3 py-2 border rounded-lg"
                            placeholder="Width"
                          />
                          <input 
                            type="text"
                            className="px-3 py-2 border rounded-lg"
                            placeholder="Height"
                          />
                          <select className="px-3 py-2 border rounded-lg">
                            <option>inches</option>
                            <option>cm</option>
                            <option>pixels</option>
                          </select>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Description</label>
                        <textarea 
                          className="w-full px-3 py-2 border rounded-lg"
                          rows={4}
                          placeholder="Describe the artwork..."
                        />
                      </div>
                    </div>
                  </div>
                </div>
        
                {/* Right Column - Settings */}
                <div className="space-y-6">
                  {/* Purchase Information */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Purchase Information</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Availability</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>For Sale</option>
                          <option>Sold</option>
                          <option>Not For Sale</option>
                          <option>Prints Available</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Price</label>
                        <div className="relative">
                          <DollarSign size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="text"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="Enter price..."
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Purchase Link</label>
                        <div className="relative">
                          <Link size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="url"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="https://..."
                          />
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Display Settings */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Display Settings</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Mode</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Single Image</option>
                          <option>Slideshow</option>
                          <option>Interactive Gallery</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Duration</label>
                        <input 
                          type="number"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Seconds per image..."
                        />
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Transition Effect</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Fade</option>
                          <option>Slide</option>
                          <option>Zoom</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Enable Purchase QR Code</span>
                        </label>
                      </div>
                    </div>
                  </div>
        
                  {/* Preview Button */}
                  <button className="w-full px-4 py-3 bg-gray-100 text-gray-700 rounded-lg flex items-center justify-center gap-2 hover:bg-gray-200">
                    <Eye size={20} />
                    Preview Display
                  </button>
                </div>
              </div>
            </div>
          );
        };
        
        export default ArtworkDisplayEditor;
        ```
        
- Add/Edit Event Promotion Content
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%204.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Calendar,
          Save,
          Eye,
          ChevronLeft,
          Trash2,
          MapPin,
          Clock,
          DollarSign,
          Users,
          Image,
          Link,
          Ticket,
          Music,
          MessageSquare,
          Globe,
          Share2,
          AlertCircle
        } from 'lucide-react';
        
        const EventPromotionEditor = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-6 pb-8">
              {/* Header */}
              <div className="flex justify-between items-center bg-gray-100 p-4 rounded-lg">
                <div className="flex items-center gap-3">
                  <button className="hover:bg-gray-200 p-2 rounded-full">
                    <ChevronLeft size={20} />
                  </button>
                  <div className="flex items-center gap-2">
                    <Calendar size={20} />
                    <h1 className="text-xl font-bold">Event Promotion</h1>
                  </div>
                </div>
                <div className="flex gap-3">
                  <button className="px-4 py-2 flex items-center gap-2 text-red-600 hover:bg-red-50 rounded-lg">
                    <Trash2 size={20} />
                    Delete
                  </button>
                  <button className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2">
                    <Save size={20} />
                    Save Event
                  </button>
                </div>
              </div>
        
              {/* Main Content */}
              <div className="grid grid-cols-3 gap-6">
                {/* Left Column - Main Content */}
                <div className="col-span-2 space-y-6">
                  {/* Basic Event Information */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Event Details</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Event Title</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Enter event title..."
                        />
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Event Type</label>
                          <select className="w-full px-3 py-2 border rounded-lg">
                            <option>Live Music</option>
                            <option>Art Exhibition</option>
                            <option>Poetry Reading</option>
                            <option>Film Screening</option>
                            <option>Workshop</option>
                            <option>Multi-Venue Event</option>
                          </select>
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Age Restriction</label>
                          <select className="w-full px-3 py-2 border rounded-lg">
                            <option>All Ages</option>
                            <option>18+</option>
                            <option>21+</option>
                          </select>
                        </div>
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Start Date & Time</label>
                          <input 
                            type="datetime-local"
                            className="w-full px-3 py-2 border rounded-lg"
                          />
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">End Date & Time</label>
                          <input 
                            type="datetime-local"
                            className="w-full px-3 py-2 border rounded-lg"
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Event Description</label>
                        <textarea 
                          className="w-full px-3 py-2 border rounded-lg"
                          rows={4}
                          placeholder="Describe the event..."
                        />
                      </div>
                    </div>
                  </div>
        
                  {/* Location Information */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Location & Venue</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Venue Name</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Enter venue name..."
                        />
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Address</label>
                        <div className="relative">
                          <MapPin size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="text"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="Venue address..."
                          />
                        </div>
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Capacity</label>
                          <input 
                            type="number"
                            className="w-full px-3 py-2 border rounded-lg"
                            placeholder="Max attendees..."
                          />
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Venue Type</label>
                          <select className="w-full px-3 py-2 border rounded-lg">
                            <option>Indoor</option>
                            <option>Outdoor</option>
                            <option>Hybrid</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Performers/Artists */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Featured Artists</h2>
                    
                    <div className="space-y-4">
                      <div className="flex flex-wrap gap-2">
                        <span className="px-4 py-2 bg-purple-100 text-purple-800 rounded-lg flex items-center gap-2">
                          <Music size={16} />
                          Main Artist
                          <button className="ml-2 text-purple-600 hover:text-purple-800">×</button>
                        </span>
                        <span className="px-4 py-2 bg-purple-100 text-purple-800 rounded-lg flex items-center gap-2">
                          <Music size={16} />
                          Supporting Act
                          <button className="ml-2 text-purple-600 hover:text-purple-800">×</button>
                        </span>
                        <button className="px-4 py-2 border rounded-lg text-sm hover:bg-gray-50">
                          + Add Artist
                        </button>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Performance Schedule</label>
                        <div className="space-y-2">
                          <div className="flex items-center gap-2 p-3 border rounded-lg">
                            <Clock size={16} className="text-gray-400" />
                            <span className="text-sm">8:00 PM - Main Artist</span>
                            <button className="ml-auto text-gray-400 hover:text-gray-600">×</button>
                          </div>
                          <button className="text-sm text-blue-500 hover:text-blue-600">
                            + Add Time Slot
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
        
                {/* Right Column - Settings */}
                <div className="space-y-6">
                  {/* Ticketing Information */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Ticketing</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Ticket Type</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Paid Event</option>
                          <option>Free Event</option>
                          <option>Donation Based</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Ticket Price</label>
                        <div className="relative">
                          <DollarSign size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="text"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="0.00"
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Ticket Link</label>
                        <div className="relative">
                          <Ticket size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="url"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="https://..."
                          />
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Promotional Settings */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Promotion Settings</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Priority</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Normal</option>
                          <option>Featured</option>
                          <option>Spotlight</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Promotional Period</label>
                        <input 
                          type="number"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Days before event..."
                        />
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Enable QR Code</span>
                        </label>
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Show in Multi-Venue Feed</span>
                        </label>
                      </div>
                    </div>
                  </div>
        
                  {/* Media Assets */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Media Assets</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Event Banner</label>
                        <div className="border-2 border-dashed rounded-lg p-4 text-center">
                          <Image size={24} className="mx-auto text-gray-400 mb-2" />
                          <button className="text-sm text-blue-500">Upload Image</button>
                        </div>
                      </div>
        
                      <div className="p-3 bg-blue-50 rounded-lg">
                        <div className="flex items-start gap-2 text-sm text-blue-800">
                          <AlertCircle size={16} className="mt-0.5" />
                          <div>
                            Recommended size: 1920x1080px
                            <br />
                            Max file size: 5MB
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Preview Button */}
                  <button className="w-full px-4 py-3 bg-gray-100 text-gray-700 rounded-lg flex items-center justify-center gap-2 hover:bg-gray-200">
                    <Eye size={20} />
                    Preview Event Display
                  </button>
                </div>
              </div>
            </div>
          );
        };
        
        export default EventPromotionEditor;
        ```
        
- Add/Edit Advertisement Content
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%205.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Speaker,
          Save,
          Eye,
          ChevronLeft,
          Trash2,
          Clock,
          DollarSign,
          Target,
          Calendar,
          BarChart,
          Upload,
          Image,
          User,
          Link,
          Globe,
          Building,
          AlertCircle,
          Tag,
          Users
        } from 'lucide-react';
        
        const AdvertisementEditor = () => {
          return (
            <div className="w-full max-w-6xl mx-auto space-y-6 pb-8">
              {/* Header */}
              <div className="flex justify-between items-center bg-gray-100 p-4 rounded-lg">
                <div className="flex items-center gap-3">
                  <button className="hover:bg-gray-200 p-2 rounded-full">
                    <ChevronLeft size={20} />
                  </button>
                  <div className="flex items-center gap-2">
                    <Speaker size={20} />
                    <h1 className="text-xl font-bold">Advertisement</h1>
                  </div>
                </div>
                <div className="flex gap-3">
                  <button className="px-4 py-2 flex items-center gap-2 text-red-600 hover:bg-red-50 rounded-lg">
                    <Trash2 size={20} />
                    Delete
                  </button>
                  <button className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2">
                    <Save size={20} />
                    Save Campaign
                  </button>
                </div>
              </div>
        
              {/* Main Content */}
              <div className="grid grid-cols-3 gap-6">
                {/* Left Column - Main Content */}
                <div className="col-span-2 space-y-6">
                  {/* Campaign Information */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Campaign Details</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Campaign Name</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="Enter campaign name..."
                        />
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Advertiser</label>
                          <div className="relative">
                            <Building size={16} className="absolute left-3 top-3 text-gray-400" />
                            <input 
                              type="text"
                              className="w-full pl-10 pr-3 py-2 border rounded-lg"
                              placeholder="Company name..."
                            />
                          </div>
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Campaign Type</label>
                          <select className="w-full px-3 py-2 border rounded-lg">
                            <option>Brand Awareness</option>
                            <option>Event Promotion</option>
                            <option>Product Launch</option>
                            <option>Special Offer</option>
                            <option>Community Support</option>
                          </select>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Campaign Description</label>
                        <textarea 
                          className="w-full px-3 py-2 border rounded-lg"
                          rows={4}
                          placeholder="Describe the campaign objectives..."
                        />
                      </div>
                    </div>
                  </div>
        
                  {/* Advertisement Content */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Advertisement Content</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Content Type</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Static Image</option>
                          <option>Video</option>
                          <option>Interactive Display</option>
                          <option>Mixed Media</option>
                        </select>
                      </div>
        
                      <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Primary Content</label>
                          <div className="border-2 border-dashed rounded-lg p-6 bg-gray-50">
                            <div className="text-center">
                              <Upload size={40} className="mx-auto text-gray-400 mb-4" />
                              <div className="text-sm text-gray-600 mb-2">
                                Upload main advertisement
                              </div>
                              <button className="px-4 py-2 bg-blue-500 text-white rounded-lg">
                                Select File
                              </button>
                            </div>
                          </div>
                        </div>
                        
                        <div className="space-y-2">
                          <label className="block text-sm font-medium">Alternative Versions</label>
                          <div className="border-2 border-dashed rounded-lg p-6 bg-gray-50">
                            <div className="text-center">
                              <Image size={40} className="mx-auto text-gray-400 mb-4" />
                              <div className="text-sm text-gray-600 mb-2">
                                Different sizes/formats
                              </div>
                              <button className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg">
                                Add Files
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
        
                      <div className="p-3 bg-yellow-50 rounded-lg">
                        <div className="flex items-start gap-2 text-sm text-yellow-800">
                          <AlertCircle size={16} className="mt-0.5" />
                          <div>
                            Content Guidelines:
                            <ul className="list-disc list-inside mt-1">
                              <li>Images: 1920x1080px (16:9 ratio)</li>
                              <li>Videos: 15-30 seconds, MP4 format</li>
                              <li>Max file size: 100MB</li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Call to Action */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Call to Action</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">CTA Type</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Visit Website</option>
                          <option>Scan QR Code</option>
                          <option>Special Offer</option>
                          <option>Learn More</option>
                          <option>Contact Us</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Destination URL</label>
                        <div className="relative">
                          <Link size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="url"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="https://..."
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">CTA Button Text</label>
                        <input 
                          type="text"
                          className="w-full px-3 py-2 border rounded-lg"
                          placeholder="e.g., Learn More, Shop Now..."
                        />
                      </div>
                    </div>
                  </div>
                </div>
        
                {/* Right Column - Settings */}
                <div className="space-y-6">
                  {/* Campaign Schedule */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Campaign Schedule</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Campaign Period</label>
                        <div className="grid grid-cols-2 gap-4">
                          <div className="relative">
                            <Calendar size={16} className="absolute left-3 top-3 text-gray-400" />
                            <input 
                              type="date"
                              className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            />
                          </div>
                          <div className="relative">
                            <Calendar size={16} className="absolute left-3 top-3 text-gray-400" />
                            <input 
                              type="date"
                              className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            />
                          </div>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Frequency</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>Every Hour</option>
                          <option>Every 2 Hours</option>
                          <option>Custom Schedule</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Display Duration</label>
                        <div className="relative">
                          <Clock size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="number"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="Seconds..."
                          />
                        </div>
                      </div>
                    </div>
                  </div>
        
                  {/* Targeting */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Targeting</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Venue Types</label>
                        <div className="flex flex-wrap gap-2">
                          <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                            Cafes
                          </span>
                          <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                            Bars
                          </span>
                          <button className="px-3 py-1 border rounded-full text-sm">
                            + Add Type
                          </button>
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Geographic Area</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>All Locations</option>
                          <option>Downtown Only</option>
                          <option>Custom Areas</option>
                        </select>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Time Targeting</label>
                        <select className="w-full px-3 py-2 border rounded-lg">
                          <option>All Hours</option>
                          <option>Peak Hours Only</option>
                          <option>Custom Hours</option>
                        </select>
                      </div>
                    </div>
                  </div>
        
                  {/* Budget & Analytics */}
                  <div className="bg-white p-6 rounded-lg border space-y-4">
                    <h2 className="text-lg font-semibold">Campaign Metrics</h2>
                    
                    <div className="space-y-4">
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Campaign Budget</label>
                        <div className="relative">
                          <DollarSign size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="number"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="Enter budget..."
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="block text-sm font-medium">Target Impressions</label>
                        <div className="relative">
                          <Users size={16} className="absolute left-3 top-3 text-gray-400" />
                          <input 
                            type="number"
                            className="w-full pl-10 pr-3 py-2 border rounded-lg"
                            placeholder="Target views..."
                          />
                        </div>
                      </div>
        
                      <div className="space-y-2">
                        <label className="flex items-center gap-2">
                          <input type="checkbox" className="rounded text-blue-500" />
                          <span className="text-sm">Enable Performance Analytics</span>
                        </label>
                      </div>
                    </div>
                  </div>
        
                  {/* Preview Button */}
                  <button className="w-full px-4 py-3 bg-gray-100 text-gray-700 rounded-lg flex items-center justify-center gap-2 hover:bg-gray-200">
                    <Eye size={20} />
                    Preview Advertisement
                  </button>
                </div>
              </div>
            </div>
          );
        };
        
        export default AdvertisementEditor;
        ```
        

### TV

- Main view
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%206.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { QrCode, Play, Building } from 'lucide-react';
        
        const TVInterface = () => {
          return (
            <div className="w-full h-screen bg-black relative">
              {/* Main Content Area */}
              <div className="relative w-full h-full">
                {/* Content Preview */}
                <div className="absolute inset-0 bg-gray-800 flex items-center justify-center">
                  <Play size={64} className="text-gray-600" />
                </div>
        
                {/* Lower Third with Integrated QR Box */}
                <div className="absolute bottom-12 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent px-8 pt-8 pb-4">
                  <div className="flex items-start gap-8">
                    {/* Text Content */}
                    <div className="flex-1 text-white space-y-2">
                      <h1 className="text-3xl font-bold">Content Title</h1>
                      <h2 className="text-xl text-gray-300">Subtitle Information</h2>
                      <p className="text-gray-400">Additional details and information about the current content</p>
                    </div>
        
                    {/* Network Promotion Box */}
                    <div className="w-80 bg-black/60 backdrop-blur-sm rounded-lg p-6">
                      <div className="text-white space-y-4">
                        <h3 className="text-xl font-bold">Join Our Network</h3>
                        <p className="text-gray-300">Become part of the Local Artist Network. Display your content across our venues.</p>
                        <div className="flex flex-col items-center gap-2">
                          <div className="w-40 h-40 bg-white rounded-lg p-2">
                            <QrCode className="w-full h-full" />
                          </div>
                          <span className="text-sm text-gray-300">Scan to Learn More</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
        
                {/* Sponsor Ticker */}
                <div className="absolute bottom-0 left-0 right-0 bg-black/90 h-12">
                  <div className="h-full flex items-center gap-4 px-4">
                    <div className="flex items-center gap-3">
                      <span className="text-gray-400 text-sm uppercase tracking-wider">Sponsored by:</span>
                      <div className="h-8 w-8 bg-gray-700 rounded flex items-center justify-center">
                        <Building size={16} className="text-gray-400" />
                      </div>
                      <div className="text-white">
                        <span className="font-medium">Sponsor Name</span>
                        <span className="mx-3 text-gray-500">|</span>
                        <span className="text-gray-300">Sponsor message or tagline goes here</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        };
        
        export default TVInterface;
        ```
        
- Home Screen
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%207.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { ChevronRight, Calendar, Clock, MapPin, Star, Settings } from 'lucide-react';
        
        const HomeScreen = () => {
          // Mock data - in production this would come from WordPress
          const featuredContent = [
            { id: 1, title: 'Summer Jazz Festival', image: '/api/placeholder/800/400', date: '2024-07-15' },
            { id: 2, title: 'Modern Art Exhibition', image: '/api/placeholder/800/400', date: '2024-07-16' },
            { id: 3, title: 'Theater: Romeo & Juliet', image: '/api/placeholder/800/400', date: '2024-07-17' }
          ];
        
          const liveNow = [
            { id: 1, title: 'Street Art Workshop', viewers: 234, thumbnail: '/api/placeholder/400/225' },
            { id: 2, title: 'Poetry Reading', viewers: 156, thumbnail: '/api/placeholder/400/225' }
          ];
        
          const localArtists = [
            { id: 1, name: 'Jane Smith', type: 'Painter', image: '/api/placeholder/200/200' },
            { id: 2, name: 'John Doe', type: 'Musician', image: '/api/placeholder/200/200' },
            { id: 3, name: 'Alice Brown', type: 'Sculptor', image: '/api/placeholder/200/200' }
          ];
        
          const categories = [
            'Live Performances', 'Visual Art', 'Film & Video', 'Music',
            'Poetry', 'Dance', 'Theater', 'Cultural Events'
          ];
        
          return (
            <div className="min-h-screen bg-gray-900 text-white p-6">
              {/* Quick Access Bar */}
              <div className="flex justify-between items-center mb-6 bg-gray-800 p-4 rounded-lg">
                <div className="flex items-center gap-3">
                  <img 
                    src="https://distributedcreatives.org/wp-content/uploads/2024/09/distributed-creatives-512-150x150.png"
                    alt="Distributed Creatives Logo"
                    className="h-8 w-8"
                  />
                  <span className="text-lg font-semibold">Distributed Creatives</span>
                </div>
                <div className="flex items-center gap-6">
                  <div className="flex items-center gap-2">
                    <Clock className="h-5 w-5" />
                    <span>10:30 AM</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <MapPin className="h-5 w-5" />
                    <span>Boulder, Colorado</span>
                  </div>
                  <div className="flex items-center gap-4">
                    <button className="bg-blue-600 px-3 py-1 rounded">QR</button>
                    <button className="bg-blue-600 px-3 py-1 rounded">🔊</button>
                    <button className="text-gray-300 hover:text-white transition-colors">
                      <Settings className="h-5 w-5" />
                    </button>
                  </div>
                </div>
              </div>
        
              {/* Featured Content Carousel */}
              <div className="mb-8">
                <h2 className="text-2xl font-bold mb-4">Featured</h2>
                <div className="flex gap-4 overflow-x-auto pb-4">
                  {featuredContent.map(item => (
                    <div key={item.id} className="flex-none w-96 relative">
                      <img 
                        src={item.image} 
                        alt={item.title}
                        className="rounded-lg w-full h-48 object-cover"
                      />
                      <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black">
                        <h3 className="text-lg font-semibold">{item.title}</h3>
                        <p className="text-sm text-gray-300">{item.date}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
        
              {/* Live Now Section */}
              <div className="mb-8">
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-2xl font-bold">Live Now</h2>
                  <button className="flex items-center text-blue-400">
                    View All <ChevronRight className="h-4 w-4" />
                  </button>
                </div>
                <div className="flex gap-4">
                  {liveNow.map(stream => (
                    <div key={stream.id} className="bg-gray-800 rounded-lg overflow-hidden">
                      <img 
                        src={stream.thumbnail} 
                        alt={stream.title}
                        className="w-full h-32 object-cover"
                      />
                      <div className="p-3">
                        <h3 className="font-semibold">{stream.title}</h3>
                        <p className="text-sm text-gray-400">{stream.viewers} watching</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
        
              {/* Category Quick Access */}
              <div className="mb-8">
                <h2 className="text-2xl font-bold mb-4">Categories</h2>
                <div className="grid grid-cols-4 gap-4">
                  {categories.map(category => (
                    <button 
                      key={category}
                      className="bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition"
                    >
                      {category}
                    </button>
                  ))}
                </div>
              </div>
        
              {/* Local Artist Spotlight */}
              <div className="mb-8">
                <h2 className="text-2xl font-bold mb-4">Local Artist Spotlight</h2>
                <div className="flex gap-4">
                  {localArtists.map(artist => (
                    <div key={artist.id} className="bg-gray-800 rounded-lg overflow-hidden">
                      <img 
                        src={artist.image} 
                        alt={artist.name}
                        className="w-full h-48 object-cover"
                      />
                      <div className="p-3">
                        <h3 className="font-semibold">{artist.name}</h3>
                        <p className="text-sm text-gray-400">{artist.type}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
        
              {/* Recently Viewed & Recommendations */}
              <div className="grid grid-cols-2 gap-6">
                <div>
                  <h2 className="text-2xl font-bold mb-4">Recently Viewed</h2>
                  <div className="bg-gray-800 rounded-lg p-4">
                    <div className="flex items-center gap-4 mb-3">
                      <Calendar className="h-5 w-5" />
                      <span>Ballet Performance - Yesterday</span>
                    </div>
                    <div className="flex items-center gap-4">
                      <Star className="h-5 w-5" />
                      <span>Art Gallery Tour - 2 days ago</span>
                    </div>
                  </div>
                </div>
                <div>
                  <h2 className="text-2xl font-bold mb-4">Recommended For You</h2>
                  <div className="bg-gray-800 rounded-lg p-4">
                    <div className="flex items-center gap-4 mb-3">
                      <Star className="h-5 w-5" />
                      <span>Jazz Night at Blue Note</span>
                    </div>
                    <div className="flex items-center gap-4">
                      <Star className="h-5 w-5" />
                      <span>Contemporary Dance Workshop</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        };
        
        export default HomeScreen;
        ```
        
- Main Menu
    
    ![image.png](Distributed%20Creatives/DC-Notion-Export/Private%20&%20Shared/Distributed%20Creatives%20HOME%20-%2021st%20Century%20Digital%20%20116faa2a7b8a80b6bf96fd9407f34f59/Project%20Local%20Artist%20Network%20(LAN)%20HOME%20116faa2a7b8a80c59c70d9c650c25de1/LAN%20Dev%20HOME%201c5faa2a7b8a8076b957d4dc4b920415/MVP%20Design%20Doc%20Overview%2012bfaa2a7b8a804c8fafe701c4813574/LAN%20Wireframes%2012bfaa2a7b8a801a9bf9fb6fcb4e5dd9/image%208.png)
    
    - Code
        
        ```jsx
        import React from 'react';
        import { 
          Calendar, 
          Map, 
          Search, 
          Settings, 
          HelpCircle, 
          Users, 
          Radio, 
          X,
          Building2,
          ChevronRight,
          Monitor
        } from 'lucide-react';
        
        const MainMenu = ({ onClose }) => {
          const menuItems = [
            { icon: Monitor, label: 'Retail Mode', description: 'Display the LAN broadcast signage' },
            { icon: Radio, label: 'Live Now', description: 'Currently streaming events' },
            { icon: Calendar, label: 'Events', description: 'Upcoming performances and shows' },
            { icon: Users, label: 'Artists', description: 'Browse featured creators' },
            { icon: Building2, label: 'Venues', description: 'Explore local spaces' },
            { icon: Calendar, label: 'My Calendar', description: 'Your scheduled events' },
            { icon: Search, label: 'Search', description: 'Find events and artists' },
            { icon: Settings, label: 'Settings', description: 'System preferences' },
            { icon: HelpCircle, label: 'Help/Support', description: 'Get assistance' }
          ];
        
          return (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-start justify-end">
              <div className="h-full w-96 bg-gray-900 shadow-lg">
                {/* Header */}
                <div className="flex justify-between items-center p-6 border-b border-gray-800">
                  <h2 className="text-2xl font-bold text-white">Main Menu</h2>
                  <button 
                    onClick={onClose}
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    <X className="h-6 w-6" />
                  </button>
                </div>
        
                {/* Menu Items */}
                <div className="p-4">
                  {menuItems.map((item, index) => (
                    <button 
                      key={index}
                      className="w-full text-left p-4 flex items-center justify-between group hover:bg-gray-800 rounded-lg mb-2 transition-colors"
                    >
                      <div className="flex items-center gap-4">
                        <div className="text-blue-400">
                          <item.icon className="h-6 w-6" />
                        </div>
                        <div>
                          <div className="text-white font-medium">{item.label}</div>
                          <div className="text-sm text-gray-400">{item.description}</div>
                        </div>
                      </div>
                      <ChevronRight className="h-5 w-5 text-gray-400 group-hover:text-white transition-colors" />
                    </button>
                  ))}
                </div>
        
                {/* Footer */}
                <div className="absolute bottom-0 w-full p-6 border-t border-gray-800">
                  <div className="flex items-center gap-3">
                    <img 
                      src="https://distributedcreatives.org/wp-content/uploads/2024/09/distributed-creatives-512-150x150.png"
                      alt="Distributed Creatives Logo"
                      className="h-8 w-8"
                    />
                    <div>
                      <div className="text-white font-medium">Distributed Creatives</div>
                      <div className="text-sm text-gray-400">Version 1.0.0</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        };
        
        export default MainMenu;
        ```