import streamlit as st
from PIL import Image
from io import BytesIO
from rembg import remove

# Set page configurations
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
    # Upscale the image to a larger size while keeping the pixelated look
    pixel_art = pixel_art.resize((pixel_size * 2, pixel_size * 2), Image.NEAREST)
    return pixel_art

def convert_image_to_bytes(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def remove_background(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    result = remove(img_byte_arr)
    return Image.open(BytesIO(result))

def main():
    st.title("✨Pixel Partz Creator✨")
    st.write("The Pixel Partz Creator was inspired by my love of pixel doll sites from the early 00s. To create your own pixel dollz or doll partz simply upload an image and we'll 🪄magically🪄 remove the background and create the pixel version!")

    st.header("Create Your Pixel Partz", divider=True)
    # File uploader to allow the user to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Automatically remove the background
        image_no_bg = remove_background(image)

        # Create a two-column layout for side-by-side display
        col1, col2 = st.columns(2)

        with col1:
            # Display the original image (on the left)
            st.image(image, caption="Original Image", use_column_width=True)

        with col2:
            # Slider to choose pixel size for the pixel art effect
            pixel_size = st.slider("Select pixel size", 8, 128, 64)

            # Convert the image with background removed to pixel art
            pixel_art_image = create_pixel_art(image_no_bg, pixel_size=pixel_size)

            # Display the pixel art image (on the right)
            st.image(pixel_art_image, caption="Pixel Partz", width=pixel_art_image.width)

            # Convert the image to bytes for downloading
            pixel_art_bytes = convert_image_to_bytes(pixel_art_image)

            # Download button to save the pixel art image
            st.download_button(
                label="Download Pixel Partz",
                data=pixel_art_bytes,
                file_name="pixelart_by_PythonPixelPartzCreator.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
