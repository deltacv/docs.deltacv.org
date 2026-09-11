import os
import subprocess
from livereload import Server
import build  # Import the existing build.py script
import modules
import download_tools

# Ensure robust local local testing binaries
download_tools.ensure_tools()

import time

last_build_time = 0

def run_build():
    global last_build_time
    now = time.time()
    if now - last_build_time < 2:
        return
    last_build_time = now

    print("\n[serve.py] Change detected or initial build! Rebuilding docs...")
    try:
        build.main()
        print("[serve.py] Build successful! Refreshing browser...")
    except SystemExit as e:
        print(f"[serve.py] Build exited with code: {e}")
    except Exception as e:
        print(f"[serve.py] Build failed with error: {e}")

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(root_dir, 'dist')

    # Perform an initial build before starting the server
    run_build()

    # Initialize the livereload server
    server = Server()

    # Iterate dynamically over the modules
    for src_dir in modules.MDBOOK_MODULES.keys():
        mod_path = os.path.join(root_dir, src_dir)
        
        # Automatically watch the most common locations that might trigger a rebuild
        possible_watches = [
            os.path.join(mod_path, 'src'),
            os.path.join(mod_path, 'book.toml'),
            os.path.join(mod_path, 'custom.css'),
        ]
        
        # Register the watch paths with the build function
        for path in possible_watches:
            if os.path.exists(path):
                server.watch(path, run_build)
                # Pre-populate mtimes so existing files don't trigger cascading rebuilds on startup
                if path in server.watcher._tasks:
                    task = server.watcher._tasks[path]
                    if os.path.isfile(path):
                        task['mtimes'][path] = os.path.getmtime(path)
                    elif os.path.isdir(path):
                        for r, _, files in os.walk(path):
                            for f in files:
                                fp = os.path.join(r, f)
                                task['mtimes'][fp] = os.path.getmtime(fp)
                print(f"[serve.py] Watching {path}")

    # Set watcher start time to current time to avoid false positives on startup
    server.watcher._start = time.time()

    print("\n[serve.py] Starting LiveReload server...")
    print("[serve.py] Access your unified docs at: http://127.0.0.1:3000\n")
    
    # Configure custom 404 handler for local dev so unmatched URLs hit 404.html
    class CustomStaticFileHandler(server.SFH):
        def write_error(self, status_code, **kwargs):
            if status_code == 404:
                custom_404 = os.path.join(self.root, '404.html')
                if os.path.exists(custom_404):
                    self.set_header('Content-Type', 'text/html; charset=UTF-8')
                    with open(custom_404, 'rb') as f:
                        self.finish(f.read())
                    return
            super().write_error(status_code, **kwargs)

    server.SFH = CustomStaticFileHandler

    # Serve the /dist directory with automatic live reloading injection
    server.serve(root=dist_dir, port=3000, host='127.0.0.1')

if __name__ == '__main__':
    main()
