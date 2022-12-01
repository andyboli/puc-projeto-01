from dash import Dash
import dash_bootstrap_components as dbc
import os

from view.callbacks import create_callbacks
from view.layout import app_layout

assets_path = os.getcwd() + '/assets'

app = Dash(__name__, assets_folder=assets_path,
           external_stylesheets=[dbc.themes.BOOTSTRAP])


def run_view():
    app.layout = app_layout
    create_callbacks(app).run(debug=True)
