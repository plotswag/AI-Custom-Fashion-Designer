import os
import requests
from PIL import Image
from io import BytesIO
import uuid

MODEL_ID = "stabilityai/stable-diffusion-2-1"
API_URL = f"https://router.huggingface.co/models/{MODEL_ID}"

def generate_fashion_image(prompt, output_dir):
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN not set")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    image = Image.open(BytesIO(response.content))

    os.makedirs(output_dir, exist_ok=True)
    filename = f"fashion_{uuid.uuid4().hex}.png"
    path = os.path.join(output_dir, filename)
    image.save(path)

    return path
