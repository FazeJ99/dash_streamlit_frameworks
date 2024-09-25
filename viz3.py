import dash
import pandas as pd
from dash import dcc, html
import plotly.express as px

# Create Dash app instance
app = dash.Dash()

# Sample data for the bar chart
ecom_sales = {
    'Country': ['United Kingdom', 'Germany', 'France', 'Australia', 'Hong Kong'],
    'Total Sales ($)': [5000, 3000, 4000, 2000, 1000]
}
ecom_sales_df = pd.DataFrame(ecom_sales)

# Create the bar chart
bar_fig_country = px.bar(
    ecom_sales_df,
    x='Total Sales ($)',
    y='Country',
    color='Country',
    color_discrete_map={
        'United Kingdom': 'lightblue',
        'Germany': 'orange',
        'France': 'darkblue',
        'Australia': 'green',
        'Hong Kong': 'red'
    }
)

# Define app layout
app.layout = html.Div(
    children=[
        html.Div(
            style={
                'height': 250,
                'width': 250,
                'background-color': 'red'
            }
        ),
        html.Div(
            children=[
                html.H1("This box"),
                html.H2("Another Title")
            ],
            style={'background-color': 'lightblue'}
        ),
        html.H1("Sales Proportion by Country"),
        dcc.Graph(
            id='bar_graph',
            figure=bar_fig_country
        ),
        html.Div(
            style={
                'width': 150,
                'height': 150,
                'background-color': 'lightblue'
            }
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
