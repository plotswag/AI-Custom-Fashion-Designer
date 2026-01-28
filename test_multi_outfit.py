from models.clothing_generator import generate_clothing_image
from models.overlay import overlay_clothing

# CHANGE THIS to your real uploaded image
USER_IMAGE = "uploads/Screenshot 2024-10-23 140136.png"

STYLES = {
    "casual": "casual outfit",
    "formal": "formal office outfit",
    "party": "party wear outfit",
    "ethnic": "traditional ethnic outfit"
}

for key, style in STYLES.items():
    print(f"Generating {key} outfit...")

    cloth_image = generate_clothing_image(style, "outputs")
    final_output = f"outputs/{key}_tryon.png"

    overlay_clothing(
        USER_IMAGE,
        f"outputs/{cloth_image}",
        final_output
    )

    print(f"{key.capitalize()} try-on saved as {final_output}")
