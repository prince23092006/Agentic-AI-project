import streamlit as st

st.set_page_config(
    page_title="StartupPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 StartupPilot AI")

idea = st.text_area("Enter your Startup Idea")

if st.button("Analyze Startup"):
    st.success("Analysis Started...")
