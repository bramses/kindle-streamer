import subprocess
import re
import time
from datetime import datetime
from ocr import ocr_image
from create_art import create_art_prompt, create_art
import json
from dotenv import load_dotenv
import os

load_dotenv()

fullpath = os.getenv("FULLPATH_OUTPUT")
while True:
    # Run the windowlist command and capture the output
    output = subprocess.run(['./windowlist'], capture_output=True, text=True).stdout

    # Search for the Kindle window ID
    match = re.search(r'Kindle:Window:(\d+)', output)
    if match:
        kindle_id = match.group(1)
        print(f"Kindle Window ID: {kindle_id}")

        # Format the date for the screenshot filename
        date_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"{fullpath}-{date_str}.png"

        # Take a screenshot of the Kindle window
        subprocess.run(['screencapture', '-l', kindle_id, '-x', filename])
        print(f"Screenshot saved as {filename}")
    else:
        print("Kindle window not found.")

    
    # Perform OCR on the screenshot
    text = ocr_image(filename)
    print(f"OCR Text: {text}")

    # Generate an art prompt from the OCR text
    art_prompt = create_art_prompt(text)
    print(f"Art Prompt: {art_prompt}")

    # Generate art from the art prompt
    art_url = create_art(art_prompt)
    print(f"Art URL: {art_url}")

    # save the art image to the output/art folder
    art_filename = f"./output/art/{date_str}.png"
    subprocess.run(['curl', art_url, '-o', art_filename])
    print(f"Art saved as {art_filename}")

    # save all above as json to the output/logs folder as pretty printed json
    log_filename = f"./output/logs/{date_str}.json"
    with open(log_filename, 'w') as f:
        f.write(json.dumps({
            "screenshot": filename,
            "ocr_text": text,
            "art_prompt": art_prompt,
            "art_url": art_url,
            "art_filename": art_filename
        }, indent=4))

    # Wait for a minute before running again
    time.sleep(60)
