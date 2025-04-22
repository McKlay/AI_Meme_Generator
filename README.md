---
title: AI Meme Generator
emoji: 🤖✨
colorFrom: purple
colorTo: purple
sdk: gradio
sdk_version: "4.15.0"
app_file: app.py
pinned: false
---

# AI Meme Generator 🤖✨

**Instantly generate meme captions using AI!**
- 🖼️ Image captioning: BLIP (Salesforce)
- 😂 Meme humor: Flan-T5-small
- 🖌️ Meme overlay: Pillow
- ⚡ Deployed with Gradio on Hugging Face Spaces

## How it works
1. **Upload an image**
2. **Optionally enter a meme prompt** (or leave blank for AI to generate humor)
3. **Click Submit** — Get your meme!

---

## Models Used
- [`Salesforce/blip-image-captioning-base`](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small)

---

## Requirements
gradio
transformers
torch
Pillow
opencv-python
sentencepiece

---

## Try it online!

Deployed on [Hugging Face Spaces](https://huggingface.co/spaces/McKlay/AI-Meme-Generator) 🚀

---
