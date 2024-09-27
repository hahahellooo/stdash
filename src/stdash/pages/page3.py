import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime as dt
import os

st.markdown("# 📁 Upload your image file here📁")
st.sidebar.markdown("# Upload Image File")
def upload_file():
    url = "http://43.202.66.008:8021/uploadfile/"
    img_file = st.file_uploader('Upload image file', type=['png','jpg','jpeg'])
    if img_file is not None:
        files = {"file":(img_file.name, img_file.getvalue(), img_file.type)}
        response = requests.post(url, files=file)
        if response.status_code == 200:
            st.success("🎉Image uploaded successfully🎉")
            st.write(response.json())
        else:
            st.error(f"Upload failed, Please upload your image again (Error Code:{response.status_code})")
            st.write(response.text)
upload_file()

