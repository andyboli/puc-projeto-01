from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash import (Dash, html, dcc)
from dash.dependencies import (Input, Output, State, )
from dash.exceptions import PreventUpdate
from controller import (reader)
import dash_bootstrap_components as dbc
import os
from database import (connection)
import matplotlib.pyplot as plt
import numpy as np

assets_path = os.getcwd() + '/assets'

app = Dash(__name__, assets_folder=assets_path,
           external_stylesheets=[dbc.themes.BOOTSTRAP])


def ROW_SECTION(children):
    return html.Div(children, className='default-auto-section default-center-row-section')


def MAIN_SECTION(children):
    return html.Div(children, className='default-section default-start-column-section main-section')


def MAIN_TITLE():
    return html.H1(reader.lang('main_title'), className='default-typography main-title')


def TEXT(key: str, id: str = ''):
    return html.P(reader.lang(key), className='default-typography', id=id)


def BOLD_TEXT(key: str):
    return html.P(reader.lang(key), className='default-typography bold-text')


def LINK(key: str, href: str):
    return html.A(reader.lang(key), href=href, className='default-typography', target='_blank')


def CARD(children):
    return html.Div(children, className='default-auto-section default-border')


def BUTTON(key: str, id: str):
    return dbc.Button(
        TEXT(key),
        color="primary",
        id=id,
        class_name='default-section default-center-row-section default-border',
        disabled=True
    )


def DROPDOWN_ITEM(option: str):
    return dbc.DropdownMenuItem(option)


def DROPDOWN(options: list, id: str):
    return dbc.DropdownMenu([*map(DROPDOWN_ITEM, options)], id=id, label="Selecione a dimensão", class_name='default-border hide')


@app.callback(
    Output(component_id='pie-graph-dropdown-1', component_property='style'),
    Output(component_id='pie-graph-dropdown-2', component_property='style'),
    Output(component_id='bar-graph-dropdown-1', component_property='style'),
    Output(component_id='bar-graph-dropdown-2', component_property='style'),
    Output(component_id='bar-graph-dropdown-3', component_property='style'),
    Output(component_id='pie-graph', component_property='style'),
    Output(component_id='bar-graph', component_property='style'),
    Input(component_id='pie-graph-button',
          component_property='n_clicks_timestamp'),
    Input(component_id='bar-graph-button',
          component_property='n_clicks_timestamp'),
)
def update_dropdown(pie_graph_dropdown_click, bar_graph_dropdown_click):
    hide = {'display': 'none'}
    show = {'display': 'block'}
    if pie_graph_dropdown_click is None and bar_graph_dropdown_click is None:
        return hide, hide, hide, hide, hide, hide, hide
    if pie_graph_dropdown_click is not None and bar_graph_dropdown_click is None:
        return show, show, hide, hide, hide, show, hide
    if pie_graph_dropdown_click is None and bar_graph_dropdown_click is not None:
        return hide, hide, show, show, show, hide, show
    if pie_graph_dropdown_click > bar_graph_dropdown_click:
        return show, show, hide, hide, hide, show, hide
    if pie_graph_dropdown_click < bar_graph_dropdown_click:
        return hide, hide, show, show, show, hide, show
    return hide, hide, hide, hide, hide, hide, hide


connection = connection.run()


