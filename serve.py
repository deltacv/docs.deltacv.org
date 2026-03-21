import os
import subprocess
from livereload import Server
import build  # Import the existing build.py script
import modules
import download_tools

# Ensure robust local local testing binaries
download_tools.ensure_tools()

def run_build():
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
                print(f"[serve.py] Watching {path}")

    print("\n[serve.py] Starting LiveReload server...")
    print("[serve.py] Access your unified docs at: http://127.0.0.1:3000\n")
    
    # Serve the /dist directory with automatic live reloading injection
    server.serve(root=dist_dir, port=3000, host='127.0.0.1')

if __name__ == '__main__':
    main()
