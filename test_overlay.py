from models.overlay import overlay_clothing

user_image = "uploads/Screenshot 2024-10-23 140136.png"
cloth_image = "outputs/cloth_83c85f1c174947588366eab4db4459ce.png"
output_image = "outputs/final_tryon.png"

overlay_clothing(user_image, cloth_image, output_image)
print("Final try-on saved:", output_image)
