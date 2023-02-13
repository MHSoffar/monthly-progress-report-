import pandas as pd
import streamlit as st

st.set_page_config(page_title="Progress Report" , page_icon=':bar_chart:')

df1=pd.read_excel(io=r"data.xlsx",
                engine='openpyxl',
                sheet_name='data',
                usecols='A:H',
                nrows=100000)



st.header("Tower Sorting Out :blue [Monthly Report]")



st.sidebar.header("Please Filtter Down Here :bych: :star:")

team = st.sidebar.multiselect("Team",df1["Team"].unique())
# usedas = st.sidebar.multiselect("Being_Used_As",df1["Being_Used_As"].unique())
# reporting_date = st.sidebar.multiselect("Repoting_Date",df1["Repoting_Date"].unique())



# df_selected=df1.query("Team == @team & Being_Used_As == @usedas & Repoting_Date == @reporting_date" ) 

df_selected=df1.query("Team == @team") 
st.dataframe(df_selected)












