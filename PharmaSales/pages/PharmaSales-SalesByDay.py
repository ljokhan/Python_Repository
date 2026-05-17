# Import libraries:
import dash
import pandas as pd
import urllib
import plotly.express as px
import os
from dash import html
from dash import Dash, dcc, html
from mssql_python import connect

# Register this page with Dash, so we can display it on the main menu:
dash.register_page(__name__, path='/PharmaSales-SalesByDay')

# Configure connection to Azure SQL Database:
server = 'sql-db-01-ljokhan-server.database.windows.net'
database = 'sql-db-01-ljokhan'
username = 'PythonUser'
password = 'ILovePython2026!'

# Build the connection string for SQL Authentication:
connection_string = (
    f"Server={server},1433;"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)
   
# This is the query used to generate the dataframe:
query = '''SELECT CAST([ReportTimestamp] as date) as ReportDate, 
            sum([AceticAcidDerivatives] + [PropionicAcidDerivatives] + [SalicylicAcidDerivatives] + [PyrazolonesAndAnilides] + [AnxiolyticDrugs]
                + [HypnoticsSndSedativesDrugs] + [ObstructiveAirwayDrugs] + [Antihistamines] ) as TotalSales
            FROM dbo.PharmaDrugSalesbyHour
            WHERE [ReportTimestamp] >= '2019-10-01'
            GROUP BY CAST([ReportTimestamp] as date) '''

# Establish connection with a timeout:
conn = connect(connection_string, timeout=180)

# Create data frame using query above:
df = pd.read_sql_query(query, conn)  
df.sort_values(by='ReportDate')
    
# Create line chart using the dataframe:
fig = px.line(df, x="ReportDate", y="TotalSales", 
              title='<b> Daily Pharmaceutical Drug Sales - All Product Lines',
              markers=True)
    
# Format the line chart:
fig.update_traces(line_color="#c74d06")
fig.update_layout(title_x=0.5) # Center title

# Display page:
layout = html.Div([
    html.Br(),
    html.Table([
        html.Tr([
            html.Td("", style={'width':'5%'}),
            html.Td(dcc.Graph(figure=fig), style={'width':'90%'}),
            html.Td("", style={'width':'5%'})
        ])
    ],style={'width':'100%','border':'0px solid black'})
])