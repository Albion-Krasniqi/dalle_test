import streamlit as st
import openai
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Set up the OpenAI client with the API key from the environment
client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

# Streamlit App
st.title("DIY Pro Image Generation")

# Input form for prompt and image size
with st.form(key='form'):
    prompt = st.text_input(label='Enter text prompt for image generation')
    #size = st.selectbox('Select size of the image', 
    #                    ('512x512', '1024x1024'))
    submit_button = st.form_submit_button(label='Generate Image')

# Generate image when the form is submitted
if submit_button:
    if prompt:
        try:
            # Generate the image using OpenAI's DALL-E API
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size='1024x1024',
                quality="standard",
                n=1,
            )

            # Extract the URL of the generated image
            image_url = response.data[0].url

            # Display the generated image
            st.image(image_url, caption="Generated Image", use_column_width=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Main entry point
if __name__ == "_main_":
    st.write("Enter a prompt to generate an image.")
