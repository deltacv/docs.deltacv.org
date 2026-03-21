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
    
    print("\nSUCCESS! All documentation has been seamlessly built into the /dist directory.")

if __name__ == '__main__':
    main()
