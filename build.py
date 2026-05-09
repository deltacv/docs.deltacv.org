import os
import shutil
import subprocess
import sys
import modules
import download_tools

# Ensure local binaries (mdbook, mdbook-blame) are downloaded and in the PATH
download_tools.ensure_tools()

def run_command(command, cwd=None):
    cmd_str = ' '.join(command)
    print(f"Running: {cmd_str} (cwd: {cwd or '.'})")
    result = subprocess.run(cmd_str, cwd=cwd, shell=True)
    if result.returncode != 0:
        print(f"Error executing {' '.join(command)}")
        sys.exit(result.returncode)

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(root_dir, 'dist')

    # Clean the dist directory
    print(f"Cleaning {dist_dir}...")
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    
    # Build each module defined in modules.py
    for src_dir, dest_subpath in modules.MDBOOK_MODULES.items():
        print(f"\n--- Building {src_dir} ---")
        module_full_path = os.path.join(root_dir, src_dir)
        
        # Calculate destination directory inside /dist
        if dest_subpath:
            module_dist_path = os.path.join(dist_dir, dest_subpath)
        else:
            module_dist_path = dist_dir
            
        run_command(['mdbook', 'build', '-d', module_dist_path], cwd=module_full_path)
    
    # Merge global assets into dist/assets at the end
    root_assets = os.path.join(root_dir, 'assets')
    dist_assets = os.path.join(dist_dir, 'assets')
    if os.path.exists(root_assets):
        print(f"\nMerging root assets into {dist_assets}...")
        if not os.path.exists(dist_assets):
            os.makedirs(dist_assets)
        
        # Copy individual files to avoid deleting existing content in dist/assets if it exists
        for item in os.listdir(root_assets):
            s = os.path.join(root_assets, item)
            d = os.path.join(dist_assets, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        
        # Also ensure favicons are available at the root dist
        shutil.copy2(os.path.join(root_assets, 'favicon-32x32.png'), os.path.join(dist_dir, 'favicon.png'))
        shutil.copy2(os.path.join(root_assets, 'favicon.ico'), os.path.join(dist_dir, 'favicon.ico'))

    print("\nSUCCESS! All documentation has been seamlessly built into the /dist directory.")

if __name__ == '__main__':
    main()
