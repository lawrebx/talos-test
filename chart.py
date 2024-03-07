import pandas as pd
import plotly.express as px



def diff_scatter(df, title):

    fig = px.scatter(df, 
                 x = 'Diff', 
                 y= 'Volume',
                 trendline = 'ols'
                 )

    fig.update_layout(title = f'{title} - Elasticity to Key Competitor',
                      hovermode='x')
    
    results = px.get_trendline_results(fig).iloc[0]["px_fit_results"].summary()

    return fig, results

if __name__ == '__main__':
    sales_source = pd.read_csv('sales_data.csv')
    sales_data = sales_source[sales_source['Attribute'] == 'Morning Commute']
    fig, results = diff_scatter(sales_data, title = 'Morning Commute')
    print(type(results))
    print(results)
    fig.show()