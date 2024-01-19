
##############################################new show image
# import requests
# import io
# from PIL import Image
#
# # API_URL = "https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration"
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
#
# headers = {"Authorization": "Bearer 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"}
#
# def generate_image(prompt):
#     # Generates an image from the prompt using the Leonardo AI model.
#
#     try:
#         response = requests.post(API_URL, headers=headers,
#                                  json={"inputs": prompt,  "height": 512,"width": 512,
#                                        "alchemy": True,"photoReal": True,"photoRealStrength": 0.5,
#                                        "presetStyle": "CINEMATIC"})
#         response.raise_for_status()  # Raise an exception for error responses
#
#         image_bytes = response.content
#         return image_bytes
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error generating image: {e}")
#         return None
#
# def display_image(image_bytes):
#     """Opens and displays the image, or saves it if display fails."""
#
#     try:
#         image = Image.open(io.BytesIO(image_bytes))
#         image.show()  # Attempt to display the image
#
#     except Exception as e:
#         print(f"Error displaying image. Saving to file instead: {e}")
#         filename = "generated_image.jpg"
#         image = Image.open(io.BytesIO(image_bytes))
#         image.save(filename)
#
#
# # Example usage
# # prompt = "Astronaut riding a horse"
# prompt = "(Post Apacolypse Wanderer), (Female), (Fantasy Apocalyptic Setting), | (Wandering through overgrown City), | (FULL BODY Generation!!!), | (Insane clothing details), (Apocalyptic Outfit), (aesthetic style), (Clothing show skin), (Necklace), (Pistol on hip), (Military boots), (Earings), | (Long beautiful hair), (Interesting hair style), (Beautiful Face), (shiny Eyes), (Light skin), (exhausted face expression), | (Kynetic body parts), (body in motion), (Proportionate body), (Human Body), (aesthetic body), | (Complex Background), (High Resolution Image), (Cinematic), (stunning visual masterpiece!), (professional composition), (Best Quality),"
# # prompt = "A stoic marble statue stands tall in an 8k cinematic landscape, A black man. its chiseled features with a laughing expression and intricate details capturing the essence of strength and resilience."
# image_bytes = generate_image(prompt)
#
# if image_bytes:
#     display_image(image_bytes)
# else:
#     print("Image generation failed.")

################################ this is with Tkinter UI ###########################

import tkinter as tk
import requests
import io
from PIL import Image, ImageTk
import gradio as gr

# API_URL = "https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration"
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {"Authorization": "Bearer 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"}

# def generate_image(prompt):
#     """Generates an image from the prompt using the Leonardo AI model."""
#
#     try:
#         response = requests.post(API_URL, headers=headers,
#                                  json={"inputs": prompt, "height": 512, "width": 512,
#                                         "alchemy": True,"photoReal": True,"photoRealStrength": 0.5,
#                                         "presetStyle": "CINEMATIC"}
#                                  )
#         response.raise_for_status()  # Raise an exception for error responses
#
#         image_bytes = response.content
#         return image_bytes
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error generating image: {e}")
#         return None
#
# def display_image(image_bytes, image_label,width=None, height=None):
#     """Opens and displays the image in the provided label."""
#
#     try:
#         image = Image.open(io.BytesIO(image_bytes))
#         if width and height:
#             image = image.resize((width, height),Image.BICUBIC)
#         photo = ImageTk.PhotoImage(image)  # Convert to PhotoImage for Tkinter
#         image_label.config(image=photo)
#         image_label.image = photo  # Keep a reference to prevent garbage collection
#
#     except Exception as e:
#         print(f"Error displaying image: {e}")
#
#
#
# def generate_and_display():
#     prompt = prompt_entry.get()
#     image_bytes = generate_image(prompt)
#     if image_bytes:
#         display_image(image_bytes, image_label,width=512,height=512)
#     else:
#         print("Image generation failed.")
#
#
# def clear_entry():
#     prompt_entry.delete(0, tk.END)
# root = tk.Tk()
# root.geometry("800x800")
#
# root.title("Leonardo AI Image Generator")
#
# prompt_label = tk.Label(root, text="Enter a prompt:",width=70)
# prompt_label.pack()
#
# prompt_entry = tk.Entry(root,width=100)
# prompt_entry.pack()
#
# generate_button = tk.Button(root, text="Generate Image", command=generate_and_display)
# generate_button.pack()
#
# clear_button = tk.Button(root, text="Clear", command=clear_entry)
# clear_button.pack()
# image_label = tk.Label(root)
# image_label.pack()
#
#
# root.mainloop()

#################################################################

#################### AND this is with Gradio UI ###################
#
# def generate_image(prompt):
#     """Generates an image from the prompt using the Leonardo AI model."""
#
#     try:
#         response = requests.post(API_URL, headers=headers,
#                                  json={"inputs": prompt, "height": 512, "width": 512,
#                                         "alchemy": True,"photoReal": True,"photoRealStrength": 0.5,
#                                         "presetStyle": "CINEMATIC"}
#                                         )
#         response.raise_for_status()
#
#         image_bytes = response.content
#         return image_bytes
#
#     except requests.exceptions.RequestException as e:
#         return f"Error generating image: {e}"

# iface = gr.Interface(
#     fn=generate_image,
#     inputs=[gr.Textbox(lines=1, placeholder="Enter a prompt")],
#     outputs=gr.Image(),
#     title=" AI Image Generator",
# )
#
# iface.launch()
####################################################### 19 jan #############
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_URL = "https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration"
# API_URL = "https://api-inference.huggingface.co/models/Joeythemonster/anything-midjourney-v-4-1"
headers = {"Authorization": "Bearer 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"}

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


