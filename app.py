from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-pro")
def get_gemini_response(prompt):
    response=model.generate_content(prompt)
    return response.text

st.set_page_config(page_title='Q&A Demo')
st.header("Gemini Application")
input=st.text_input("Input: ",key="input")

submit=st.button("Ask a Question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
