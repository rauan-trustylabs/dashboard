import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
from sidebar import Sidebar
from dashboard import Dashboard

nav = Navbar()
side = Sidebar()
dashboard = Dashboard()

body = dbc.Container(
    [
        dbc.Row([
                    dbc.Col(html.Div(side), lg=2),
                    dbc.Col(html.Div(dashboard)),
        ])
    ],
    fluid=True
)


def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout


