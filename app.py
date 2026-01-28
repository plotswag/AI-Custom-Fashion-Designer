import streamlit as st
from fashion_generator import generate_fashion_design

OUTPUT_DIR = "outputs"

st.set_page_config(
    page_title="AI Custom Fashion Designer",
    layout="centered"
)

st.title("👗 AI Custom Fashion Designer")
st.write(
    "Enter **any custom fashion idea**. "
    "The AI will generate a unique dress design image based on your description."
)

prompt = st.text_area(
    "Describe your custom dress design",
    placeholder="e.g. men's party wear, black blazer with gold buttons, luxury fashion"
)

if st.button("✨ Generate Fashion Design"):
    if not prompt.strip():
        st.warning("Please enter a fashion description.")
    else:
        with st.spinner("Designing your fashion concept (CPU-based, please wait)..."):
            image_path = generate_fashion_design(prompt, OUTPUT_DIR)

        st.success("Fashion design generated successfully!")

        st.image(image_path, caption="AI Generated Fashion Design", width=350)

        with open(image_path, "rb") as f:
            st.download_button(
                "Download Image",
                f,
                file_name="fashion_design.png",
                mime="image/png"
            )
