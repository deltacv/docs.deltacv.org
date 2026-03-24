# tools.py
# Define all native executables required for building the documentation framework locally

REQUIRED_TOOLS = [
    {
        "name": "mdbook",
        "repo": "rust-lang/mdBook",
        "version": "v0.5.2",
        "asset_name": "mdbook-{version}-{suffix}"
    },
    {
        "name": "mdbook-blame",
        "repo": "deltacv/mdbook-blame",
        "version": "v0.1.0",
        "asset_name": "mdbook-blame-{version}-{suffix}"
    }
]
