from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!='':
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title='Visual Explorer: Describe Any Image with AI')
st.header("An Intelligent Image Q&A System")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit=st.button("Ask a Question")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is:")
    st.write(response)
