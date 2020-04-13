import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go


table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

data = [
        {
            'labels': ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'],
            'values': [4500, 2500, 1053, 500],
            'type': 'pie',
            'hole': 0.7,
        },
    ]


def Dashboard():
    dashboard = html.Div(
        [
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.Div([
                        html.H5("Click through Rate & Impressions"),
                        html.P("by Clicks, CTR and Impressions"),
                        dbc.Row(
                            dbc.CardDeck([
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H6("Card 1", className="card-title"),
                                            html.P(
                                                "Card1",
                                                className="card-text",
                                            ),
                                        ]
                                    )
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H6("Card 1", className="card-title"),
                                            html.P(
                                                "Card2",
                                                className="card-text",
                                            ),
                                        ]
                                    )
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H6("Card 1", className="card-title"),
                                            html.P(
                                                "Card3",
                                                className="card-text",
                                            ),
                                        ]
                                    )
                                )
                            ]),
                            className="justify-content-between",
                        ),
                        dcc.Graph(
                            id='line',
                            figure=go.Figure(
                                {
                                    "data": [
                                        {
                                            "x": ['2020-10-04', '2021-11-04', '2023-12-04'],
                                            "y": [90, 40, 60],
                                            "mode": "lines+markers",
                                            "name": "Line Cahrt",
                                        }
                                    ],
                                    "layout": {
                                        "height": 200,
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "margin": {
                                            "l": 0,
                                            "r": 0,
                                            "b": 0,
                                            "t": 0,
                                        },
                                        "showlegend": True,
                                        "legend": {
                                            "orientation": "h",
                                            "x": 0,
                                            "y": 1.1,
                                            "traceorder": "normal",
                                        },
                                        "xaxis": {
                                            "automargin": True,
                                            "autorange": True,
                                            "showgrid": False,
                                            "showline": True,
                                        },
                                        "yaxis": {
                                            "automargin": True,
                                            "showgrid":False,
                                            "showline": True,
                                            "autorange": True,
                                            "title": {
                                                "text": "Clicks",
                                                "standoff": 40,
                                            },
                                        },
                                        "yaxis2": {
                                            "overlaying": "y",
                                            "side": "right",
                                            "automargin": True,
                                            "showgrid": False,
                                            "showline": True,
                                            "autorange": True,
                                            "title": {
                                                "text": "Clicks",
                                                "standoff": 40,
                                            },
                                        },
                                    }
                                }
                            ),
                            config={
                                'displayModeBar': False,
                                'scrollZoom': True,
                                'responsive': True,
                            }
                        )
                    ])),
                    dbc.Col(html.Div([
                        html.H5("Conversion Rate & Cost"),
                        html.P("by Conversion Rate & Cost/Conv."),

                        dcc.Graph(
                            id='line',
                            figure=go.Figure(
                                {
                                    "data": [
                                        {
                                            "x": ['2020-10-04', '2021-11-04', '2023-12-04'],
                                            "y": [90, 40, 60],
                                            "mode": "lines+markers",
                                            "name": "Line Cahrt",
                                        }
                                    ],
                                    "layout": {
                                        "height": 200,
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "margin": {
                                            "l": 0,
                                            "r": 0,
                                            "b": 0,
                                            "t": 0,
                                        },
                                        "showlegend": True,
                                        "legend": {
                                            "orientation": "h",
                                            "x": 0,
                                            "y": 1.1,
                                            "traceorder": "normal",
                                        },
                                        "xaxis": {
                                            "automargin": True,
                                            "autorange": True,
                                            "showgrid": False,
                                            "showline": True,
                                        },
                                        "yaxis": {
                                            "automargin": True,
                                            "showgrid": False,
                                            "showline": True,
                                            "autorange": True,
                                            "title": {
                                                "text": "Clicks",
                                                "standoff": 40,
                                            },
                                        },
                                    }
                                }
                            ),
                            config={
                                'displayModeBar': False,
                                'scrollZoom': True,
                                'responsive': True,
                            }
                        )
                    ])),
                    dbc.Col(html.Div([
                        html.H5("Cost Per Click"),
                        html.P("by Cost, CPC and CPM"),

                        dcc.Graph(
                            id='line',
                            figure=go.Figure(
                                {
                                    "data": [
                                        {
                                            "x": ['2020-10-04', '2021-11-04', '2023-12-04'],
                                            "y": [90, 40, 60],
                                            "mode": "lines+markers",
                                            "name": "Line Cahrt",
                                        }
                                    ],
                                    "layout": {
                                        "height": 200,
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "margin": {
                                            "l": 0,
                                            "r": 0,
                                            "b": 0,
                                            "t": 0,
                                        },
                                        "showlegend": True,
                                        "legend": {
                                            "orientation": "h",
                                            "x": 0,
                                            "y": 1.1,
                                            "traceorder": "normal",
                                        },
                                        "xaxis": {
                                            "automargin": True,
                                            "autorange": True,
                                            "showgrid": False,
                                            "showline": True,
                                        },
                                        "yaxis": {
                                            "automargin": True,
                                            "showgrid": False,
                                            "showline": True,
                                            "autorange": True,
                                            "title": {
                                                "text": "Clicks",
                                                "standoff": 40,
                                            },
                                        },
                                    }
                                }
                            ),
                            config={
                                'displayModeBar': False,
                                'scrollZoom': True,
                                'responsive': True,
                            }
                        )
                    ])),
                ],
                align="center",
            ),
            html.Hr(),
            dbc.Row(
                [
                dbc.Col(
                    dbc.Table(table_header + table_body, bordered=True)
                ),
                dbc.Col(
                    dcc.Graph(
                        id="graph",
                        figure=go.Figure({
                            'data': data,
                            'layout': {
                                "height": 250,
                                "paper_bgcolor": "rgba(0,0,0,0)",
                                "plot_bgcolor": "rgba(0,0,0,0)",
                                'margin': {
                                    'l': 0,
                                    'r': 0,
                                    'b': 0,
                                    't': 0
                                },
                                'showlegend': False,
                            }
                        }),
                        config={
                            'displayModeBar': False,
                            'scrollZoom': True,
                            'responsive': True,
                        },
                    )
                )
                ])
        ]
    )
    return dashboard