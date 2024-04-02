import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="Talos - Area Dashboard",page_icon=':briefcase:',layout="wide")
'''
sales_source = pd.read_csv('sales_data.csv')
all_site_data = pd.read_csv('site_data.csv')

with st.sidebar:
    site_label = st.selectbox('Site Selection', set(sales_source['Site']))
    site_info = all_site_data[all_site_data['Site ID'] == site_label]
    sales_raw = sales_source[sales_source['Site'] == site_label]
    product_selection = st.selectbox('Product',set(sales_raw['Product']))

sales_data = sales_raw.loc[sales_raw['Product'] == product_selection]

def baseline_forecast(sales_data, start_date = date.today(), end_date = date.today() + timedelta(days = 365*2)):
'''
start_date = date.today()
end_date = date.today() + timedelta(days = 365*2)
sales_data = pd.read_csv('sales_data.csv')
sales_data = sales_data[sales_data['Site'] == 1001]
daypart_list = sales_data['Attribute'].unique()
baseline_date_list = pd.date_range(start=start_date, end=end_date, freq='D')
    
print(daypart_list)

sales_df = pd.DataFrame()

for dp in daypart_list:
    dp_df = pd.DataFrame()
    dp_df['date'] = baseline_date_list
    dp_df = dp_df.assign(daypart=dp)
    sales_df = pd.concat([sales_df,dp_df])

print(sales_df.shape[0])
print(sales_df.head(5))



   # return baseline_forecast
