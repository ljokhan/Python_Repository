# Import libraries:
import dash
import pandas as pd
import urllib
import plotly.express as px
import os
import dash_bootstrap_components as dbc
from dash import html
from dash import Dash, dcc, html
from mssql_python import connect

# Register this page with Dash, so we can display it on the main menu:
dash.register_page(__name__, path='/PharmaSales-SalesByYear')

# Configure connection to Azure SQL Database:
server = 'sql-db-02-free-healthcare-server.database.windows.net'
database = 'sql-db-02-free-healthcare'
username = 'ljokhan'
password = 'NissanAltima2013#'

# Build the connection string for SQL Authentication:
connection_string = (
    f"Server={server},1433;"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    ###"login_timeout=30"
)

# This is the query used to generate the dataframe:
query = '''SELECT Year([ReportTimestamp]) as Year, 
        sum([AceticAcidDerivatives] + [PropionicAcidDerivatives] + [SalicylicAcidDerivatives] + [PyrazolonesAndAnilides] + [AnxiolyticDrugs]
                + [HypnoticsSndSedativesDrugs] + [ObstructiveAirwayDrugs] + [Antihistamines] ) as TotalSales
        FROM dbo.PharmaDrugSalesbyHour 
        GROUP BY Year([ReportTimestamp])
        ORDER BY Year'''

# Establish connection with a timeout:
conn = connect(connection_string, timeout=120)

# Create data frame using query above:
df = pd.read_sql_query(query, conn)   
   
# Create pie chart:
fig = px.pie(df, values='TotalSales', names='Year', 
             title='<b>Total Pharmaceutical Drug Sales by Year</b>')    

# Format the pie chart:
fig.update_layout(title_x=0.5) # Center title

# Display page:
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
