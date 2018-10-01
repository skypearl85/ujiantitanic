import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from categoryplot import getPlot, dfTitanic, dfStd

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Tabs(id='tabs', value='tab-1',children=[
        dcc.Tab(label='Tips Data Set', value='tab-1',children=[
            html.Div([
                html.H1(children = 'Table Titanic'),
                 html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Table: ')
                        ]),
                        html.Td([
                            dcc.Dropdown(
                                id='ddl-table',
                                options=[{'label': 'titanic', 'value': 'titanic'},
                                    {'label': 'titanicOutlierCalculation', 'value': 'outlier'}
                                ],
                                value = 'titanic'
                            )
                        ])
                    ])
                )
            ]),
            html.Div([
                dcc.Graph(
                    id='tableTitanic',
                    figure = {
                    'data':[
                        go.Table(
                            header=dict(
                                values=dfTitanic.columns,
                                font=dict(size=18),
                                height=30,
                                fill = dict(color='#46a3cb')
                            ),
                            cells=dict(
                                values=[dfTitanic[col] for col in dfTitanic.columns],
                                height=30,
                                font=dict(size=16),
                                fill = dict(color='#e5e8ed')
                            )
                        )
                    ],
                    'layout': go.Layout(height=600, margin={'t':10})
                    }
                )
            ])
        ]),
        dcc.Tab(label='Tips Data Set', value='tab-2',children=[
            html.Div([
                html.H1(children = 'Categorical Plot Ujian Titanic'),
                html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Type: '),
                            dcc.Dropdown(
                                id='ddl-plot-category',
                                options=[{'label': 'Bar', 'value': 'bar'},
                                    {'label': 'Violin', 'value': 'violin'},
                                    {'label': 'Box', 'value': 'box'}
                                ],
                                value = 'bar'
                            )
                        ]),
                        html.Td([
                            html.P('X axis: '),
                            dcc.Dropdown(
                                id='ddl-x-category',
                                options=[{'label': 'Survived', 'value': 'survived'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Ticket class', 'value': 'pclass'},
                                    {'label': 'Embark Town', 'value': 'embark_town'},
                                    {'label': 'Who', 'value': 'who'},
                                    {'label': 'Outlier', 'value': 'outlier'}
                                ],
                                value = 'sex'
                            )
                        ])
                    ]),
                    style = {
                        'width':'900px'
                    }
                ),
                dcc.Graph(
                    id = 'categoricalPlot',
                    figure = {}
                )
            ])
        ])
    ])
])

@app.callback(
    Output('categoricalPlot', 'figure'),
    [Input('ddl-plot-category', 'value'),
    Input('ddl-x-category', 'value')]
)
def update_category_graph(ddlcateogrytype, ddlxtype):
    return {
        'data':getPlot(ddlcateogrytype, ddlxtype),
        'layout':
            go.Layout(
                xaxis = {'title': ddlxtype.capitalize()},
                yaxis = {'title': 'US$'},
                margin = {'l': 40, 'b':40, 't':10, 'r':10},
                boxmode = 'group', violinmode = 'group',
                hovermode = 'closest'
            )
    }

if __name__ == '__main__':
    #debug True, automatic refresh after update
    app.run_server(debug=True, port=8080)
