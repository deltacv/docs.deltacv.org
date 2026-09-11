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

def generate_redirect_file(target_path, destination_url):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; url={destination_url}">
    <link rel="canonical" href="https://docs.deltacv.org{destination_url}">
    <script>
        window.location.replace("{destination_url}" + window.location.search + window.location.hash);
    </script>
</head>
<body>
    <p>Redirecting to <a href="{destination_url}">{destination_url}</a>...</p>
</body>
</html>
"""
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

def setup_redirects(root_dir, dist_dir):
    print("\nSetting up legacy directory redirects (eocv-sim -> visionbench, papervision -> visiongraph)...")
    
    # 1. Root-level redirect files for paths requested without trailing slashes (e.g. /eocv-sim, /papervision)
    generate_redirect_file(os.path.join(dist_dir, 'eocv-sim.html'), "/visionbench/")
    generate_redirect_file(os.path.join(dist_dir, 'eocvsim.html'), "/visionbench/")
    generate_redirect_file(os.path.join(dist_dir, 'papervision.html'), "/visiongraph/")

    # 2. Copy base redirect files from root folders if they exist (preserves custom index.html and 404.html)
    for old_mod in ["eocv-sim", "papervision"]:
        src = os.path.join(root_dir, old_mod)
        dst = os.path.join(dist_dir, old_mod)
        if os.path.exists(src):
            os.makedirs(dst, exist_ok=True)
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isfile(s):
                    shutil.copy2(s, d)

    # Also copy eocv-sim base redirects to eocvsim
    eocvsim_dst = os.path.join(dist_dir, 'eocvsim')
    os.makedirs(eocvsim_dst, exist_ok=True)
    eocv_src = os.path.join(root_dir, 'eocv-sim')
    if os.path.exists(eocv_src):
        for item in os.listdir(eocv_src):
            s = os.path.join(eocv_src, item)
            d = os.path.join(eocvsim_dst, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)

    # 3. Mirror all generated HTML files from visionbench to eocv-sim
    vb_dist = os.path.join(dist_dir, 'visionbench')
    eocv_dist = os.path.join(dist_dir, 'eocv-sim')
    if os.path.exists(vb_dist):
        for root, dirs, files in os.walk(vb_dist):
            for file in files:
                # Do not overwrite 404.html, keep the dedicated legacy 404 handler
                if file.endswith('.html') and file != '404.html':
                    full_src = os.path.join(root, file)
                    rel_path = os.path.relpath(full_src, vb_dist)
                    rel_url = rel_path.replace('\\', '/')
                    dest_url = "/visionbench/" if rel_path == "index.html" else f"/visionbench/{rel_url}"
                    
                    # Direct path in eocv-sim
                    target_file = os.path.join(eocv_dist, rel_path)
                    generate_redirect_file(target_file, dest_url)

                    # Also support extensionless paths via directory index (e.g. /eocv-sim/features/telemetry)
                    if not rel_path.endswith('index.html'):
                        rel_no_ext = rel_path[:-5]
                        dir_target = os.path.join(eocv_dist, rel_no_ext, 'index.html')
                        generate_redirect_file(dir_target, dest_url)
                    
                    # Also support renamed files (e.g. downloading-eocv-sim.html -> downloading-visionbench.html)
                    legacy_rel = rel_path.replace('visionbench', 'eocv-sim')
                    if legacy_rel != rel_path:
                        legacy_target = os.path.join(eocv_dist, legacy_rel)
                        generate_redirect_file(legacy_target, dest_url)
                        if not legacy_rel.endswith('index.html'):
                            legacy_no_ext = legacy_rel[:-5]
                            legacy_dir_target = os.path.join(eocv_dist, legacy_no_ext, 'index.html')
                            generate_redirect_file(legacy_dir_target, dest_url)

    # 4. Mirror all generated HTML files from visiongraph to papervision
    vg_dist = os.path.join(dist_dir, 'visiongraph')
    pv_dist = os.path.join(dist_dir, 'papervision')
    if os.path.exists(vg_dist):
        for root, dirs, files in os.walk(vg_dist):
            for file in files:
                # Do not overwrite 404.html, keep the dedicated legacy 404 handler
                if file.endswith('.html') and file != '404.html':
                    full_src = os.path.join(root, file)
                    rel_path = os.path.relpath(full_src, vg_dist)
                    rel_url = rel_path.replace('\\', '/')
                    dest_url = "/visiongraph/" if rel_path == "index.html" else f"/visiongraph/{rel_url}"
                    
                    # Direct path in papervision
                    target_file = os.path.join(pv_dist, rel_path)
                    generate_redirect_file(target_file, dest_url)

                    # Also support extensionless paths via directory index (e.g. /papervision/downloading-papervision)
                    if not rel_path.endswith('index.html'):
                        rel_no_ext = rel_path[:-5]
                        dir_target = os.path.join(pv_dist, rel_no_ext, 'index.html')
                        generate_redirect_file(dir_target, dest_url)
                    
                    # Also support renamed files (e.g. downloading-papervision.html -> downloading-visiongraph.html)
                    legacy_rel = rel_path.replace('visiongraph', 'papervision')
                    if legacy_rel != rel_path:
                        legacy_target = os.path.join(pv_dist, legacy_rel)
                        generate_redirect_file(legacy_target, dest_url)
                        if not legacy_rel.endswith('index.html'):
                            legacy_no_ext = legacy_rel[:-5]
                            legacy_dir_target = os.path.join(pv_dist, legacy_no_ext, 'index.html')
                            generate_redirect_file(legacy_dir_target, dest_url)

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
    
    # Setup legacy redirects
    setup_redirects(root_dir, dist_dir)
    
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
