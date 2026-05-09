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
        module_src_path = os.path.join(module_full_path, 'src')
        
        # Copy root assets to module/src/assets
        root_assets = os.path.join(root_dir, 'assets')
        module_assets_path = os.path.join(module_src_path, 'assets')
        if os.path.exists(root_assets):
            if os.path.exists(module_assets_path):
                shutil.rmtree(module_assets_path)
            shutil.copytree(root_assets, module_assets_path)
            
            # Copy favicon-32x32.png as favicon.png for mdBook's native handling
            shutil.copy2(os.path.join(root_assets, 'favicon-32x32.png'), os.path.join(module_src_path, 'favicon.png'))

        # Calculate destination directory inside /dist
        if dest_subpath:
            module_dist_path = os.path.join(dist_dir, dest_subpath)
        else:
            module_dist_path = dist_dir
            
        run_command(['mdbook', 'build', '-d', module_dist_path], cwd=module_full_path)
    
    # Also copy assets to root dist for general use
    root_assets = os.path.join(root_dir, 'assets')
    dist_assets = os.path.join(dist_dir, 'assets')
    if os.path.exists(root_assets):
        print(f"\nCopying root assets to {dist_assets}...")
        if os.path.exists(dist_assets):
            shutil.rmtree(dist_assets)
        shutil.copytree(root_assets, dist_assets)
        # Also copy a favicon.png to the root dist just in case
        shutil.copy2(os.path.join(root_assets, 'favicon-32x32.png'), os.path.join(dist_dir, 'favicon.png'))
    
    print("\nSUCCESS! All documentation has been seamlessly built into the /dist directory.")

if __name__ == '__main__':
    main()
