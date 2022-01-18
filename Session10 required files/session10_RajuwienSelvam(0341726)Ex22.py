"""
@author: Rajuwien Selvam 0341726
"""
#Importing libraries 
import dash  
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px
import pandas as pd
import numpy as np

#Reading file
dataframe = pd.read_csv('USA_Housing.csv')

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div(children=[
        html.Button('Create a New Chart', id='add_chart', n_clicks=0),
    ]),
    html.Div(id='container', children=[])
])

@app.callback(
    Output('container', 'children'),
    [Input('add_chart', 'n_clicks')],
    [State('container', 'children')]
)

#display the graph and dropdown lists
def display_components(n_clicks, div_children):
    new_child = html.Div(
        style={'width': '90%', 'display': 'inline-block', 'outline': 'bold', 'padding': 20},
        children=[
            #graph component
            dcc.Graph(
                id={
                    'type': 'dynamic-graph',
                    'index': n_clicks
                },
                figure={}
            ),
            dcc.RadioItems( 
                id={
                    'type': 'dynamic-choice',
                    'index': n_clicks
                },
                options=[{'label': '2D Bar Chart', 'value': 'bar'},
                         {'label': '2D Pie Chart', 'value': 'pie'}],
                value='bar',
            ),
            html.P(),
            #addresses dropdown list
            "Addresses:",
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-s',
                    'index': n_clicks
                },
                options=[{'label': x, 'value': x} for x in np.sort(dataframe['Address'].unique())],
                multi=True,
                value=["208 Michael Ferry Apt. 674", "188 Johnson Views Suite 079"],
            ),
            html.P(),
            #seperate Div to have both lists side by side
            html.Div(
                style={'display': 'flex', 'outline': 'bold'},
                children=[
                    #x-axis dropdown list
                    html.Div(children = [
                        "X-Axis:",
                        dcc.Dropdown( #X axis 
                            id={
                                'type': 'dynamic-category',
                                'index': n_clicks
                            },
                            options=[{'label': y, 'value': y} for y in ['Avg. Area House Age', 'Area Population', 'Address']],
                            value='Address',
                            clearable=False
                        )
                    ], style=dict(width='50%')),
                    #div just to make space
                    html.Div(style=dict(width='2%')),
                    #y-axis dropdown list
                    html.Div(children=[
                        "Y-Axis:",
                        dcc.Dropdown( #Y axis 
                            id={
                                'type': 'dynamic-num',
                                'index': n_clicks
                            },
                            options=[{'label': z, 'value': z} for z in ['Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Avg. Area Income', 'Price']],
                            value='Price',
                            clearable=False
                        )
                    ], style=dict(width='50%'))
                ]
            )
        ]   
    )
    
    div_children.append(new_child)
    return div_children

#callback function
@app.callback(
    Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
    [Input(component_id={'type': 'dynamic-dpn-s', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-category', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-num', 'index': MATCH}, component_property='value'),
     Input({'type': 'dynamic-choice', 'index': MATCH}, 'value')]
)

#Update
def update_graph(value, cvalue, num_value, chart_choice):
    print(value)
    dataframef = dataframe[dataframe['Address'].isin(value)]

    if chart_choice == 'bar':
        dataframef = dataframef.groupby([cvalue], as_index=False)[['Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Avg. Area Income', 'Price']].sum()
        fig = px.bar(dataframef, x=cvalue, y=num_value)
        return fig
    elif chart_choice == 'pie':
        fig = px.pie(dataframef, names=cvalue, values=num_value)
        return fig

#run app
if __name__ == '__main__':
    app.run_server(debug=False)

