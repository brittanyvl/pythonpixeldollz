import streamlit as st
from PIL import Image
from io import BytesIO

#Set page configurations
st.set_page_config(
    page_title="Doll Partz Creator",
    page_icon="🎨",
    menu_items={
        'About': "# This application allows you to upload an image and generate a pixel-art representation. It is meant to produce pixel dollz and doll partz."
    }
)


def create_pixel_art(image, pixel_size=16):
    # Resize image to small size for pixel art effect
    pixel_art = image.resize((pixel_size, pixel_size), Image.NEAREST)
    # Optionally, upscale the image to a larger size while keeping the pixelated look
    pixel_art = pixel_art.resize((pixel_size * 10, pixel_size * 10), Image.NEAREST)
    return pixel_art


def convert_image_to_bytes(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr


def main():
    st.title("Doll Partz Creator")

    # File uploader to allow the user to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption="Original Image", use_column_width=True)

        # Slider to choose pixel size for the pixel art effect
        pixel_size = st.slider("Select pixel size", 8, 128, 16)

        # Convert the image to pixel art
        pixel_art_image = create_pixel_art(image, pixel_size=pixel_size)

        # Display the pixel art image
        st.image(pixel_art_image, caption="Your Doll Partz", use_column_width=True)

        # Convert the image to bytes for downloading
        pixel_art_bytes = convert_image_to_bytes(pixel_art_image)

        # Download button to save the pixel art image
        st.download_button(
            label="Download Your Doll Partz",
            data=pixel_art_bytes,
            file_name="pixel_art_by_PythonPixelDollz.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()