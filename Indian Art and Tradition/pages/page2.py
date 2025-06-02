import streamlit as st
from data_processing import get_tourism_stats
from utils import plot_yearly_bars, plot_growth_rate
def show():
    st.title("Cultural Data Insights")
    st.write("Visited Tourist in each month from 2018 to 2019 years")
    # Load Data
    df_tourism = get_tourism_stats()
    st.write(df_tourism)
    
    # Plot Yearly Bar Charts
    figs = plot_yearly_bars(df_tourism)
    for year, fig in figs.items():
        st.plotly_chart(fig)
    
    
    # # Plot Growth Rate Line Graph
    plot_growth_rate(df_tourism)

show()