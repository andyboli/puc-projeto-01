from dash import dcc, html
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from view.components import TEXT, ROW_SECTION, BUTTON, DROPDOWN, MAIN_SECTION, MAIN_TITLE, CARD, BOLD_TEXT, LINK, COLUMN_SECTION, SPINNER, INTERVAL, STORE, BAR_GRAPH, DATE_RANGE_PICKER
from view.constants import COMPONENTS_IDS, STORE_STATE
from controller.orchestrator import start_app_iterations
from database.constants import TABLES

APP_STORE = [
    STORE(STORE_STATE['done']),
    STORE(STORE_STATE['error']),
    STORE(STORE_STATE['first_dimension_label']),
    STORE(STORE_STATE['first_dimension']),
    STORE(STORE_STATE['loading']),
    STORE(STORE_STATE['second_dimension_label']),
    STORE(STORE_STATE['second_dimension']),
    STORE(STORE_STATE['success']),
]

DATABASE_CARD = CARD([
    BOLD_TEXT('database'),
    LINK('database_name', 'https://dados.pbh.gov.br/dataset/populacao-de-rua')
])

AUTHORS_CARD = CARD([BOLD_TEXT('authors'), TEXT('authors_name')])

INFO_CARDS = ROW_SECTION([DATABASE_CARD, AUTHORS_CARD],
                         id=COMPONENTS_IDS["info_cards"])

PAGE_HEADER = [
    MAIN_TITLE(),
    INFO_CARDS
]

START_APP_BUTTON = BUTTON(
    children=[SPINNER(id=COMPONENTS_IDS['start_app_button_spinner']),
              TEXT('start_app', id=COMPONENTS_IDS['start_app_button_text'])],
    id=COMPONENTS_IDS["start_app_button"]
)

STATUS_SECTION = ROW_SECTION(id=COMPONENTS_IDS['status_section'])

END_APP_BUTTON = BUTTON(
    children=TEXT('end_app', id=COMPONENTS_IDS["end_app_button_text"]),
    color="warning",
    id=COMPONENTS_IDS["end_app_button"]
)

DATABASE_BUTTON = BUTTON(
    children=TEXT('show_database'),
    color="success",
    id=COMPONENTS_IDS["database_button"]
)

CHARTS_BUTTON = BUTTON(
    children=TEXT('show_charts'),
    color="success",
    id=COMPONENTS_IDS["charts_button"]
)

BAR_CHART_BUTTON = BUTTON(
    children=TEXT('bar_chart'),
    id=COMPONENTS_IDS["bar_chart_button"]
)


PIE_CHART_BUTTON = BUTTON(
    children=TEXT('pie_chart'),
    id=COMPONENTS_IDS["pie_chart_button"]
)

HIDE_CHARTS_BUTTON = BUTTON(
    children=TEXT('hide_charts'),
    color="warning",
    id=COMPONENTS_IDS["hide_charts_button"]
)


CHARTS_BUTTONS_SECTION = COLUMN_SECTION(
    [HIDE_CHARTS_BUTTON, ROW_SECTION([BAR_CHART_BUTTON, PIE_CHART_BUTTON], id=COMPONENTS_IDS['charts_buttons'])], id=COMPONENTS_IDS['charts_buttons_section'])


BAR_CHART_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"],
             options=TABLES['homeless']['headers_label']),
    DROPDOWN(id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"],
             options=TABLES['homeless']['headers_label']),
], id=COMPONENTS_IDS['bar_chart_dropdowns'])


PIE_CHART_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["pie_chart_first_dimension_dropdown"]),
    DROPDOWN(id=COMPONENTS_IDS["pie_chart_second_dimension_dropdown"]),
], id=COMPONENTS_IDS['pie_chart_dropdowns'])

PERIOD_RANGE = DATE_RANGE_PICKER(id=COMPONENTS_IDS["date_range"])


CHARTS_DROPDOWNS = [BAR_CHART_DROPDOWNS, PIE_CHART_DROPDOWNS, PERIOD_RANGE]


APP_BUTTONS = ROW_SECTION(
    children=[DATABASE_BUTTON, CHARTS_BUTTON, END_APP_BUTTON], id=COMPONENTS_IDS["app_buttons"], hide=True)


CONTROL_SECTION = COLUMN_SECTION(
    [START_APP_BUTTON, STATUS_SECTION, APP_BUTTONS], id=COMPONENTS_IDS["control_section"])


APP_CHARTS = [BAR_GRAPH(id=COMPONENTS_IDS['bar_chart'])]


CHART_SECTION = COLUMN_SECTION(
    [CHARTS_BUTTONS_SECTION, *CHARTS_DROPDOWNS, *APP_CHARTS], id=COMPONENTS_IDS['charts_section'], hide=True)


app_layout = MAIN_SECTION(
    [*APP_STORE, *PAGE_HEADER, CONTROL_SECTION, CHART_SECTION, INTERVAL(
        id=COMPONENTS_IDS["app_interval"], max_intervals=start_app_iterations)])
