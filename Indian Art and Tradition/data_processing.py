import snowflake.connector
import streamlit as st
import pandas as pd
import requests



def get_tourism_stats():
    conn = snowflake.connector.connect(
        user="SHUBHAM",
        password="Shubham#@77shub",
        account="TRDJOOE-XN48272",
        role="ACCOUNTADMIN",
        warehouse="MY_WAREHOUSE",  # If no warehouse is selected
        database="CULTURAL_INSIGHTS",
        schema="TOURISM_DATA"
    )
    cursor = conn.cursor()
    
    query = "SELECT * FROM TOURISM_DATA.MONTHLY_TOURISTS_DATA;"
    cursor.execute(query)
    data = cursor.fetchall()
    
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
    
    cursor.close()
    conn.close()
    
    return df


def load_data():

    url = "https://techedumike.online/all_scheme_public/SPOCS_Scheme.php"
    response = requests.get(url)
    data = response.json()  # Convert response to JSON 
    df = pd.DataFrame(data)
    
    df.rename(columns={'Located in State/UT': 'State', 'Total project cost': 'Project_Cost'}, inplace=True)
    df['Project_Cost'] = pd.to_numeric(df['Project_Cost'], errors='coerce')


    return df

def get_regional_visitors():
    conn = snowflake.connector.connect(
        user="SHUBHAM",
        password="Shubham#@77shub",
        account="TRDJOOE-XN48272",
        role="ACCOUNTADMIN",
        warehouse="MY_WAREHOUSE",  # If no warehouse is selected
        database="CULTURAL_INSIGHTS",
        schema="TOURISM_DATA"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM regional_visitors"
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    df.columns = ["Region_Name", "Arrivals_2019", "Arrivals_2020", "Arrivals_2021", 
              "Percentage_Share_2019", "Percentage_Share_2020", "Percentage_Share_2021",
              "Percentage_Change_2020_19", "Percentage_Change_2021_20"] # Removes the last row

    return df


if __name__=="main":
    load_data()