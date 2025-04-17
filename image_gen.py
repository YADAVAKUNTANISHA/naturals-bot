def generate_image(prompt, output_path):
    from PIL import Image, ImageDraw, ImageFont
    # Mocked image generation with prompt text for now
    img = Image.new('RGB', (1080, 1080), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 500), prompt, fill=(0, 100, 200), font=font)
    img.save(output_path)
    print(f"🖼️ Image saved as {output_path}")
