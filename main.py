import streamlit as st
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Streamlit App
st.title("DALL·E Image Generation")

# Input form for prompt and image size
with st.form(key='form'):
    prompt = st.text_input(label='Enter text prompt for image generation')
    size = st.selectbox('Select size of the image', 
                        ('512x512', '1024x1024'))
    submit_button = st.form_submit_button(label='Generate Image')