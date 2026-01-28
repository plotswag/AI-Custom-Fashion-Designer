import os
import uuid
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import streamlit as st

@st.cache_resource(show_spinner=False)
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cpu")
    return pipe

def generate_fashion_design(prompt, output_dir):
    pipe = load_pipeline()

    image = pipe(
        prompt,
        num_inference_steps=15,
        guidance_scale=7.5
    ).images[0]

    filename = f"fashion_{uuid.uuid4().hex}.png"
    path = os.path.join(output_dir, filename)
    image.save(path)

    return path
