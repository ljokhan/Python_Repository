import dash
import pandas as pd
import urllib
import plotly.express as px
from dash import html
from dash import Dash, dcc, html

dash.register_page(__name__, path='/PharmaSales-SalesByDay')

layout = html.Div([
    html.Br(),
    html.Br()
])