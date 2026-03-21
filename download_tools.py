import os
import sys
import platform
import urllib.request
import json
import zipfile
import tarfile
import shutil

import tools

BIN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")

def get_platform_info():
    system = platform.system().lower()
    machine = platform.machine().lower()

    if machine in ['amd64', 'x86_64']:
        arch = 'x86_64'
    elif machine in ['arm64', 'aarch64']:
        arch = 'aarch64'
    else:
        arch = 'x86_64' # fallback

    # mdbook & mdbook-blame specific suffixes
    if system == 'windows':
        return f"{arch}-pc-windows-msvc.zip", ".exe"
    elif system == 'darwin':
        return f"{arch}-apple-darwin.tar.gz", ""
    else:
        # Default Linux
        return f"{arch}-unknown-linux-gnu.tar.gz", ""

def download_and_extract(url, extract_to, is_zip):
    print(f"Downloading {url}...")
    temp_file = os.path.join(BIN_DIR, "temp_download")
    try:
        urllib.request.urlretrieve(url, temp_file)
        print("Extracting...")
        if is_zip:
            with zipfile.ZipFile(temp_file, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        else:
            with tarfile.open(temp_file, 'r:gz') as tar_ref:
                tar_ref.extractall(extract_to)
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def get_latest_github_release_tag(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        return data['tag_name']

def ensure_tools():
    if not os.path.exists(BIN_DIR):
        os.makedirs(BIN_DIR)

    suffix, ext = get_platform_info()
    is_zip = suffix.endswith('.zip')

    metadata_path = os.path.join(BIN_DIR, "tools_meta.json")
    metadata = {}
    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
        except Exception:
            pass

    for tool in tools.REQUIRED_TOOLS:
        tool_name = tool['name']
        tool_path = os.path.join(BIN_DIR, f"{tool_name}{ext}")
        
        supported_os = tool.get('supported_os')
        if supported_os and platform.system().lower() not in supported_os:
            print(f"[{tool_name}] The author of this package only provides pre-built binaries for: {', '.join(supported_os)}.")
            print(f"[{tool_name}] Skipping auto-download on {platform.system()}. If this package was marked optional in book.toml, your build will gracefully continue without it!")
            continue

        version_req = tool['version']
        installed_info = metadata.get(tool_name, {})
        installed_req = installed_info.get("version_req")

        if not os.path.exists(tool_path) or installed_req != version_req:
            if not os.path.exists(tool_path):
                print(f"{tool_name} not found locally. Installing...")
            else:
                print(f"{tool_name} version changed from {installed_req} to {version_req}. Updating...")
            
            resolved_version = version_req
            if version_req == 'latest':
                try:
                    resolved_version = get_latest_github_release_tag(tool['repo'])
                except Exception as e:
                    print(f"Failed to fetch latest release for {tool_name}: {e}")
                    resolved_version = "v0.1.2" # default safe fallback

            asset_name = tool['asset_name'].format(version=resolved_version, suffix=suffix)
            url = f"https://github.com/{tool['repo']}/releases/download/{resolved_version}/{asset_name}"
            download_and_extract(url, BIN_DIR, is_zip)
            
            metadata[tool_name] = {
                "version_req": version_req,
                "version_resolved": resolved_version
            }
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=4)

    # Prepend our local bin/ folder to the system PATH so commands can natively find them!
    bin_path = os.path.abspath(BIN_DIR)
    if bin_path not in os.environ["PATH"]:
        os.environ["PATH"] = bin_path + os.pathsep + os.environ["PATH"]

if __name__ == "__main__":
    ensure_tools()
