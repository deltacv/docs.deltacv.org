# modules.py
# Define all the mdbook projects here.
# Key: The name of the source directory (e.g., 'visiongraph')
# Value: The subpath in the /dist folder where it should be built (use '' for root)

MDBOOK_MODULES = {
    "landing": "",                 # Builds directly into /dist
    "visionbench": "visionbench", # Builds into /dist/visionbench
    "visiongraph": "visiongraph", # Builds into /dist/visiongraph
}
