from models.clothing_generator import generate_clothing_image

filename = generate_clothing_image(
    "formal office outfit",
    "outputs"
)

print("Generated clothing image:", filename)
