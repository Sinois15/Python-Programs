#module 7
#Introduction to Dashbiard development

#Import Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

#Setting Up Website Style Using CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Create a DataFrame using Pandas
df = pd.DataFrame({
 "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
 "Amount": [4, 1, 2, 2, 4, 5],
 "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

#Create Plotting Object 
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

#Create App Layout
'''
• Layout: composed of a tree of "components" like html.Div and dcc.Graph.
• dash_html_components library has a component for every HTML tag. 
html.H1(children='Hello Dash') is the same as <h1>Hello Dash</h1>
• dash_core_components describe higher-level components that are interactive are generated with 
JavaScript, HTML, and CSS through the React.js library.
• Dash is declarative: you will primarily describe your application through these attributes.
'''

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
             Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)