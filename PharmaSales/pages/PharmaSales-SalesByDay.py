import dash
import pandas as pd
import urllib
import plotly.express as px
import os
from dash import html
from dash import Dash, dcc, html
from mssql_python import connect

dash.register_page(__name__, path='/PharmaSales-SalesByDay')

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
       
    query = '''SELECT CAST([ReportTimestamp] as date) as ReportDate, sum([SalicylicAcidDerivatives]) as TotalSales
            FROM dbo.PharmaDrugSalesbyHour
            WHERE [ReportTimestamp] >= '2019-10-01'
            GROUP BY CAST([ReportTimestamp] as date) '''

    df = pd.read_sql_query(query, conn)  
    df.sort_values(by='ReportDate')
    
    # Create line chart:
    fig = px.line(df, x="ReportDate", y="TotalSales", 
              title='<b> Daily Sales Across All Product Lines',
              markers=True)
    fig.update_traces(line_color="#c74d06")

# Configure webpage:
layout = html.Div([
    html.Br(),
    html.Br(),
    dcc.Graph(figure=fig)
])