import streamlit as st
from data_processing import load_data
from utils import plot_loaded_data

def show():
    st.title("Investment Overview")
    st.write("Here is the investment data of Scheme for Promotion of Culture of Science (SPOCS)")
    st.write("Retrived from https://techedumike.online/all_scheme_public/SPOCS_Scheme.php")
    df2=load_data()
    st.write(df2)
    
    plot_loaded_data(df2)

    st.write("Total investment per state")
    state_comparison = df2.groupby("State")["Project_Cost"].sum().reset_index()
    
    # Sort by highest investment
    state_comparison = state_comparison.sort_values(by="Project_Cost", ascending=False)
    
    st.dataframe(state_comparison, use_container_width=True)

show()