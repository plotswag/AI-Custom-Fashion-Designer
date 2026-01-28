import os
import sys

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from models.image_generator import generate_outfit_image

prompt = "A professional formal office outfit, clean design, smart and elegant"

output = generate_outfit_image(prompt, "outputs")

print("Generated image:", output)
