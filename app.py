import gradio as gr
from utils import generate_caption, generate_funny_caption, overlay_caption
"""
def meme_generator(image, prompt=None):
    description = generate_caption(image)
    funny_caption = generate_funny_caption(description)
    final_caption = prompt if prompt else funny_caption
    meme = overlay_caption(image, final_caption)
    return meme
"""
def meme_generator(image, prompt=None):
    if prompt:
        # Use the user’s input as prompt to the language model
        funny_caption = generate_funny_caption(prompt)
    else:
        # Use image captioning + humor generation
        description = generate_caption(image)
        funny_caption = generate_funny_caption(description)
    
    meme = overlay_caption(image, funny_caption)
    return meme

demo = gr.Interface(
    fn=meme_generator,
    inputs=[
        gr.Image(type="pil", label="Upload an image"),
        gr.Textbox(label="Optional custom caption (leave blank to auto-generate humor)")
    ],
    outputs=gr.Image(type="pil", label="Meme Output"),
    title="AI Meme Generator 🤖✨",
    description="Upload an image and let AI generate a funny meme caption using BLIP + Flan-T5!"
)

if __name__ == "__main__":
    demo.launch()
