import streamlit as st
from data_processing import get_tourism_stats, load_data
from utils import plot_yearly_bars, plot_growth_rate , plot_loaded_data
from pages import page1, page2

st.title("Welcome to Indian Art & Tradition Web App")
st.write("Select an option from the sidebar to explore!")

st.markdown("""
# 📜 Project Overview: Preserving India’s Cultural Heritage Through Data & Storytelling

India’s vast cultural and artistic heritage deserves an immersive and interactive platform that not only showcases **traditional art forms** but also unveils deeper insights into **tourism trends and responsible travel**.

Your **Streamlit-powered solution** aims to bridge this gap by integrating **data-driven storytelling** with rich visualization, offering travelers and cultural enthusiasts a **comprehensive, engaging, and insightful experience**.

This initiative will dive deep into **seasonal tourism patterns, hidden cultural gems, and government efforts** in cultural preservation, turning raw datasets into a compelling narrative that **educates, inspires, and promotes sustainable tourism**.
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .title {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        color: #ff7f50;
    }
    .subtitle {
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
        color: #444;
    }
    .text {
        font-size: 18px;
        line-height: 1.6;
        color: #555;
    }
</style>

<div class='title'>📜 Project Overview: Preserving India’s Cultural Heritage Through Data & Storytelling</div>
<div class='text'>
India’s vast cultural and artistic heritage deserves an immersive and interactive platform that not only showcases <b>traditional art forms</b> but also unveils deeper insights into <b>tourism trends and responsible travel</b>.
</div>
<div class='text'>
Your <b>Streamlit-powered solution</b> aims to bridge this gap by integrating <b>data-driven storytelling</b> with rich visualization, offering travelers and cultural enthusiasts a <b>comprehensive, engaging, and insightful experience</b>.
</div>
<div class='text'>
This initiative will dive deep into <b>seasonal tourism patterns, hidden cultural gems, and government efforts</b> in cultural preservation, turning raw datasets into a compelling narrative that <b>educates, inspires, and promotes sustainable tourism</b>.
</div>
""", unsafe_allow_html=True)

