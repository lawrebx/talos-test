import pandas as pd
import statsmodels.api as sm

sales_raw = pd.read_csv('sales_data.csv')

sales_source = sales_raw.loc[(sales_raw['Site'] == 1001) & (sales_raw['Product'] == 'Regular') & (sales_raw['Attribute'] == 'Morning Commute')]

sales_source['Date'] = pd.to_datetime(sales_source['Date'])
sales_source['Weekday'] = sales_source['Date'].dt.day_name()
sales_source['Month'] = sales_source['Date'].dt.month_name()

weekday_dummies = pd.get_dummies(sales_source['Weekday'], dtype = float)
sales_source = pd.concat([sales_source,weekday_dummies], axis = 1)

month_dummies = pd.get_dummies(sales_source['Month'], dtype = float)
sales_source = pd.concat([sales_source,month_dummies], axis = 1)

site_list = sales_source['Site'].unique().tolist()
product_list = sales_source['Product'].unique().tolist()
daypart_list = sales_source['Attribute'].unique().tolist()
weekday_list = sales_source['Weekday'].unique().tolist()
month_list = sales_source['Month'].unique().tolist()

variable_list = weekday_list
variable_list.extend(month_list)

print(site_list)
print(product_list)
print(daypart_list)
print(weekday_list)
print(month_list)
print(variable_list)

print(sales_source.head(5))

x = sales_source[variable_list]
y= sales_source ['Volume']

est = sm.OLS(y, x).fit()

print(est.summary())

# create forecast dataframe
# create model from last 90 days - weighting options