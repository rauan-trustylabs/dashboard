import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

PLOTLY_LOGO = "http://trustylabs.kz/img/logo.png"


def Navbar():
    navbar = dbc.Navbar([
        html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src=PLOTLY_LOGO, height="30px"),
                        ),
                        dbc.Col(dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Project 1", href="#"),
                                dbc.DropdownMenuItem("Project 2", href="#"),
                            ],
                            label="Проекты",
                            bs_size="sm"
                        ))
                    ],
                    align="center"
                )
            ),
            dbc.NavbarToggler(id="navbar-toggler")],
        color="dark",
        dark=True,
    )

    return navbar