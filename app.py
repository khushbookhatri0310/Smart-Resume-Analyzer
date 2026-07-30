import streamlit as st
from ui import show_ui
# Page configuration
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
show_ui()
