# train_notifier/image_tools.py
from PIL import Image

def combine_images(img_paths, output_path="combined.png", cols=2, scale=0.5):
    imgs = [Image.open(p) for p in img_paths]
    resized = [img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS) for img in imgs]
    w, h = resized[0].size
    rows = (len(resized) + cols - 1) // cols
    combined = Image.new("RGB", (cols * w, rows * h), (255, 255, 255))
    for idx, img in enumerate(resized):
        combined.paste(img, ((idx % cols) * w, (idx // cols) * h))
    combined = combined.convert("RGB")
    combined.save(output_path, format="JPEG", quality=80, optimize=True)
    return output_path
