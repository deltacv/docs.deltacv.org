# modules.py
# Define all the mdbook projects here.
# Key: The name of the source directory (e.g., 'papervision')
# Value: The subpath in the /dist folder where it should be built (use '' for root)

MDBOOK_MODULES = {
    "landing": "",           # Builds directly into /dist
    "eocv-sim": "eocv-sim",         # Builds into /dist/eocvsim
    "papervision": "papervision", # Builds into /dist/papervision
}
