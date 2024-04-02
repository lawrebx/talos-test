import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
from portfolio_map import gen_portfolio_map

st.set_page_config(page_title="Talos - Executive Summary",page_icon=':dollar:',layout="wide")

st.header('Rule builder')

st.markdown('''Brainstorm on rulemaking UI
            Recommendations by site-product-daypart
            Slider for volume/margin tradeoff?
            Allow site-level optimziation or require ruleset at higher level with site-level overrides?
             ''')

