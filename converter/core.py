# converter/core.py
import os
from wand.image import Image

SUPPORTED_INPUT_FORMATS = ['.heic', '.png', '.bmp', '.tiff', '.tif', '.gif', '.webp', '.jpeg', '.jpg']

def is_supported_image(path):
    ext = os.path.splitext(path)[1].lower()
    return ext in SUPPORTED_INPUT_FORMATS

def convert_image_to_jpg(image_path, output_dir):
    if not is_supported_image(image_path):
        return f"⚠ Skipped: {os.path.basename(image_path)}"
    try:
        base = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join(output_dir, base + ".jpg")
        with Image(filename=image_path) as img:
            img.format = 'jpeg'
            img.save(filename=output_path)
        return f"✓ Converted: {os.path.basename(output_path)}"
    except Exception as e:
        return f" Failed: {os.path.basename(image_path)} - {str(e)}"
