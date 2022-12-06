from dash import (dash_table, dcc, html)
from math import ceil
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

from controller.orchestrator import start_app_iterations
from controller.reader import lang


def ALERT(children="", color="success", text_color="success"):
    return dbc.Alert(
        children=[
            html.I(className="bi bi-check-circle-fill me-2"),
            children,
        ],
        color=color,
        className="default-section default-row-section default-border",
    )


def BAR_CHART(id: str = ''):
    return dcc.Graph(id=id)


def BOLD_TEXT(key: str):
    return html.P(lang(key), className='default-bold-typography')


def BUTTON(children: any, id: str, color: str = "primary"):
    return dbc.Button(
        children=children,
        class_name='default-section default-row-section default-border',
        color=color,
        id=id,
    )


def CARD(children):
    return html.Div(children, className='default-section default-white-section default-border')


def COLUMN_SECTION(children: any = "", id="", hide=False):
    if hide:
        return html.Div(children, className='default-section default-column-section default-hide-section', id=id)
    return html.Div(children, className='default-section default-column-section', id=id)


def DATE_PICKER_RANGE(id: str):
    return dcc.DatePickerRange(
        start_date_placeholder_text=lang(
            'component_start_date_placeholder'),
        end_date_placeholder_text=lang("component_end_date_placeholder"),
        calendar_orientation='vertical',
        display_format="DD MM YYYY",
        id=id,
        min_date_allowed='2019-01-01',
        className='default-section default-border'
    )


def DROPDOWN(options: dict = {}, id=''):
    return dbc.DropdownMenu([*map(lambda option: DROPDOWN_ITEM(option=option, id=id), options.items())], id=id, label=lang("component_dropdown_label"), class_name='default-border')


def DROPDOWN_ITEM(option: tuple, id: str):
    key, value = option
    return dbc.DropdownMenuItem(value, id=key + '-' + id)


def INTERVAL(id: str):
    return dcc.Interval(
        disabled=True,
        id=id,
        interval=2*1000,
        max_intervals=start_app_iterations,
        n_intervals=0,
    )


def LINK(key: str, href: str):
    return html.A(lang(key), href=lang(href), className='default-typography', target='_blank')


def MAIN_SECTION(children: any = ""):
    return html.Div(children, className='main-section default-column-section')


def MAIN_TITLE():
    return html.H1(lang('component_main_title_text'), className='default-typography main-title')


def PIE_CHART():
    first_dimension_values = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
                              "Rest of World"]

    second_dimension_values = ["GHG", "CO2", "CH4", "CH3", "O2"]

    second_dimension_length = len(second_dimension_values)

    cols = 2
    rows = ceil(second_dimension_length / cols)

    initial_x = cols * 0.19
    initial_y = rows*0.31

    x_gap = 0.60
    y_gap = 0.42

    fig = make_subplots(rows=rows, cols=cols, specs=[
                        [{'type': 'domain'} for _ in range(cols)] for _ in range(rows)])

    annotations = []

    for name in second_dimension_values:
        value_index = second_dimension_values.index(name) + 1
        col = cols - value_index % cols
        row = ceil(value_index / cols)
        x = initial_x + (col - 1)*x_gap
        y = initial_y - (row - 1)*y_gap
        fig.add_trace(go.Pie(labels=first_dimension_values, values=[16, 15, 12, 6, 5, 4, 42], name=name),
                      col=col, row=row)
        annotations.append(dict(text=name, x=x, y=y,
                           font_size=20, showarrow=False))

    fig.update_traces(hoverinfo="label+percent+name")

    fig.update_layout(title_text="Global Emissions 1990-2011",
                      annotations=annotations)

    return dcc.Graph(figure=fig, id="pie-graph")


def ROW_SECTION(children: any = "", id="", hide=False):
    if hide:
        return html.Div(children, className='default-section default-row-section default-hide-section', id=id)
    return html.Div(children, className='default-section default-row-section', id=id)


def SPINNER(id: str):
    return html.Div(dbc.Spinner(size="sm"), id=id, className="default-hide-section")


def STORE(id: str):
    return dcc.Store(id=id)


def TABLE():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

    return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])


def TEXT(key: str, id: str = ''):
    return html.P(lang(key), className='default-typography', id=id)
