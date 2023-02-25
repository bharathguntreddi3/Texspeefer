import streamlit as st
import pandas as pd
import pyttsx3
from gtts import gTTS
import os
from PIL import Image

img = Image.open('speak.png')
st.set_page_config(page_title="Text To speech Converter", page_icon=img)

st.title('Text To Speech Converter')

text = st.text_input('', placeholder = 'Enter your text here')

if st.button('convert'):
    text_speech = pyttsx3.init()  # initialize
    voices = text_speech.getProperty('voices')
    text_speech.setProperty('voice', voices[1].id)
    text_speech.say(text)   # convert
    text_speech.runAndWait()


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)