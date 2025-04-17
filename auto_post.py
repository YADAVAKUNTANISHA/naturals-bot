import os
import json
import random
import datetime
from image_gen import generate_image
from uploader import upload_to_instagram

# Load prompt list
with open("prompts.txt", "r", encoding="utf-8") as file:
    prompts = file.read().splitlines()

# Load configuration (hashtags, captions, etc.)
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# Choose a prompt
prompt = random.choice(prompts)

# Create filename with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"naturals_{timestamp}.png"

# Step 1: Generate the image
generate_image(prompt, filename)

# Step 2: Upload to Instagram
caption = f"{prompt}\n\n{config['caption']}\n\n{config['hashtags']}"

upload_to_instagram(filename, caption)

print("✅ Image generated and posted successfully!")
