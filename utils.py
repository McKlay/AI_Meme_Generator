from PIL import Image, ImageDraw, ImageFont
import torch
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    T5Tokenizer,
    T5ForConditionalGeneration
)

# Load BLIP for image captioning
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model.eval()

# Load Flan-T5 for humor generation
humor_tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
humor_model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")
humor_model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
caption_model.to(device)
humor_model.to(device)

def generate_caption(image):
    """Generate a literal image description using BLIP"""
    inputs = caption_processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        output = caption_model.generate(**inputs)
    description = caption_processor.decode(output[0], skip_special_tokens=True)
    return description

def generate_funny_caption(description):
    """Generate a witty caption based on image description using Flan-T5"""
    """
    prompt = (
        f"The following is a funny and witty meme caption based on the image description:\n"
        f"Image description: {description}\n"
        f"Meme caption:"
    )
    """
    prompt = (
        f"The following is a funny and witty meme caption based on the image description:\n"
        f"{description}\nMeme caption:"
    )

    input_ids = humor_tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    output = humor_model.generate(input_ids, max_length=30)
    caption = humor_tokenizer.decode(output[0], skip_special_tokens=True)
    return caption

def overlay_caption(image, caption):
    """Overlay the final caption with dynamic font size to fit the image width."""
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)

    max_width = image.width - 40  # padding from edges
    font_size = 40  # start large

    # Try reducing font size until text fits
    while font_size > 10:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), caption, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:
            break
        font_size -= 2  # shrink font

    # Final text placement
    text_height = bbox[3] - bbox[1]
    x = (image.width - text_width) / 2
    y = image.height - text_height - 20

    # Draw black outline for contrast
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text((x + dx, y + dy), caption, font=font, fill="black")
    draw.text((x, y), caption, font=font, fill="white")

    return image

