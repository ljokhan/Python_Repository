import dash
import pandas as pd
import urllib
import plotly.express as px
import os
import dash_bootstrap_components as dbc
from dash import html
from dash import Dash, dcc, html
from mssql_python import connect

# Register this page with the Dash Application:
dash.register_page(__name__, path='/PharmaSales-SalesByYear')

# Configure connection to Azure SQL Database:
server = 'sql-db-02-free-healthcare-server.database.windows.net'
database = 'sql-db-02-free-healthcare'
username = 'ljokhan'
password = 'NissanAltima2013#'

# Build the connection string for SQL Authentication:
conn_str = (
    f"Server={server},1433;"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    ###"login_timeout=30"
)

# Establish connection
with connect(conn_str) as conn:
       
    query = '''SELECT Year([ReportTimestamp]) as Year, 
        sum([AceticAcidDerivatives] + [PropionicAcidDerivatives] + [SalicylicAcidDerivatives] + [PyrazolonesAndAnilides] + [AnxiolyticDrugs]
                + [HypnoticsSndSedativesDrugs] + [ObstructiveAirwayDrugs] + [Antihistamines] ) as TotalSales
        FROM dbo.PharmaDrugSalesbyHour 
        GROUP BY Year([ReportTimestamp])
        ORDER BY Year'''

    df = pd.read_sql_query(query, conn)   
    
    # Create pie chart:
    fig = px.pie(df, values='TotalSales', names='Year', 
             title='<b>Total Pharmaceutical Drug Sales by Year</b>')    
    fig.update_layout(title_x=0.5) # Center title

# Configure webpage:
layout = html.Div([
    html.Br(),
    html.Table([
        html.Tr([
            html.Td("", style={'width':'30%'}),
            html.Td(dcc.Graph(figure=fig), style={'width':'40%'}),
            html.Td("", style={'width':'30%'})
        ])
    ],style={'width':'100%','border':'0px solid black'})
])
