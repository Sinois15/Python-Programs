# -*- coding: utf-8 -*-
"""
Ian Cedric Ng Man King
Casugol Ex.21
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("USA_Housing.csv")
print(df)
app.layout = html.Div([
    html.Label('Dropdown List of Addresses from USA_housing.py'),
    html.Div([
    dcc.Dropdown(id="Address",
        options=[
            {'label': i,
             'value': i
             } for i in df['Address']
            ], value='Address'
        )], style={'width': '100%', 'display': 'inline-block'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)