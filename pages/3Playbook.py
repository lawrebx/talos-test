import streamlit as st
import pandas as pd
from chart import diff_scatter
from comp_map import gen_comp_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Talos - Analyst Playbook",page_icon=':fuelpump:',layout="wide")

@st.cache_data
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

site_dayparts = ['Morning Commute','Lunch Rush','Evening Commute','Overnight']
sales_source = pd.read_csv('sales_data.csv')
all_site_data = pd.read_csv('site_data.csv')

with st.sidebar:
    st.image('images/Talos Logo - High Res - White Text.png',use_column_width=True)
    site_label = st.selectbox('Site Selection', set(sales_source['Site']))
    site_info = all_site_data[all_site_data['Site ID'] == site_label]
    sales_raw = sales_source[sales_source['Site'] == site_label]
    daypart_selection = st.selectbox('Daypart',site_dayparts)
    product_selection = st.selectbox('Product',set(sales_raw['Product']))

sales_data = sales_raw.loc[(sales_raw['Attribute'] == daypart_selection) & (sales_raw['Product'] == product_selection)]

sales_raw = sales_raw.merge(all_site_data, how='left', left_on='Key Comp', right_on='Site ID')

map_list = sales_raw['Key Comp'].unique().tolist()
map_list.append(site_label)

map_sites = all_site_data[all_site_data['Site ID'].isin(map_list)].copy()
map_sites['map_color'] = '#7b32a8'
map_sites.loc[map_sites['Site ID'] == str(site_label), 'map_color'] = '#a83232'  

#hcol1, hcol2, hcol3, hcol4 = st.columns([5,5,5,2])
#with hcol4:
#    st.image('Talos Logo - High Res - White Text.png',use_column_width=True)
placeholder_comp = {'Morning Commute': 'Murphy USA - Loop 288', 
                    'Lunch Rush': 'QT - State School Rd', 
                    'Evening Commute': 'Exxon - Loop 288', 
                    'Overnight': 'Chevron - Robinson Rd'}

st.title(f'{site_info["Site Name"].iloc[0]} Playbook')
st.header(f'{daypart_selection} Daypart | Key Comp: {placeholder_comp[daypart_selection]} (placeholder)')

st.divider()

st_folium(gen_comp_map(33.180382,-97.100601, 'x'), width = 925)

st.divider()

st.header('Elasticity Analysis')

fig, results = diff_scatter(sales_data, title = daypart_selection)

fig

with st.expander("Analysis Details"):
    st.write(results)

st.write(daypart_selection)

sales_csv = convert_df_to_csv(sales_data)

st.dataframe(sales_data)

st.download_button(
                   label = 'Download Sales Data',
                   data = sales_csv,
                   file_name = 'sales_output.csv',
                   mime = 'text/csv'
                   )

button_upgrade = st.button("Subscribe")

if button_upgrade:
    st.write('LFG!!!!')

like = st.checkbox('Like')

button_submit = st.button('Submit')

if button_submit:
    if like:
        st.write('Thanks bro.')
    else:
        st.write('Skill issue. Get good bro.')