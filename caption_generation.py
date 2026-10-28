from openai import OpenAI
import base64
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.set_page_config(page_title="Automatic Caption Generator",page_icon="💬",layout="centered")
st.title("📱 CaptionCraft AI")
st.header("✨ AI-Powered Caption Generator for Viral Posts & Social Media")

file1=st.file_uploader("📷 Upload an image file",type=["png"])
if file1 is not None:
    st.image(file1,caption="📍 Uploaded Image")
    image_bytes=file1.read()
    image_base64=base64.b64encode(image_bytes).decode("utf-8")
col1,col2,col3=st.columns(3)
with col1:
 if st.button("📸Instagram"):
    prompt="""
    You are an experienced content creator,
    You have to generate caption based on the Image which has been given for Instagram,
    Rules to follow:
    1. Make the caption with emojis
    2. Don't use abusive words in the captions
    3. Keep the caption informal and friendly
    4. Mention a caption for the image belonging to different type like self love,humouros,healing etc based on the image
    5. Don't use any senstive topic as joke in the caption
    Structure:
    [Caption]
    [Add the required hashtags as you can understand from the photo, the tags can be informal and amiable, no vulgar tags are allowe]
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{image_base64}"
                    }
                ]
            }
        ]
    )
    st.write(response.output_text)

with col2:   
 if st.button("💬WhatsApp"):
    prompt="""
    You are an experienced content creator,
    You have to generate caption based on the Image which has been given foe WhatsApp,
    Rules to follow:
    1. Make the caption with emojis
    2. Don't use abusive words in the captions
    3. Keep the caption informal and friendly
    4. Mention a caption which is in between formal and informal 
    5. Don't use any senstive topic as joke in the caption
    6. These captions will be used on Whatsapp so make the caption accoringly
    Structure:
        [Caption]
        [Add the required hashtags as you can understand from the photo, keep the tags both little formal and informal]
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{image_base64}"
                    }
                ]
            }
        ]
    )
    st.write(response.output_text)

with col3:
 if st.button("💼Linkedin"):
    prompt="""
    You are an experienced professional content creator,
    You have to generate caption based on the Image which has been given for Linkedin,
    Rules to follow:
    1. Make the caption with emojis but very few
    2. Don't use abusive words in the captions
    3. Keep the caption formal and super professional
    4. Don't use any senstive topic as joke in the caption
    5. These captions will be used on Linkedin post so make the caption accoringly
    Structure:
        [Caption]
        [Add the required hashtags as you can understand from the photo, keep the tags professional]
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{image_base64}"
                    }
                ]
            }
        ]
    )
    st.write(response.output_text)