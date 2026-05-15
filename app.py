import streamlit as st

st.set_page_config(page_title="Paws & Portraits", layout="wide")

with open("index.html", "r") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=4000, scrolling=True)
