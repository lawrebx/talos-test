import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
from area_map import gen_area_map

st.set_page_config(page_title="Talos - Executive Summary",page_icon=':monocle_face:',layout="wide")

area_dayparts = ['Morning Commute','Lunch Rush','Evening Commute','Overnight']
sales_source = pd.read_csv('sales_data.csv')
all_site_data = pd.read_csv('site_data.csv')

with st.sidebar:
    st.image('images/Talos Logo - High Res - White Text.png',use_column_width=True)
    daypart_selection = st.selectbox('Daypart',area_dayparts)
    product_selection = st.selectbox('Product',set(sales_source['Product']))

st.divider()

st_folium(gen_area_map(33.180382,-97.100601, 'x'), width = 925)

st.divider()