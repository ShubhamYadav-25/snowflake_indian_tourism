import streamlit as st
from data_processing import get_regional_visitors
from utils import plot_regional_visitor

def show():
    st.title("Regional distribution of visitors")
    df=get_regional_visitors()
    st.write(df)
    plot_regional_visitor(df)

show()