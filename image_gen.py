from PIL import Image, ImageDraw, ImageFont

def generate_image(prompt, output_path):
    img = Image.new('RGB', (1080, 1080), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((10, 500), prompt, fill=(0, 100, 200), font=font)
    img.save(output_path)
    print(f"🖼️ Image saved as {output_path}")
