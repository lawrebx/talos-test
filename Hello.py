import streamlit as st
import pandas as pd
from chart import diff_scatter
from comp_map import gen_comp_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Talos - Demo Home",page_icon=':fuelpump:',layout="wide")

@st.cache_data
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

site_dayparts = ['Morning Commute','Lunch Rush','Evening Commute','Overnight']
sales_source = pd.read_csv('sales_data.csv')
all_site_data = pd.read_csv('site_data.csv')

st.header('Welcome to the Talos Experience')
st.image('images/Talos Logo - High Res - White Text.png',use_column_width=False)

