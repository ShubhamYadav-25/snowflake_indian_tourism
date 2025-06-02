import plotly.express as px
import streamlit as st


def plot_yearly_bars(df):

    df = df[df['MONTHS'] != 'Total']

    """Generate separate bar charts for each year."""
    years = ["YEAR_2018", "YEAR_2019", "YEAR_2020", "YEAR_2021"]
    figures = {}
    
    for year in years:
        fig = px.bar(df, x="MONTHS", y=year, title=f"Tourist Visits in {year}")
        figures[year] = fig
    return figures

def plot_growth_rate(df):
    df = df[df['MONTHS'] != 'Total']
    return st.line_chart(df.set_index("MONTHS"))


def plot_loaded_data(df):

    states = sorted(df['State'].unique())
    selected_state = st.selectbox("Select a State", states, key="state_selector")

    filtered_df = df[df["State"] == selected_state].copy()  # Add `.copy()` to avoid modification issues
    # This gets ALL rows from the selected state
    filtered_df['Project_Cost'] = filtered_df['Project_Cost'].fillna(0)  # Replace NaNs with zero

    # Calculate total investment for selected state
    total_investment = filtered_df['Project_Cost'].sum()
    # Display total investment in a styled metric box
    st.metric(label=f"Total Investment in {selected_state}", value=f"₹{total_investment:,.2f} Lakhs")

    fig = px.scatter_mapbox(
        filtered_df,
        lat="Lattitude",
        lon="Longitude",
        hover_name="District",
        color="Project_Cost",
        size="Project_Cost",
        color_continuous_scale="Turbo",
        mapbox_style="open-street-map",
        title=f"Invested Districts in {selected_state}"
    )

    st.plotly_chart(fig)


    trend_data = filtered_df.groupby("Year of Establishment")["Project_Cost"].sum().reset_index()
    # Create the line chart
    fig_trend = px.line(
        trend_data,
        x="Year of Establishment",
        y="Project_Cost",
        title=f"Investment Trend in {selected_state}",
        markers=True,
    )
    
    st.plotly_chart(fig_trend)

def plot_regional_visitor(df):
    df = df.iloc[:-1]  # Removes the last row
    fig = px.bar(df, x="Region_Name", y=["Arrivals_2019", "Arrivals_2020", "Arrivals_2021"], 
             title="Year-wise Visitor Arrivals", 
             labels={"value": "Arrivals", "variable": "Year"},
             barmode="group")

    st.plotly_chart(fig)

    fig2 = px.line(df, x="Region_Name", y=["Percentage_Share_2019", "Percentage_Share_2020", "Percentage_Share_2021"], 
              title="Percentage Share of Visitors Over Time",
              labels={"value": "Percentage Share", "variable": "Year"})

    st.plotly_chart(fig2)
