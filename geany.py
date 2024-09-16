import os
import urllib.request

# URL to the Geany AppImage (you can find the latest version on the Geany website)
appimage_url = "https://github.com/geany/geany/releases/download/1.38/geany-1.38.AppImage"
appimage_file = "geany.AppImage"

# Download the AppImage
print(f"Downloading Geany from {appimage_url}...")
urllib.request.urlretrieve(appimage_url, appimage_file)

# Make the AppImage executable
os.system(f"chmod +x {appimage_file}")

# Optionally move it to a location in PATH
# os.system(f"mv {appimage_file} ~/.local/bin/") # Uncomment if you want to move it

# Run the AppImage
print("Running Geany AppImage...")
os.system(f"./{appimage_file}")
