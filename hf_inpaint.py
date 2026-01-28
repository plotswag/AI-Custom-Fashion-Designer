import os
import base64
import requests
from PIL import Image
from io import BytesIO
import uuid

MODEL_ID = "stabilityai/stable-diffusion-2-inpainting"
API_URL = f"https://router.huggingface.co/models/{MODEL_ID}"

def inpaint_clothing(image_path, mask_path, prompt, output_dir):
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN not set")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    with open(mask_path, "rb") as f:
        mask_bytes = f.read()

    payload = {
        "inputs": {
            "image": base64.b64encode(image_bytes).decode("utf-8"),
            "mask_image": base64.b64encode(mask_bytes).decode("utf-8"),
            "prompt": prompt
        }
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=180
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    image = Image.open(BytesIO(response.content))

    os.makedirs(output_dir, exist_ok=True)
    filename = f"tryon_{uuid.uuid4().hex}.png"
    path = os.path.join(output_dir, filename)
    image.save(path)

    return path
