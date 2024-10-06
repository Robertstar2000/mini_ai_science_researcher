# ui.py
import streamlit as st

def display_app_header():
    st.title("AI-Powered Research Paper Generator")
    st.image("logo.png", width=200)
    st.write("Welcome to the AI-Powered Research Paper Generator. Create comprehensive research papers effortlessly.")

def get_user_input():
    st.header("Research Target Input")
    research_target = st.text_input(
        "Enter your research topic here:",
        placeholder="e.g., 'The impact of artificial intelligence on modern healthcare'"
    )
    with st.expander("Additional Options"):
        paper_type = st.selectbox(
            "Select the type of paper:",
            options=["Literature Review", "Experimental Study", "Case Study"]
        )
        paper_length = st.slider("Desired paper length (pages):", min_value=5, max_value=100, value=10)
        citation_styles = st.multiselect(
            "Preferred citation style(s):",
            options=["APA", "MLA", "Chicago"]
        )
    return research_target, paper_type, paper_length, citation_styles

def display_progress(progress):
    st.progress(progress)
