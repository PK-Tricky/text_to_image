
#
####################################################### 19 jan #############
API_URL = "https://api-inference.huggingface.co/"


import gradio as gr
import requests
import io
from PIL import Image

def generate_image(prompt, negative_prompt="",save_path=""):
  """Generates an image from the prompt, optionally incorporating a negative prompt."""

  full_prompt = f"{prompt} {negative_prompt}" if negative_prompt else prompt

  try:
    response = requests.post(API_URL, headers=headers, json={"inputs": full_prompt})
    response.raise_for_status()

    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))  # Convert to PIL Image
    # if save_path:
    #   image.save(save_path)
    print(image,"--------image")
    return image

  except requests.exceptions.RequestException as e:
    print(e)
    # Consider returning a user-friendly error message or alternative content

iface = gr.Interface(
  fn=generate_image,
  inputs=[
    gr.components.Textbox(lines=1, placeholder="Enter a prompt"),
    gr.components.Textbox(lines=1, placeholder="Enter a negative prompt (optional)"),
    # gr.components.Textbox(lines=1, placeholder="Enter save path (optional)"),
  ],
  outputs=gr.components.Image(label="Output", type="pil", width=512, height=512),
  allow_flagging="never",
  title="AI Art Image Generator",
)

iface.launch(share=True)


