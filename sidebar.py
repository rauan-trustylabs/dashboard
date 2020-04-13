import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from datetime import datetime as dt


def Sidebar():
    sidebar = html.Div([
        html.H6("Sidebar"),
        html.Hr(),
    ])
    return sidebar