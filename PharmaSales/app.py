# Import libraries:
from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd

app = Dash(__name__, use_pages=True)
server = app.server

# Configure HTML page:
app.layout = html.Div(
    
    style={
        'background-image': 'url("/assets/Wallpaper - Pharmacy generic.jpg")',
        'background-size': 'cover',        # Scales image to cover the entire container
        'background-repeat': 'no-repeat',  # Prevents the image from tiling
        'background-position': 'center',   # Centers the image
        'height': '97vh',                 # Sets height to 100% of the viewport height
        'width': '97vw'                   # Sets width to 100% of the viewport width
    },  
    
    children=[

    # Add blank line:
    html.Br(),

    # Add logo:
    html.Div(children=[
        html.Img(src='/assets/logo.png', style={'width': '150px'})
    ],style = {"display":"flex", "justifyContent":"center"}),

    # Add menu title:
    html.H1('Pharmacy Sales Report Menu', style = {"text-align":"center", "color":"white"}),
    html.H4('(click on any menu item below)', style = {"text-align":"center", "color":"white"}),

    # Create menu as a horizontal table of buttons:
    html.Table([
        html.Tr([
            html.Td([
                dcc.Link("Daily Sales Line Chart", href="/PharmaSales-SalesByDay", style = {'color':'white', 'font-size':24, 'text-align':'center', 'font-weight':'bold'})
            ], style = {'text-align':'center'}),
            html.Td([
                dcc.Link("Monthly Sales Bar Chart", href="/PharmaSales-SalesByMonth", style = {'color':'white', 'font-size':24, 'text-align':'center', 'font-weight':'bold'})
            ], style = {'text-align':'center'}),
            html.Td([
                dcc.Link("Yearly Sales Pie Chart", href="/PharmaSales-SalesByYear", style = {'color':'white', 'font-size':24, 'text-align':'center', 'font-weight':'bold'})
            ], style = {'text-align':'center'}),
        ])
    ], style={'width':'100%'}),

    # Page content is loaded here:
    dash.page_container
])  

if __name__ == '__main__':
    app.run(debug=True)