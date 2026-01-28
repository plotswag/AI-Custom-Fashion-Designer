import os
import base64
import requests
from PIL import Image
import io
import uuid

API_URL = "https://router.huggingface.co/fal-ai/fal-ai/flux-2/edit?_subdomain=queue"

def edit_clothing(image_path, prompt, output_dir):
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN environment variable not set")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    payload = {
        "inputs": base64.b64encode(image_bytes).decode("utf-8"),
        "parameters": {
            "prompt": prompt,
            "strength": 0.75
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

    image = Image.open(io.BytesIO(response.content))

    filename = f"tryon_{uuid.uuid4().hex}.png"
    output_path = os.path.join(output_dir, filename)
    image.save(output_path)

    return output_path
