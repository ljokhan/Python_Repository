import dash
from dash import html

dash.register_page(__name__, path='/') 

layout = html.Div([
    html.H1('This is our home page'),
    html.Div('Welcome to the dashboard!'),
])