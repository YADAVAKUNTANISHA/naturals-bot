import os
from instagrapi import Client

def upload_to_instagram(image_path, caption):
    username = os.environ.get("INSTAGRAM_USERNAME") 
    password = os.environ.get("INSTAGRAM_PASSWORD")
    
    cl = Client()
    cl.login(username, password)
    
    cl.photo_upload(image_path, caption)
    print("📤 Uploaded to Instagram successfully!")
