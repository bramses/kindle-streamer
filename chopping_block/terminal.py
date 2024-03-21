import subprocess

# Get the window ID of the application you want to capture
def get_window_id(app_name):
    cmd = f"osascript -e 'tell app \"{app_name}\" to id of window 1'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None

# Define the application name you want to capture (e.g., "Safari", "Google Chrome")
app_name = "Cursor"

# Get the window ID of the specified application
window_id = get_window_id(app_name)
print(window_id)

# Check if the window ID is valid
if window_id:
    # Define the path where you want to save the screenshot
    save_path = "./screenshot.png"

    # Run the screencapture command to capture the specified window
    subprocess.run(["screencapture", "-l", window_id, "-T0", "-x", save_path])

    print(f"Screenshot of {app_name} window saved at: {save_path}")
else:
    print(f"Window ID for {app_name} not found.")