@app.callback(
    Output(component_id='main-button-text', component_property='children'),
    Output(component_id='primary-button-spinner', component_property='style'),
    Output(component_id='interval-component', component_property='disabled'),
    Output(component_id='main-button', component_property='color'),
    Output(component_id='bar-graph-button', component_property='disabled'),
    Output(component_id='pie-graph-button', component_property='disabled'),
    Input(component_id='interval-component', component_property='n_intervals'),
    Input(component_id='main-button', component_property='n_clicks'),
    State(component_id='main-button-text', component_property='children')
)
def update_main_button(n_intervals, n_clicks, current_children):
    button_text = reader.lang('show_database')
    spinner_style = {'display': 'none'}
    interval_disabled = True
    button_color = 'success'
    bar_graph_button_disabled = False
    pie_graph_button_disabled = False

    button_not_clicked = n_clicks is None

    if button_not_clicked:
        button_text = reader.lang('start')
        bar_graph_button_disabled = True
        pie_graph_button_disabled = True
        return button_text, spinner_style, interval_disabled, button_color, bar_graph_button_disabled, pie_graph_button_disabled

    finished = current_children == reader.lang('show_database')

    if finished:
        return current_children, spinner_style, interval_disabled, button_color, bar_graph_button_disabled, pie_graph_button_disabled

    button_first_click = n_clicks is not None and n_intervals == 0

    if button_first_click:
        button_text = reader.lang('loading')
        spinner_style = {'display': 'block'}
        interval_disabled = False
        bar_graph_button_disabled = True
        pie_graph_button_disabled = True
        return button_text, spinner_style, interval_disabled, button_color, bar_graph_button_disabled, pie_graph_button_disabled

    on_intervals = n_intervals != 0

    if on_intervals:
        try:
            message, error = next(connection)
            bar_graph_button_disabled = True
            pie_graph_button_disabled = True
            if message is not None:
                button_text = message
                interval_disabled = False
                spinner_style = {'display': 'block'}
            if error is not None:
                button_text = error
                button_color = 'danger'
        except StopIteration:
            button_text = reader.lang('show_database')
        finally:
            return button_text, spinner_style, interval_disabled, button_color, bar_graph_button_disabled, pie_graph_button_disabled

    return button_text, spinner_style, interval_disabled, button_color, bar_graph_button_disabled, pie_graph_button_disabled


MAIN_BUTTON = dbc.Button(
    [html.Div(dbc.Spinner(size="sm"), id='primary-button-spinner'),
     TEXT('loading', id='main-button-text')],
    color="success",
    id='main-button',
    class_name='default-section default-start-row-section default-border',
)

INTERVAL = dcc.Interval(
    disabled=True,
    id='interval-component',
    interval=1*1000,
    n_intervals=0,
)

GRAPH_BUTTONS = ROW_SECTION([BUTTON(key='bar_graph', id='bar-graph-button'),
                             BUTTON(key='pie_graph', id='pie-graph-button')])

GRAPH_DROPDOWNS = ROW_SECTION(
    [
        DROPDOWN(options=['Jisoo', 'Jennie', 'Rosé', 'Lisa'],
                 id='bar-graph-dropdown-1'),
        DROPDOWN(options=['Jisoo', 'Jennie', 'Rosé', 'Lisa'],
                 id='bar-graph-dropdown-2'),
        DROPDOWN(options=['Jisoo', 'Jennie', 'Rosé', 'Lisa'],
                 id='bar-graph-dropdown-3'),
        DROPDOWN(options=['Jisoo', 'Jennie', 'Rosé', 'Lisa'],
                 id='pie-graph-dropdown-1'),
        DROPDOWN(options=['Jisoo', 'Jennie', 'Rosé', 'Lisa'],
                 id='pie-graph-dropdown-2'),

    ])

CONTROLS_SECTION = [MAIN_BUTTON, INTERVAL, GRAPH_BUTTONS, GRAPH_DROPDOWNS]


PAGE_HEADER = [
    MAIN_TITLE(),
    ROW_SECTION([CARD([BOLD_TEXT('database'),
                       LINK(
        'database_name', 'https://dados.pbh.gov.br/dataset/populacao-de-rua')
    ]), CARD([BOLD_TEXT('authors'), TEXT('authors_name')])])]


BAR_GRAPH = dcc.Graph(
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5],
                'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    },
    id="bar-graph"
)


labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
          "Rest of World"]

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[
                    [{'type': 'domain'}, {'type': 'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Global Emissions 1990-2011",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])


PIE_GRAPH = dcc.Graph(figure=fig, id="pie-graph")


GRAPH_SECTION = [BAR_GRAPH, PIE_GRAPH]


def run_view():
    app.layout = MAIN_SECTION(
        [*PAGE_HEADER, *CONTROLS_SECTION, *GRAPH_SECTION])

    app.run_server(debug=True)
