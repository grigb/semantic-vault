# Implementation Plan for Adding 3D File Support to PeepSo

Based on this: https://gitlab.com/PeepSo/Public/HelloWorld

### **1. File Upload Handling**

### Objective:

Enable users to upload 3D files (e.g., `.glb`, `.gltf`, `.obj`) through the PeepSo interface.

### Steps:

1. **Extend Allowed File Types**:
    - Add support for 3D file extensions by hooking into PeepSo’s upload validation process.
        
        ```
        add_filter('peepso_allowed_file_types', function ($types) {
            $types[] = 'glb';
            $types[] = 'gltf';
            $types[] = 'obj';
            return $types;
        });
        ```
        
2. **Create a Custom AJAX Handler**:
    - Add a new AJAX endpoint for processing 3D file uploads.
    - Use the `PeepSoAjaxCallback` structure to handle file uploads.
    
    ```jsx
    class PeepSo3DFileAjax extends PeepSoAjaxCallback {
        public function upload_3d_file(PeepSoAjaxResponse $resp) {
            $file = $_FILES['file'];
            // Validate and process file
            $file_url = $this->save_3d_file($file); // Custom save logic
            if ($file_url) {
                $resp->success(TRUE);
                $resp->set('file_url', $file_url);
            } else {
                $resp->success(FALSE);
            }
        }
    }
    
    ```
    
3. **Save Uploaded Files**:
- Store files in a dedicated directory (`/wp-content/uploads/peepso/3d-files/`).
- Generate metadata for the file (e.g., dimensions, format, file size).

### **2. Data Management**

### Objective:

Store and retrieve metadata for uploaded 3D files.

### Steps:

1. **Extend the Database**:
    - Create a custom database table for 3D file metadata if necessary.
    - Store data like `file_url`, `user_id`, `timestamp`, `file_format`.
    
    ```jsx
    CREATE TABLE wp_peepso_3d_files (
        id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id BIGINT UNSIGNED NOT NULL,
        file_url TEXT NOT NULL,
        file_format VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
    
2. **Use Custom Model**:
    - Implement a model in `helloworldmodel.php` to interact with this table.
    
    ```jsx
    class PeepSo3DFileModel {
        public function save_file($user_id, $file_url, $file_format) {
            global $wpdb;
            $wpdb->insert('wp_peepso_3d_files', [
                'user_id' => $user_id,
                'file_url' => $file_url,
                'file_format' => $file_format,
            ]);
        }
    }
    ```
    

### **3. Rendering 3D Files in the Feed**

### Objective:

Display uploaded 3D files in the PeepSo social feed using a 3D viewer.

### Steps:

1. **Inject JavaScript Libraries**:
    - Add [Three.js](https://threejs.org/) to the plugin assets.
    - Enqueue the library in WordPress for the feed.
    
    ```jsx
    function enqueue_3d_viewer_scripts() {
        wp_enqueue_script('threejs', 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', [], null, true);
        wp_enqueue_script('peepso-3d-viewer', plugin_dir_url(__FILE__) . 'assets/js/3d-viewer.js', ['threejs'], null, true);
    }
    add_action('wp_enqueue_scripts', 'enqueue_3d_viewer_scripts');
    ```
    
2. **Customize Feed Output**:
    - Hook into PeepSo’s feed rendering to include a 3D viewer.
    
    ```jsx
    add_filter('peepso_feed_render', function ($output, $post) {
        if ($post->type === '3d_file') {
            $output .= '<div class="peepso-3d-container" data-file-url="' . esc_url($post->file_url) . '"></div>';
        }
        return $output;
    }, 10, 2);
    ```
    
3. **Implement a Viewer**:
    - Use Three.js to render the file in a `canvas` element.
    
    ```jsx
    document.querySelectorAll('.peepso-3d-container').forEach(container => {
        const fileUrl = container.dataset.fileUrl;
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        container.appendChild(renderer.domElement);
        const loader = new THREE.GLTFLoader();
        loader.load(fileUrl, gltf => {
            scene.add(gltf.scene);
            camera.position.z = 5;
            renderer.render(scene, camera);
        });
    });
    ```
    

### **4. Profile and Feed Integration**

### Objective:

Ensure uploaded 3D files appear on user profiles and feeds.

### Steps:

1. **Profile Integration**:
    - Extend the `widgethelloworld.php` file to render a user’s uploaded 3D files on their profile.
2. **Feed Posting**:
    - Allow users to post 3D files directly to the feed, tagging their content as `3D Media`.

```jsx
add_action('peepso_post_after_save', function ($post_id) {
    $file_url = $_POST['file_url']; // Capture from upload form
    if ($file_url) {
        update_post_meta($post_id, 'file_url', $file_url);
    }
});
```

###